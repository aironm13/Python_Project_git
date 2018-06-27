from wsgiref.simple_server import make_server
from webob.dec import wsgify
from webob import Response, Request
from webob.exc import HTTPNotFound



# Version 2
# 1，修改注册为装饰器
# class Route:
#     ROUTETABLE = {}
#
#     # register定义为类的方法
#     @classmethod
#     def register(cls, path, handler):
#         cls.ROUTETABLE[path] = handler
#
#
# def indexhandler(request:Request):
#     return '<h1>Index hello word</h1>'
#
# def pythonhandler(request:Request):
#     return '<h1>Python hello word</h1>'

# 使用类的register方法进行注册
# Route.register('/', indexhandler)
# Route.register('/python', pythonhandler)

class Route:
    ROUTETABLE = {}

    @classmethod
    def register(cls, path):
        def _warrp(handler):
            cls.ROUTETABLE[path] = handler
            # return的必须还是传入的函数；否则会出问题
            return handler
        return _warrp

@Route.register('/') # indexhandler = Route.register('/')(indexhandler)
def indexhandler(request:Request):
    return '<h1>index hello word</h1>'

@Route.register('/python') # pythonhandler = Route.register('/python')(pythonhandler)
def pythonhandler(request:Request):
    return '<h1>python hello word</h1>'


class APP:
    _ROUTE = Route

    @wsgify
    def __call__(self, request:Request):
        try:
            return self._ROUTE.ROUTETABLE[request.path](request)
        except:
            raise HTTPNotFound('<h1>ERROR PAGE</h1>')

if __name__ == '__main__':
    webserver = make_server('127.0.0.1', 8080, APP)
    webserver.serve_forever()

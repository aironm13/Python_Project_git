from webob import Request, Response
from webob.exc import HTTPNotFound
from webob.dec import wsgify
from wsgiref.simple_server import make_server


# Version 1
# 使用Router类的实例进行注册
class Router:
    ROUTETABLE = {}
    def regeister(self, path, handler):
        self.ROUTETABLE[path] = handler


def indexhandler(request:Request):
    return '<h1>Index hello word</h1>'

def pythonhandler(request:Request):
    return '<h1>python hello word</h1>'


route = Router()
route.regeister('/', indexhandler)
route.regeister('/python', pythonhandler)

class APP:
    _Route = Router

    @wsgify
    def __call__(self, request:Request):
        try:
            return self._Route.ROUTETABLE[request.path](request)
        except:
            raise HTTPNotFound('<h1>error page</h1>')

if __name__ == '__main__':
    webserver = make_server('127.0.0.1', 8080, APP())
    webserver.serve_forever()




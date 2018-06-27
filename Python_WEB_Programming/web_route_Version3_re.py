from webob.exc import HTTPNotFound
from webob.dec import wsgify
from webob import Request, Response
from wsgiref.simple_server import make_server
import re

class Router:
    ROUTERTABLE = []
    @classmethod
    # pattern：匹配模式
    def register(cls, pattern):
        def _wrapper(handler):
            cls.ROUTERTABLE.append((re.compile(pattern), handler))
            return handler
        return _wrapper

# 带参装饰器；参数是pattern
@Router.register(r'^/$') # indexhandler = Router.register(r'^/$')(indexhandler)
def indexhandler(request:Request):
    return '<h1>index hello word</h1>'

# 带参装饰器；参数是pattern
@Router.register(r'/(python)/(?P<id>\d+)') # pythonhandler = Router.register(r'/(python)/(?P<id>\d+)')(pythonhandler)
def pythonhandler(request:Request):
    return '<h1>python hello word</h1>'


class APP:
    _ROUTE = Router

    @wsgify
    def __call__(self, request:Request):
        for pattern, handler in self._ROUTE.ROUTERTABLE:
            # pattern是编译后匹配模式。使用match从head开始锚定
            if pattern.match(request.path):
                return handler(request)
        raise HTTPNotFound('<h1>ERROR PAGE</h1>')

if __name__ == '__main__':
    webserver = make_server('127.0.0.1', 8080, APP())
    webserver.serve_forever()
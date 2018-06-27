from webob import Request, Response
from webob.exc import HTTPNotFound
from webob.dec import wsgify
from wsgiref.simple_server import make_server
import re


class Route:
    ROUTETABLE = []

    @classmethod
    # 在带参装饰器中加入一个参数method
    def register(cls, method, pattern):
        def _wrapper(handler):
            cls.ROUTETABLE.append((method.upper(), re.compile(pattern), handler))
            return handler
        return _wrapper

@Route.register("GET", r'^/$') # indexhandler = Route.register("GET", r'^/$')(indexhandler)
def indexhandler(request:Request):
    return '<h1>index hello word</h1>'

@Route.register("GET", r'/python/(?P<id>\d+)') # pythonhandler = Route.register("GET", r'/python/(?P<id>\d+)')(pythonhandler)
def pythonhandler(request:Request):
    # 输出分组信息
    print(request.groups)
    return '<h1>python hello word</h1>'


class APP:
    _Route = Route

    @wsgify
    def __call__(self, request:Request):
        for method, pattern, handler in self._Route.ROUTETABLE:
            # 判断方法是否相等必须使用continue；因为路由类中注册了多条路由，如果使用break或return；则把其他注册的路由也跳过，这样使不合理的
            if request.method != method:
                continue
            matcher = pattern.match(request.path)
            if matcher:
                request.groups = matcher.groups()
                request.groupdict = matcher.groupdict()
                return handler(request)
        raise HTTPNotFound('<h1>ERROR PAGE</h1>')

if __name__ == '__main__':
    webserver = make_server('127.0.0.1', 8080, APP())
    webserver.serve_forever()

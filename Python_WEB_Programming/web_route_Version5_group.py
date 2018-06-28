from webob import Request, Response
from webob.dec import wsgify
from wsgiref.simple_server import make_server
from webob.exc import HTTPNotFound
import re


class Router:
    def __init__(self, prefix=''):
        self.__prefix = prefix.rstrip('/\\')
        self.__routetable = []

    def route(self, pattern, *methods):
        def wrapper(handler):
            self.__routetable.append((tuple(map(lambda obj: obj.upper(), methods)),
                                     re.compile(pattern),
                                      handler))
            return handler
        return wrapper

    def get(self, pattern):
        return self.route(pattern, "GET")

    def post(self, pattern):
        return self.route(pattern, "POST")

    def head(self, pattern):
        return self.route(pattern, "HEAD")

    # 6，match方法用来处理分组和路径匹配等问题
    def match(self, request:Request):
        # 如果请求开头没有匹配成功；则return一个None
        if not request.path.startswith(self.__prefix):
            return None
        # 7，头部匹配成功，则进入path处理
        for methods, pattern, handler in self.__routetable:
            if not methods or request.method in methods:
                matcher = pattern.match(request.path.replace(self.__prefix, '', 1))
                if matcher:
                    request.groups = matcher.groups()
                    request.groupdict = matcher.groupdict()
                    # 最后调用handler处理函数，传入request，进行处理
                    return handler(request)

class APP:
    _ROUTES = []

    @classmethod
    # routers是多个Router类实例化的对象
    def register(cls, *routers):
        # 迭代routers，并添加到_ROUTES列表中
        for route in routers:
            cls._ROUTES.append(route)

    @wsgify
    def __call__(self, request:Request):
        # 有一个请求进来，迭代_ROUTES中注册的Router对象
        for route in self._ROUTES:
            # 调用每个Router对象的match方法
            resp = route.match(request)
            if resp:
                return resp
        raise HTTPNotFound('<h1>ERROR</h1>')

# 1，创建Router对象,通过对象装饰
idx = Router()
py = Router('/python')

# 2，注册
APP.register(idx,  py)

# 3，装饰handler
@idx.get(r'^/$')
@idx.route(r'^/(?P<id>\d+)$')
def indexhandler(request:Request):
    return '<h1>index hello word</h1>'

# 4，装饰handler
@py.get('^/(\w+)$')
def pythonhandler(request:Request):
    return '<h1>Python hello word</h1>'

if __name__ == '__main__':
    # 5，定义并启动
    webserver = make_server('127.0.0.1', 8080, APP())
    webserver.serve_forever()
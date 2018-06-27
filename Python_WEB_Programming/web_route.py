from webob import Response, Request
from webob.dec import wsgify
from wsgiref.simple_server import make_server
from webob.exc import HTTPNotFound
import re


# 路由：请求方法、url到处理函数的映射
class Router:
    ROUTERTABLE = []

    @classmethod
    def route(cls, pattern, *methods): # 4，
        def _wrapper(handler): # 5，
            # 对ROUTERTABLE添加路由映射信息
            cls.ROUTERTABLE.append((tuple(map(lambda s: s.upper(), methods)),
                                   re.compile(pattern),
                                   handler))
            return handler # 最后返回handler，传入的函数
        return _wrapper

    @classmethod
    def get(cls, pattern): # 2，
        return cls.route(pattern, 'GET') # 3，route(cls, pattern, *methods)(pythonhandler)

# handler处理方法；带参装饰器

@Router.get(r'^/$') # 1， indexhandler = Router.get(r'^/$')(indexhandler)
def indexhandler(request:Request):
    return '<h1>index hello word</h1>'

@Router.get(r'^/(python)/(?P<id>\d+)$') # pythonhandler = Router.get(r'^/(python)/(?P<id>\d+)$')(pythonhandler)
def pythonhandler(request:Request):
    return '<h1>python hello word</h1>'



class APP:
    # Router是一个类
    _Router = Router

    @wsgify
    def __call__(self, request:Request):
        for methods, pattern, handler in self._Router.ROUTERTABLE:
            # 判断方法是否为空或请求方法在注册的方法中
            if not methods or request.method in methods:
                # 正则匹配请求的路径
                matcher = pattern.match(request.path)
                if matcher:
                    # setattr对request对象设置属性
                    request.groups = matcher.groups()
                    request.groupdict = matcher.groupdict()
                    # setattr(request, 'groups', matcher.groups())
                    # setattr(request, 'groupdict', matcher.groupdict())
                    # handler处理方法
                    return handler(request)
        raise HTTPNotFound('<h1>ERROR PAGE</h1>')


if __name__ == '__main__':
    webserver = make_server('127.0.0.1', 8080, APP())
    webserver.serve_forever()

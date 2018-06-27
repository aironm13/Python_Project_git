from webob.exc import HTTPNotFound
from webob import Request, Response
from webob.dec import wsgify
from wsgiref.simple_server import make_server
import re



# 注册路由类
class Route:
    ROUTETABLE = []

    @classmethod
    def register(cls, pattern):
        def _wrapper(handler):
            cls.ROUTETABLE.append((re.compile(pattern), handler))
            return handler
        return _wrapper


@Route.register(r'^/$') # indexhandler = Route.register(r'^/$')(indexhandler)
def indexhandler(request:Request):
    return '<h1>Index hello word</h1>'

@Route.register(r'/python/(?P<id>\d+)') # pythonhandler = Route.register(r'/python/(?P<id>\d+)')
def pythonhandler(request:Request):
    return '<h1>python hello word</h1>'


class APP:
    _Route = Route

    @wsgify
    def __call__(self, request:Request):
        for pattern, handler in self._Route.ROUTETABLE:
            matcher = pattern.match(request.path)
            if matcher:
                # 所有分组组成的元组，包含命名分组
                # 1，动态在对象上添加
                # 2，可以利用传参的方式
                request.groups = matcher.groups()
                request.groupdict = matcher.groupdict()
                # 匹配成功，则交由对应的handler处理程序处理
                return handler(request)
        # 所有都没有匹配则抛出找不到异常
        raise HTTPNotFound('<h1>ERROR PAGE</h1>')

if __name__ == '__main__':
    # APP是个类，__call__方式式实例的调用
    webserver = make_server('127.0.0.1', 8080, APP())
    webserver.serve_forever()
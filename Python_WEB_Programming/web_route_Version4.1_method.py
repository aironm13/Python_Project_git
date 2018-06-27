from wsgiref.simple_server import make_server
from webob.dec import wsgify
from webob.exc import HTTPNotFound
from webob import Request, Response
import re


class Route:
    ROUTETABLE = []

    @classmethod
    def register(cls, pattern, *method):
        def _wrapper(handler):
            cls.ROUTETABLE.append((tuple(map(lambda obj:obj.upper(), method)),
                                   re.compile(pattern),
                                   handler))
            return handler
        return _wrapper

@Route.register(r'^/$', "GET", "POST")
def indexhandler(request:Request):
    return '<h1>index hello word</h1>'

@Route.register(r'/python/(?P<id>\d+)', "GET")
def pythonhandler(request:Request):
    return '<h1>python hello word</h1>'

class APP:
    _Route = Route

    @wsgify
    def __call__(self, request:Request):
        for method, pattern, handler in self._Route.ROUTETABLE:
            if request.method not in method:
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
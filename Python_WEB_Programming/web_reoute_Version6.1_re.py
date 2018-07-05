# 需求：增加对捕获数据的类型，使用re.sub()就不行了，重写parse函数
'''

TYPECAST = {
    'str':str,
    'word':str,
    'int':int,
    'float':float,
    'any':str
}


def parse(src:str):
    start = 0
    repl = ''
    types = {}

    matchers = regex.finditer(src)

    for i, matcher in enumerate(matchers):
        name = matcher.group(1)
        t = matcher.group(2)

        types[name] = TYPECAST.get(matcher.group(2), str)

        repl += src[start:matcher.start()] # 拼接分组
        tmp = '/(?P<{}>{}'.format(matcher.group(1),
                                  TYPEPATTERNS.get(matcher.group(2), TYPEPATTERNS['str']))

        repl += tmp # 替换
        start = matcher.end() # 移动指针
    else:
        repl += src[start:] # 拼接分组后的内容

    return repl, types
'''



from webob import Response, Request
from webob.dec import wsgify
from webob.exc import HTTPNotFound
from wsgiref.simple_server import make_server
import re

class AttrDict:
    def __init__(self, dicts:dict):
        self.__dict__.update(dicts if isinstance(dicts, dict) else {})

    def __setattr__(self, key, value):
        raise NotImplementedError

    def __repr__(self):
        return '<AttrDict {}>'.format(self.__dict__)

    def __len__(self):
        return len(self.__dict__)


class Router:
    __regex = re.compile(r'/{([^{}:]+):?([^{}:]*)}')

    TYPEPATTERNS = {
        'str':r'[^/]+',
        'word':r'\w+',
        'int':r'[+-]?\d+',
        'float':r'[+-]?\d+\.\d+',
        'any':r'.+'
    }

    TYPECAST = {
        'str':str,
        'word':str,
        'int':int,
        'float':float,
        'any':str
    }

    def __parse(self, src:str):
        start = 0
        repl = ''
        types = {}
        # 通过编译的__regex正则匹配的finditer方法匹配src，返回一个迭代器
        matchers = self.__regex.finditer(src)
        for i, matcher in enumerate(matchers):
            name = matcher.group(1)
            t = matcher.group(2)

            types[name] = self.TYPECAST.get(matcher.group(2), str)
            repl += src[start:matcher.start()]
            tmp = '/(?P<{}>{})'.format(matcher.group(1),
                                       self.TYPEPATTERNS.get(matcher.group(2), self.TYPEPATTERNS['str']))
            repl += tmp # 替换

            start = matcher.end()
        else:
            repl += src[start:]
        return repl, types

    def __init__(self, prefix:str=''):
        self.__prefix = prefix.rstrip('/\\')
        self.__routetable = []


    def route(self, rule, *methods):
        def wrapper(handler):
            pattern, trans = self.__parse(rule) # 用户输入的规则转换为正则表达式
            self.__routetable.append((tuple(map(lambda x: x.upper(), methods)),
                                      re.compile(pattern),
                                      trans,
                                      handler)) # (方法，预编译对象，类型转换，处理函数)
            return handler
        return wrapper

    def get(self, pattern):
        return self.route(pattern, 'GET')

    def post(self, pattern):
        return self.route(pattern, 'POST')

    def match(self, request:Request):
        if not request.path.startswith(self.__prefix):
            return None

        for methods, pattern, trans, handler in self.__routetable:
            if not methods or request.method.upper() in methods:
                matcher = pattern.match(request.path.replace(self.__prefix, '', 1))
                if matcher:
                    newdict = {}
                    for k, v in matcher.groupdict().items():
                        newdict[k] = trans[k][v]
                    request.vars = AttrDict(newdict)
                    return handler(request)

class APP:
    _ROUTERS = []

    @classmethod
    def register(cls, *routers:Router):
        for router in routers:
            cls._ROUTERS.append(router)

    @wsgify
    def __call__(self, request:Request):
        for router in self._ROUTERS:
            resp  = router.match(request)
            if resp:
                return resp
        raise HTTPNotFound('<h1>Error Page</h1>')


# 创建对象
idx = Router()
py = Router('/python')

# 注册
APP.register(idx, py)

@idx.get(r'^/$')
@idx.get(r'^/{id:int}$')
def indexhandler(request:Request):
    id = ''
    if request.vars:
        id = request.vars.id
    return '<h1>Index hell world {}</h1>'.format(id)

@py.get(r'^/{id}$')
def pythonhandler(request:Request):
    if request.vars:
        print(type(request.vars.id))
    res = Response()
    res.charset = 'utf-8'
    res.body = '<h1>Python hello world</h1>'.encode()
    return res

if __name__ == '__main__':
    webserver = make_server('127.0.0.1', 8080, APP())
    try:
        webserver.serve_forever()
    except KeyboardInterrupt:
        webserver.shutdown()
        webserver.server_close()

from webob import Request, Response
from webob.dec import wsgify
from wsgiref.simple_server import make_server
from webob.exc import  HTTPNotFound
import re

# 传入一个对象，在这个对象的字典中增加属性（key-values）
class AttrDict:
    def __init__(self, dicts:dict):
        # 通过对self的字典增加，使用字典的update方法；
        # 如果直接对传入的对象增加，则会引发最大递归
        self.__dict__.update(dicts if isinstance(dicts, dict) else {})

    def __setattr__(self, key, value):
        raise NotImplementedError

    def __repr__(self):
        return '<AttrDict {}>'.format(self.__dict__)

    def __len__(self):
        return len(self.__dict__)

# 对传入的路径进行正则解析
class Router:
    __regex = re.compile(r'/{([^{}:]+):?([^{}:]*)}')

    TYPEATTERNS = {
        'str':r'[^/]+',
        'word':r'\w+',
        'int':r'[+-]?\d+',
        'float':r'[+-]?\d+\.\d+',
        'any':r'.+'
    }

    def __repl(self, matcher):
        return '/(?P<{}>{})'.format(matcher.group(1),
                                    self.TYPEATTERNS.get(matcher.group(2), self.TYPEATTERNS['str']))

    def __parse(self, src:str):
        return self.__regex.sub(self.__repl, src)

    def __init__(self, prefix:str=''): # prefix缺省是空
        self.__prefix = prefix.rstrip('/\\') # 前缀
        self.__routetable = [] # 存三元组

    # 装饰器
    def route(self, pattern, *methods):
        def wrapper(handler):
            self.__routetable.append((tuple(map(lambda x:x.upper(), methods)),
                                      re.compile(self.__parse(pattern)), # 用户输入规则转换为正则表达式
                                      handler))
            return handler
        return wrapper

    def get(self, pattern):
        return self.route(pattern, 'GET')

    def post(self, pattern):
        return self.route(pattern, 'POST')

    def head(self, pattern):
        return self.route(pattern, 'HEAD')

    def match(self, request:Request):
        # 前缀没有匹配成功，则返回None
        if not request.path.startswith(self.__prefix):
            return None

        for methods, pattern, handler in self.__routetable:
            if not methods or request.method.upper() in methods:
                # 前缀匹配成功，通过replace去掉prefix剩下的才是正则表达式需要匹配的路径
                matcher = pattern.match(request.path.replace(self.__prefix, '', 1))
                if matcher:
                    request.groups = matcher.groups() # 所有分组组成的元组，包含命名分组
                    request.groupdict = AttrDict(matcher.groupdict()) # 命名分组组成的字典被属性化
                    return handler(request)

class APP:
    _ROUTER = [] # 存储所有一级Router对象
    # 注册
    @classmethod
    def register(cls, *routers:Router):
        for router in routers:
            cls._ROUTER.append(router)

    @wsgify
    def __call__(self, request:Request):
        # 遍历_ROUTER，调用Router实例的match方法，判断匹配
        for router in self._ROUTER:
            resp = router.match(request)
            if resp: # 匹配返回非None的Router对象
                return resp
        raise HTTPNotFound('<h1>Error Page</h1>')

# 创建对象
idx = Router()
py = Router('/python')
# 注册
APP.register(idx, py)

@idx.get(r'^/$')
@idx.route(r'^/{id:int}$') # 支持所有方法访问
def indexhandler(request):
    id = ''
    if request.groupdict:
        id = request.groupdict.id
    return '<h1>Index hello world {}</h1>'.format(id)

@py.get(r'^/{id}$')
def pythonhandler(request):
    res = Response()
    res.charset = 'utf-8'
    res.body = '<h1> Welcome to Python</h1>'.encode()
    return res


if __name__ == '__main__':
    webserver = make_server('127.0.0.1', 8080, APP())
    try:
        webserver.serve_forever()
    except KeyboardInterrupt:
        webserver.shutdown()
        webserver.server_close()
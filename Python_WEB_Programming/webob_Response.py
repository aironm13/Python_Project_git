from wsgiref.simple_server import make_server
import webob



# # Response的__call__方法
# def __call__(self, environ, start_response):
#     """
#     WSGI application interface
#     """
#     if self.conditional_response:
#         return self.conditional_response_app(environ, start_response)
#
#     headerlist = self._abs_headerlist(environ)
#
#     start_response(self.status, headerlist)
#     if environ['REQUEST_METHOD'] == 'HEAD':
#         # Special case here...
#         return EmptyResponse(self._app_iter)
#     return self._app_iter



# 1，函数实现APP
# def app(environ, start_response):
#     # 定义响应
#     res = webob.Response() # 对应上面的__call__方法
#     # 状态码
#     print(res.status)
#     # 数值状态码
#     print(res.status_code)
#     # headers是一个对象
#     print(type(res.headers))
#     print(res.headers)
#     # headerlist是一个列表
#     print(res.headerlist)
#     start_response(res.status, res.headerlist)
#     html = '<h1>hello word</h1>'.encode('utf-8')
#     return [html]

# # 2，函数实现，借鉴webob.response
# def app(environ, start_response):
#     # 请求处理
#     request = webob.Request(environ)
#
#     # 响应处理
#     resp = webob.Response() # Response实例化
#     resp.status_code = 200
#     # content_type响应的MIME类型
#     print(resp.content_type)
#     html = '<h1>hello word</h1>'.encode('utf-8')
#     # 在resp实例上，添加一个body主体信息指向自定义的html
#     resp.body = html
#     # start_response交给resp完成，resp并return一个可迭代对象
#     return resp(environ, start_response) # 调用__call__方法，传入environ,start_response两个参数，并return一个可迭代对象

# webob.dec装饰器
from webob.dec import wsgify
# (self, func=None, RequestClass=None, args=(), kwargs=None, middleware_wraps=None)

# 使用函数定义WSGI APP
@wsgify # app = wsgify(app)
def app(request:webob.Request) -> webob.Response:
    resp = webob.Response('<h1>hello word</h1>')
    return resp

# 使用类定义WSGI APP
class App:
    @wsgify
    def __call__(self, req:webob.Request):
        return '<h1>hello word</h1>'

if __name__ == '__main__':
    # 使用类定义；实例是可调用对象，类必须实例传入
    webserver = make_server('127.0.0.1', 8080, App())
    try:
        webserver.serve_forever()
    except KeyboardInterrupt:
        webserver.shutdown()
        webserver.close_request()

# # wsgify装饰器源码
#     1，调用装饰器时，WSGI Server传入的environ，start_response两个参数被req和*args接收！！！！！！！！！！！重点理解这个，不然后面难以理解
#     # __call__(self, req, *args, **kw)这个传参必须理解装饰器的传参原理；！！！！！！
#     def __call__(self, req, *args, **kw):
#         """Call this as a WSGI application or with a request"""
#         # 2，把我们定义的app赋值func变量
#         func = self.func
#         # func不是None；所以不执行
#         if func is None:
#             if args or kw:
#                 raise TypeError(
#                     "Unbound %s can only be called with the function it "
#                     "will wrap" % self.__class__.__name__)
#             # 把webob.Request给func
#             func = req
#             return self.clone(func)
#
#         # 3，req是WSGI Server传入的第一个environ实参被req形参接收，而environ本身就是一个字典；故条件成立
#         if isinstance(req, dict):
#             # -----判断args元组中元素的个数不等于1或有kw参数；则抛出异常
#             if len(args) != 1 or kw:
#                 raise TypeError(
#                     "Calling %r as a WSGI app with the wrong signature" %
#                     self.func)
#             # ！！！！！！！！！！4，把req给environ；相当于把WSGI Server传递的environ赋值给environ
#             environ = req
#             # ！！！！！！！！！！5，把args接收的实参start_response也就是元组中的第一个参数，给start_response
#             start_response = args[0]
#             # 把environ字典交给webob.Request实例化
#             req = self.RequestClass(environ)
#             # ???????????????????
#             req.response = req.ResponseClass()
#             try:
#                 args, kw = self._prepare_args(None, None)
#                 # self.call_func调用我们定义的APP；然后把return的结果给resp
#                 resp = self.call_func(req, *args, **kw)
#             except HTTPException as exc:
#                 resp = exc
#             # 如果resp是None；就把req.ResponseClass()给resp
#             if resp is None:
#                 resp = req.response
#             # 如果resp是文本类型，就调用bytes_，进行encode()编码操作；默认encoding='latin-1'
#             if isinstance(resp, text_type):
#                 resp = bytes_(resp, req.charset)
#             # 如果是bytes，先把resp这个bytes对象给到body，然后把resp定义为req.ResponseClass()给resp；最后把body主体写入resp
#             if isinstance(resp, bytes):
#                 body = resp
#                 resp = req.response
#                 resp.write(body)
#             if resp is not req.response:
#                 resp = req.response.merge_cookies(resp)
#             # 最后调用resp，传入environ，start_response；
#             return resp(environ, start_response)
#         else:
#             args, kw = self._prepare_args(args, kw)
#             return self.call_func(req, *args, **kw)



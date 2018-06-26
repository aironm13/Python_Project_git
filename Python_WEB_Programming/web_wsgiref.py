from wsgiref.simple_server import make_server


# demo_app的源代码
# def demo_app(environ,start_response):
#     from io import StringIO
#     stdout = StringIO()
#     print("Hello world!", file=stdout)
#     print(file=stdout)
#     h = sorted(environ.items())
#     for k,v in h:
#         print(k,'=',repr(v), file=stdout)
#     # start_response在return之前执行；返回的是Response的Header信息，即响应的头部信息
#     start_response("200 OK", [('Content-Type','text/plain; charset=utf-8')])
#     # demo_app函数return的是Response的主体信息，即客户端请求的资源
#     return [stdout.getvalue().encode("utf-8")]

# make_server(host, port, app, server_class=WSGIServer, handler_class=WSGIRequestHandler)
# demo_app：处理Request的函数，可调用
# webserver = make_server('127.0.0.1', 8080, demo_app) # WSGI Server调用demo_app传入environ，start_response
# webserver.serve_forever() # 启动


# # 1，函数实现
# def app(environ, start_response):
#     return [res_str]
#
#
# # 2，类实现
# class app:
#     def __init__(self, environ, start_response):
#         pass
#
#     def __iter__(self):
#         yield res_str
#
# # 3，类实现，通过调用实例的__call__方法实现;app()
# class app:
#     def __call__(self, environ, start_response):
#         return [res_str]


from wsgiref.simple_server import make_server
from cgi import parse_qs
from urllib import parse

def app(environ, start_response):
    # 1，解析查询字符串
    # qstr = environ.get('QUERY_STRING')
    # print(qstr)
    # if qstr:
    #     querydict = {k:v for k, _, v in map(lambda item: item.partition('='), qstr.split('&'))}
    # print(querydict)

    # 2，使用cgi模块
    # qstr = environ.get('QUERY_STRING')
    # print(qstr)
    # print(parse_qs(qstr))

    # 3，使用urllib库
    qstr = environ.get('QUERY_STRING')
    print(qstr)
    print(parse.parse_qs(qstr)) # 字典
    print(parse.parse_qsl(qstr)) # 返回二元组列表

    # environ是一个dict
    # for i in environ.items():
    #     print(i)
    # 定义状态码
    status = '200 ok'
    # 定义头部信息
    headers = [('Content-Type', 'text/html;charset=utf-8')]
    # 返回Response头部信息
    start_response(status, headers)

    # 返回可迭代对象
    html = '<h1>hello word</h1>'.encode('utf-8')
    # 返回可迭代对象，所以把html放到一个列表中
    return [html]

webserver = make_server('127.0.0.1', 8080, app)
webserver.serve_forever()
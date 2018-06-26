from wsgiref.simple_server import make_server
import webob

def app(environ, start_response):
    # webob.Request继承自BaseRequest
    request = webob.Request(environ)
    # 显示请求头部
    print(request.headers)
    # 显示请求方法
    print(request.method)
    # 显示请求资源的路径
    print(request.path)
    # 显示查询字符串
    print(request.query_string)
    # GET方法的所有数据
    print(request.GET)
    # POST方法的所有数据
    print(request.POST)
    # # 所有数据
    # print(request.params)
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



# from webob.request import MultiDict
# s = MultiDict()
# s.add('a', 1)
# print(s)
# # s.add(1, 2) # 抛出异常
# s.add('a', 3)
# print(s)
# # 存在多个值时，使用get返回最近定义的
# print(s.get('a'))
# # 与fetchone、sqlalchemy中的one一样，有且只有一个；否则抛出异常
# print(s.getone('a'))

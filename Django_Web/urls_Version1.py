# 导入url
from django.conf.urls import url
from django.http import HttpResponse, HttpRequest, HttpResponseBadRequest, JsonResponse
import simplejson
from .models import User


# 创建注册视图函数
# Version: 1
def reg(request:HttpRequest):
    # 输出请求的方法
    print(request.POST)
    # 输出请求提交中主体信息，body
    print(request.body)
    # 将body中的信息序列化，转换为Json格式
    payload = simplejson.loads(request.body)

    # 捕获异常
    try:
        # 从payload中拿出email对应的value
        email = payload['email']
        # 在User表对象中使用filter查询字段为email=email，后面的email是变量
        query = User.objects.filter(email=email)
        print('++++', query, '++++', type(query), '++++', query.query)
        # 如果email在数据库中存储，if则为真，return Django提供的异常类
        if query:
            # return之后，后面的代码都不执行
            return HttpResponseBadRequest()

        # 在数据库中未查到，继续下面
        name = payload['name']
        password = payload['password']
        print('++++', name, email, password)

        # 构建User表对象，以便提交数据
        # User表的id是自增，所以不用做处理
        user = User()
        user.email = email
        user.name = name
        user.password = password

        try:
            # 如果在数据库User表中未查找email，则将本次客户端发送的数据提交到数据库中
            user.save()
            # 如果正常，返回本次提交，数据库查询返回的id
            return JsonResponse({'user':user.id})
        # 否则将上次抛出的异常类，继续向外抛出
        except:
            raise
    # 有任何异常，都使用Django定义的异常类实例抛出返回给客户端
    except Exception as e:
        print('++++', e)
        # HttpResponseBadRequest()加了括号，所以返回的是实例，不是类
        return HttpResponseBadRequest()


# 路径映射
urlpatterns = [
    url(r'^reg$', reg)
]
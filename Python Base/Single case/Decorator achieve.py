from functools import wraps


# 装饰器实现
# 传入一个类对象
def singleton(cls):
    # 初始化一个变量instance
    instance = None

    # 使用wraps装饰cls，修正cls的属性
    @wraps(cls)
    # 接收类__init__中定义的形参
    def wrapper(*args, **kwargs):
        # 使用nonlocal 定义闭包；可以在wrapper中使用instance变量
        nonlocal instance
        # 如果不存在这个实例
        if not instance:
            # 实例化一个对象并赋给instance变量
            instance = cls(*args, **kwargs)
        # return；如果存在直接return
        return instance
    return wrapper
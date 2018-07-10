

# 在类中定义装饰器，并将其作用在其他函数或方法上

# 问题刨析：明确使用方式，是作为一个实例方法还是类方法

from functools import wraps

class A:
    def decorator1(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('Decorator 1')

    @classmethod
    def decorator2(cls, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('Decorator 2')
            return func(*args, **kwargs)
        return wrapper

# 使用

a = A()
@a.decorator1
def spam():
    pass


@A.decorator2
def grok():
    pass

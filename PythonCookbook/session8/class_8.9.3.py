

# 描述器实现了大部分Python类特性中的底层魔法，包括@classmethod,@staticmethod,@property
# 甚至__slots__特性

class Integer:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Expected an int')
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]

# 描述器只能在类级别被定义，而不能为每个实例单独定义

# 下面的代码是不正确的

class Point:
    def __init__(self, x, y):
        self.x = Integer('x')
        self.y = Integer('y')
        self.x = x
        self.y = y


# 类装饰器
class Typed:
    def __init__(self, name, expected_type):
        self.name = name
        self.expected_type = expected_type

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError('Expected ' + str(self.expected_type))
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]

# 定义一个带参装饰器
def typeassert(**kwargs): # 接受多个可变关键字参数
    def decorate(cls): # 传入类
        for name, expected_type in kwargs.items():
            setattr(cls, name, Typed(name, expected_type))
        return cls
    return decorate

@typeassert(name=str, shares=int, price=float) # 带参装饰器
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

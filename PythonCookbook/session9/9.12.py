

# 使用装饰器扩充类的功能



# 接收一个类传入
def log_getattribute(cls):
    # 把这个类的getattribute方法定义一个标识符
    orig_getattribute = cls.__getattribute__

    # 传入实例和属性名
    def new_getattribute(self, name):
        print(self)
        print('gettint', name)
        print(cls.__getattribute__)
        # 从__getattribute__找到这个实例的这个属性对应的值
        return orig_getattribute(self, name)

    # 访问属性时，首先查看的就是__getattribute__， 所以调用new_getattribute函数
    cls.__getattribute__ = new_getattribute
    # 最后还要返回传入的这个类
    return cls


@log_getattribute
class A:
    def __init__(self, x):
        self.x = x

    def spam(self):
        pass
a = A(42)
print(a.x)



class LoggedGetattribute:
    def __getattribute__(self, name):
        print('getting', name)
        return super().__getattribute__(name)

class A(LoggedGetattribute):
    def __init__(self, x):
        self.x = x

    def spam(self):
        pass


# 问题：封装类的实例上面的私有数据

# 解决：第一个约定是任何以单下划线开头的名字都是内部实现

class A:
    def __init__(self):
        self._internal = 0
        self.public = 1

    def public_method(self):
        pass

    def _internal_method(self):
        pass
# 下划线开头的约定同样适用模块名和模块级别函数

# 解决：两个下划线
# 两个下划线的属性会重命名，重命名的目的就是继承，这种属性通过继承是无法被覆盖的
class B:
    def __init__(self):
        self.__private = 0

    def __private_method(self):
        pass

    def public_method(self):
        pass
        self.__private_method()

class C(B):
    def __init__(self):
        super().__init__()
        self.__private = 1

    def __private_method(self):
        pass


# 总结：非公共名称以单下划线开头，如果代码会涉及到子类，并且有些内部属性应该在
# 子类中隐藏起来，这时可以考虑使用双下划线
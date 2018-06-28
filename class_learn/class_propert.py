class Property:
    def __init__(self, fget=None, fset=None):
        self.fget = fget
        self.fset = fset


    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.fget(instance)

    def __set__(self, instance, value):
        if self.fset is None:
            raise AttributeError('set attributeerror')
        self.fset(instance, value)

    def settr(self, fset):
        self.fset = fset # 把x赋值给self.fset，后面__set__使用；否则抛出self.fset is None错误。
        return self # settr装饰完之后，必须返回Property(x)这个实例，不然类A中就的x就不是描述器，x就指向了settr装饰的函数


class A:
    def __init__(self, x):
        self.__x = x

    @Property # x = Property(x) # Property(x)类的实例化，作为类A的属性，描述器的特性之一
    def x(self):
        return self.__x

    # 1, x现在是类A的属性指向Property的一个实例对象
    # 2, x = Property(x) # x是实例，能够.settr，证明是实例的方法
    # 3, 所以x.settr , settr是类Property(x)实例的一个方法
    @x.settr # x = settr(x) # settr(x)返回必须还是之前Property(x)这个实例，返回函数就破坏了描述器的原则，类的实例属性必须是另外一个类的实例
    def x(self, value):
        self.__x = value

    def __repr__(self):
        return "{}".format(self.__x)

if __name__ == '__main__':
    p1 = A(3)
    print(p1.x)
    p1.x = 18
    print(p1.x)
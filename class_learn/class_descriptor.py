from functools import partial


class StaticMethod:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):  # owner是类A
        return self.func


class ClassMethod:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):  # owner是类A
        return partial(self.func, owner)  # partial函数返回一个新的函数；才可以调用


class A:
    @StaticMethod  # smeth = StaticMethod(smeth) 最后返回smeth这个方法
    def smeth():
        print('This is smeth')

    @ClassMethod  # cmeth = ClassMethod(cmeth) ；cls为类A，所以使用偏函数固定cls并返回一个新的函数
    def cmeth(cls):
        print('This is Class')


if __name__ == '__main__':
    A.smeth()
    print('--------------')
    A.cmeth()


# 问题：给某个实例attrbute增加除访问与修改之外的其他处理逻辑，如类型检查或合法性验证

# 解决： 自定义某个属性的一种简单方法是将它定义一个property

class Person:
    def __init__(self, first_name):
        self.first_name = first_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    @first_name.deleter
    def first_name(self):
        raise AttributeError("Can't delete attribute")

# 上述代码中的三个方法的名字都必须一样，
# 第一个方法是一个getter函数，使first_name成为一个属性
# 其他两个方法给first_name属性添加了setter和deleter函数，
# 重点：只有在first_name属性被创建后，后面的两个装饰器才能被定义


# Version2：

class Person2:
    def __init__(self, first_name):
        self.set_first_name(first_name)

    def get_first_name(self):
        return self._first_name

    def set_first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    def del_first_name(self):
        raise AttributeError("Can't delete attribute")

    name = property(get_first_name, set_first_name, del_first_name)


# Version2:
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def diameter(self):
        return self.radius ** 2

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius
# 将所有的访问接口形式统一，对半径、直径、周长和面积访问都是通过属性访问

c = Circle(4.0)
print(c.area)
print(c.radius)
print(c.perimeter)
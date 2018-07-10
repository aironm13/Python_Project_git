

# 问题：将一个只读属性定义成一个property，并且只在访问的时候才计算结果，同时一旦被访问，将结果值缓存起来，不用每次都计算

# 解决：定义一个延迟属性的一种高效方法通过使用一种描述器

class Lazyproperty:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, cls):
        print(1, instance)
        if instance is None:
            return self
        value = self.func(instance)
        print(2, self.func.__name__)
        setattr(instance, self.func.__name__, value)
        return value

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @Lazyproperty
    def area(self):
        print('Computing area')
        return math.pi * self.radius ** 2

    @Lazyproperty
    def preimeter(self):
        print('Computing perimeter')
        return 2 * math.pi * self.radius

c = Circle(4.0)
print(c.radius)

print(c.area)
print(c.area)

# 多次计算，print('Computing perimeter')只出现一次
print(c.preimeter)
print(c.preimeter)
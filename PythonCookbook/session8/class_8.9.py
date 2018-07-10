

# 问题：创建一个新的拥有一些额外功能的实例属性类型


# 解决：Version1：使用描述器

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

# 一个描述器就是一个实现了三个核心的属性访问get、set、delete的类
# 重点：这些方法接受一个实例作为输入，之后相应的操作实例底层的字典

# 作为一个描述器，需要将这个描述器的实例作为类属性放到一个类的定义中

class Point:
    x = Integer('x')
    y = Integer('y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(2, 3)
print(p.__dict__)
print(p.x)
p.y = 5
p.x = 2.3 # 抛出错误

# 作为输入，描述器的每一个方法会接受一个操作实例

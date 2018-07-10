
# 改变对象实例的打印或显示输出，让它们更具有可读性

# 解决:Version1 重新定义__str__()和__repr__()方法

class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Pair({0.x!r}, {0.y!r})'.format(self)

    def __str__(self):
        return '({0.x!s}, {0.y!s})'.format(self)

# __repr__()方法返回一个实例的代码表示形式，通常用来重新构造这个实例
# __str__()方法将实例转换为一个字符串，使用str()或print()函数会输出这个字符串
# 如果__str__()没有定义，那么就会使用__repr__()
p = Pair(3, 4)
print(p)
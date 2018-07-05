
# 减少可调用对象的参数个数

# 解决：使用functools.partial()；partial()函数允许给定一个或多个参数设置固定值，减少接下来调用时的参数个数

def spam(a, b, c, d):
    print(a, b, c, d)

from functools import partial

s1 = partial(spam, 1) # a = 1
s1(2, 3, 4)

# partial()固定某些参数并返回一个新的callable对象。
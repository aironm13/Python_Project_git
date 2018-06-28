from functools import partial


def add(x, y):
    return x + y

# 固定x形参
triple = partial(add, 3)
# 只用传入一个参数给y就可以
print(triple(4))

# # Python3.5
# # 源码：使用函数定义
#
# def partial(func, *args, **keywords):
#     def newfunc(*fargs, **fkeywords):  # 新的函数
#         newkeywords = keywords.copy()
#         newkeywords.update(fkeywords)
#         return func(*(args + fargs), **newkeywords)
#
#     newfunc.func = func
#     newfunc.args = args
#     newfunc.keywords = keywords
#     return newfunc  # 返回新的函数
#
#
# # Python3.6
# # 源码：使用类定义
#
# def __call__(*args, **keywords):
#     if not args:
#         raise TypeError("descriptor '__call__' of partial needs an argument")
#
#
# self, *args = args
# newkeywords = self.keywords.copy()
# newkeywords.update(keywords)
# return self.func(*self.args, *args, **newkeywords)
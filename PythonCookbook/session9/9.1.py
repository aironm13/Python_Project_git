#
# # 在函数上添加包装器
#
# import time
# from functools import wraps
#
# def timethis(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(func.__name__, end-start)
#         print(result)
#         return result
#     return wrapper
#
# @timethis
# def countdown(n):
#     while n > 0:
#         n -= 1
#
# countdown(100000)
# # 一个装饰器就是一个函数，接受一个函数作为参数并返回一个新的函数
#
#
# # 内置的装饰器
# class A:
#     @classmethod
#     def method(cls):
#         pass
#
# class B:
#     def method(cls):
#         pass
#
#     method = classmethod(method)
#     # classmethod(function) -> method


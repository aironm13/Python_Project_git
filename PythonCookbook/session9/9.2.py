

# 创建装饰器时保留函数元信息，如名字、文档字符串、注解和参数签名

# 解决：Version1：使用functools库中的wraps装饰器

import time

from functools import wraps
def timethis(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return result
    return wrapper

@timethis
def countdown(n):
    while n > 0:
        n -= 1

print(countdown(10000000))
print(countdown.__name__)
print(countdown.__doc__)
print(countdown.__annotations__)

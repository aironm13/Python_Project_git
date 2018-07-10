


# 定义一个带参装饰器

from functools import wraps
import logging

def logged(level, name=None, message=None):

    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)
        return wrapper
    return decorate


@logged(logging.DEBUG)
def add(x, y):
    return x + y

@logged(logging.CRITICAL, 'example')
def spam():
    print('Sapm!')

# 总结：最外层的函数logged()接受参数并将它们作用在内部的装饰器函数上，
# 内层的函数decorate()接受一个函数作为参数，然后再函数上放置一个装饰器
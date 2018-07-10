
# 带可选参数的装饰器

from functools import wraps, partial
import logging


def logged(func=None, *, level=logging.DEBUG, name=None, message=None):
    if func is None:
        return partial(logged, level=level, name=name, message=message)
    logname = name if name else func.__module__
    log = logging.getLogger(logname)
    logmsg = message if message else func.__name__

    @wraps(func)
    def wrapper(*args, **kwargs):
        log.log(level, logmsg)
        return func(*args, **kwargs)
    return wrapper


@logged
def add(x, y): # add = logged(add)
    return x + y

@logged(level=logging.CRITICAL, name='example')
def spam(): # spam = logged(level=logging.CRITICAL, name='example')(spam)
    print('Spam!')
# 被装饰函数会被当作第一个参数直接传递给logged装饰器，因此logged()中的第一个参数就是被包装函数本身


# 问题：利用装饰器强制函数上的类型检查

from inspect import signature
from functools import wraps


def typeassert(*ty_args, **ty_kwargs):
    def decorate(func):
        if not __debug__:
             return func

        sig = signature(func)
        # 返回一个有序字典
        bound_types = sig.bind_partial(*ty_args, **ty_kwargs).arguments

        @wraps(func)
        def wrapper(*args, **kwargs):
            bound_values = sig.bind(*args, **kwargs)

            # 迭代参数并判断参数类型是否正确
            for name, value in bound_values.arguments.items():
                # 判断形参是否在带参装饰器给定的类型中
                if name in bound_types:
                    # 如果类型不匹配，则抛出类型异常
                    if not isinstance(value, bound_types[name]):
                        raise TypeError('Argument {} must be {}'.format(name, bound_types[name]))
            # 参数类型没有问题，则执行传入的函数
            return func(*args, **kwargs)
        return wrapper
    return decorate

@typeassert(int, z=int)
def spam(x, y, z=42):
    print(x, y, z)

spam(1, 2, 3)
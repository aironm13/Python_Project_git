

# 属性的代理访问


class A:
    def spam(self, x):
        pass

    def foo(self):
        pass

class B1:

    def __init__(self):
        self._a = A()

    def spam(self, x):
        return self._a.spam(x)

    def foo(self):
        return self._a.foo()

    def bar(self):
        pass

# 大量的方法需要代理
class B2:
    def __init__(self):
        self._a = A()

    def bar(self):
        pass

    def __getattr__(self, name):
        return getattr(self._a, name)


# __getattr__方法是在访问 attribute 不存在的时候被调用
b = B2()
b.bar()
b.spam(42)


class Proxy:
    def __init__(self, obj):
        self._obj = obj

    def __getattr__(self, name):
        print('Getattr:', name)
        return getattr(self._obj, name)

    def __setattr__(self, key, value):
        if key.startswith('_'):
            super().__setattr__(key, value)
        else:
            print('setattr:', key, value)
            setattr(self._obj, key, value)

    def __delattr__(self, item):
        if item.startswith('-'):
            super().__delattr__(item)
        else:
            print('delattr:', item)
            delattr(self._obj, item)

class Spam:
    def __init__(self, x):
        self.x = x

    def bar(self, y):
        print('Spam.bar:', self.x, y)
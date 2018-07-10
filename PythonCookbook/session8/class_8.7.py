

# 问题：在子类中调用父类的某个已经被覆盖的方法

# 解决：使用super()函数

class A:
    def spam(self):
        print('A.spam')

class B(A):
    def spam(self):
        print('B.spam')
        super().spam() # 调用父类的方法

# super()函数常见用法在__init__方法中确保父类被正确的初始化

class A:
    def __init__(self):
        self.x = 0

class B(A):
    def __init__(self):
        super().__init__()
        self.y = 1

# super()的另外一个常见用法出现在覆盖Python特殊方法的代码中

class Proxy:
    def __init__(self, obj):
        self._obj = obj

    def __getattr__(self, name):
        return getattr(self._obj, name)

    def __setattr__(self, name, value):
        if name.startswith('_'):
            # 如果是下划线开头，则交给父类的__setattr__处理
            super().__setattr__(name, value)
        else:
            setattr(self._obj, name, value)

# 不使用supper()的问题

class Base:
    def __init__(self):
        print('Base.__init__')

class A(Base):
    def __init__(self):
        Base.__init__(self)
        print('A.__init__')

class B(Base):
    def __init__(self):
        Base.__init__(self)
        print('B.__init__')

class C(A, B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        print('C.__init__')

print(C.__mro__)
c = C()
print(c)
# 问题：Base被调用两次
# 如果使用supper()，则每个__init__方法只会被调用一次
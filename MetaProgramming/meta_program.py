class ModelMeta(type):
    def __new__(cls, name, bases, attrs):
        print(name)
        print(bases)
        print(attrs)
        return super().__new__(cls, name, bases, attrs)

# 类A是普通的继承；
class A(ModelMeta):
    pass
print(type(A)) # A的type还是type

# metaclass表示元类，如果还有继承B的类，那么它的type就是B的元类
class B(metaclass=ModelMeta): # 等价 B = type('B', (), {})
    pass
print(type(B))

# C继承B的元类
class C(B):
    pass
print(type(C))


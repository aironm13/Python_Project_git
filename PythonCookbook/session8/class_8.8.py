

# 扩展定义在父类的property的功能

class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._name = value

    @name.deleter
    def name(self):
        raise AttributeError("Can't delete attribute")


# 下面的类继承Person并扩展了name属性的功能
# SubPerson继承Person类，使用Person类的构造方法
class SubPerson(Person):
    @property
    def name(self):
        print('Getting name')
        return super().name

    @name.setter
    def name(self, value):
        print('Setting name to', value)
        print(isinstance(SubPerson, type))
        print(super(SubPerson, SubPerson))
        # <super: <class 'SubPerson'>, <SubPerson object>>
        super(SubPerson, SubPerson).name.__set__(self, value)

    @name.deleter
    def name(self):
        print('Deleting name')
        super(SubPerson, SubPerson).name.__delete__(self)


# Verson3：如果只是想扩展property的某一个方法，可以像下面这样
'''
class SubPerson(Person):
    @Person.name.getter
    def name(self):
        print('Getting name')
        return super().name

class SubPerson(Person):
    @Person.name.setter
    def name(self, value):
        print('Setting name to', value)
        super(SubPerson, SubPerson).name.__set__(self, value)
'''

# 调用父类的init方法
s = SubPerson('Guido')
print('---------------')
print(1, s)
print(2, s.name)
s.name = 'Larry'

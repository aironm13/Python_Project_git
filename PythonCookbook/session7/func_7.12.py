


# 扩展函数中的某个闭包，允许它能访问和修改函数的内部变量

# 通常来说，闭包的内部变量对于外界来说是完全隐藏的

# 解决：Version1，通过编写访问函数将其作为函数属性绑定到闭包上

def sample():
    n = 0
    def func():
        print('n=', n)

    def get_n():
        return  n

    def set_n(value):
        nonlocal n
        n = value

    # 把函数的属性给到func
    func.get_n = get_n
    func.set_n = set_n
    return func

f = sample()
print(f())
print(f.set_n(10))
print(f())
f.get_n()


import sys
class ClosureInstance:
    def __init__(self, locals=None):
        if locals is None:
            locals = sys._getframe(1).f_locals

        self.__dict__.update((key, value) for key, value in locals.items() if callable(value))

    def __len__(self):
        return self.__dict__['__len__']()

def Stack():
    items = []
    def push(item):
        items.append(item)

    def pop():
        return items.pop()

    def __len__():
        return len(items)

    return ClosureInstance()

s = Stack()
print(s)
s.push(10)
len(s)
s.pop()
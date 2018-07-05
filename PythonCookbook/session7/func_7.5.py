
# 定义有默认参数的函数

# 解决：
def spam(a, b=42):
    return a, b

print(spam(3))



# 如果默认参数是一个可修改的容器如列表、字典、集合，可以使用None作为默认值。
def spam(a, b=None):
    if b is None:
        b = []
    return a, b


# 默认参数的值仅仅在函数定义的时候赋值一次
x = 42
def spam(a, b=x):
    return a, b
print(spam(1))
x = 23
print(spam(1))


# 默认参数的值应该是不可变的对象，如None、True、False

def spam(a, b=[]):
    print(b)
    return b
x = spam(1)
print(x)
x.append(99)
x.append('Yow!')
print(x)
print(spam(1))

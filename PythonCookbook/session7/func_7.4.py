

# 问题：构建一个可以返回多个值的函数

# 解决：函数return一个元组即可

def myfun():
    return 1, 2, 3

print(myfun())

# 当我们调用返回一个元组的函数的时候，通常将结果赋值给多个变量，这就像解包；同时也可以赋值给单个变量，这个变量就是元组本身
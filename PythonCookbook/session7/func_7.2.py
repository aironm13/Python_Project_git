
# 问题：函数的某些参数强制使用关键字参数传递？

# 解决：将强制关键字参数放在某个*参数或单个*后面；keywordonly

def recv(maxsize, *, block):
    pass

print(recv(1024, block=True)) # ok


# 在接受任意多个位置参数的函数中指定关键字参数

def mininum(*values, clip=None):
    # min内建函数取values中最小的
    m = min(values)
    # 如果clip为None，直接return m
    # 如果clip不为None，判断clip是否大于m，大于返回clip，否则返回m
    if clip is not None:
        m = clip if clip > m else m
    return m
print(mininum(1, 5, 2, -5, 10))
print(mininum(1, 5, 2, -5, 10, clip=0))
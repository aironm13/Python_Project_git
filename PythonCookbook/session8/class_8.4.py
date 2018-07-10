

# 创建大量对象时节省内存方法


# 解决通过给类添加__slots__属性极大的减少实例所占的内存

class Date:
    __slots__ = ['year', 'month', 'day']
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

# 重点总结：定义__slots__，Python会为实例使用一种更加紧凑的内部表示，实例通过一个
# 很小的固定大小的数组来构建，而不是为每个实例定义一个字典

# 优点：slots更多的是作为一个内存优化工具
# 缺点：使用slots不能再给实例添加新的属性了


# 问题：给函数参数增加元信息

# 解决：使用参数注解

# Python解释器不会对这些注解添加任何的语义；它们不会被类型检查，运行时跟没有加注解之前的效果也没有任何差距
def add(x:int, y:int) -> int:
    return x + y
print(help(add))

# 函数注解存储在函数的__annotations__属性中
print(add.__annotations__)




nums = [37, 99, 48, 47, 40, 25, 99, 51]
num_list = sorted(nums)

# 二分插入前提：序列必须是有序的！
def insert_int(orderlist, value):
    ret = orderlist[:] # 浅拷贝
    low = 0
    height = len(orderlist)

    while low < height:
        mid = (low + height) // 2 # 取中间值
        if value > ret[mid]:
            low = mid + 1
        else:
            height = mid
    ret.insert(low, value)
    return  ret
print(insert_int(num_list, 100))

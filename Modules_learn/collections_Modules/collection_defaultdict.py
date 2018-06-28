import collections
import string
import random

# 创建一个字典，默认的value一个列表
dicts = collections.defaultdict(list)
# 迭代小写字母表，字母是key，vlaue是1到100的随机数
for i in string.ascii_lowercase:
    dicts[i].append(random.randint(1, 100))

print(dicts)

from collections import OrderedDict
od = OrderedDict(a=1, b=2, c=3)
od[0] = 0
od[1] = 1
od['d'] = 4
print(od)
# OrderedDict([('a', 1), ('b', 2), ('c', 3), (0, 0), (1, 1), ('d', 4)])


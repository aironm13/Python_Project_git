from collections import namedtuple


point = namedtuple('p', 'id name')
p1 = point(1, 'tom')
print(p1)
# p(id=1, name='tom')
print(p1.id)
print(p1.name)

# 构造一个可接受任意数量参数的函数

# 使用*参数：
# rest是由所有其他位置参数组成的元组；然后在代码中把它当成一个序列来进行后续的计算
def avg(first, *rest):
    return (first + sum(rest)) / (1 + len(rest))

print(avg(1, 2))
print(avg(1, 2, 3, 4))


# 使用**开头的参数，可以接受任意数量的关键字参数

import html

def make_element(name, value, **attrs):
    keyvals = [' %s="%s"' % item for item in attrs.items()]
    attr_str = ''.join(keyvals)
    element = '<{name} {attrs}>{value}</{name}>'.format(name=name,
                                                        attrs= attr_str,
                                                        value=html.escape(value))
    return element

print(make_element('item', 'Albatross', size='large', quantity=6))
import logging

FORMAT ='%(name)s %(asctime)s %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)

# 根logger
root = logging.getLogger()
# 设置root的级别为ERROR
root.setLevel(logging.ERROR)
print('root', root.handlers)

# 自定义handler
h0 = logging.StreamHandler()
h0.setLevel(logging.WARNING)
root.addHandler(h0)
print('root', root.handlers)

for i in root.handlers:
    print('root handler = {}, formatter = {}'.format(i, i.formatter))


# 继承

# log1
log1 = logging.getLogger('log1')
log1.setLevel(logging.ERROR)
h1 = logging.FileHandler('/var/log/nginx.log')
h1.setLevel(logging.WARNING)
log1.addHandler(h1)
print('log1', log1.handlers)

# log2
log2 = logging.getLogger('log1.log2')
log2.setLevel(logging.CRITICAL)
h2 = logging.FileHandler('/var/log/nginx.log')
h2.setLevel(logging.WARNING)
log2.addHandler(h2)
print('log2', log2.handlers)

# log3
log3 = logging.getLogger('log1.log2.log3')
log3.setLevel(logging.INFO)
# 输出log3的有效级别
print(log3.getEffectiveLevel())
log3.warning('log3')
print('log3', log3.handlers)
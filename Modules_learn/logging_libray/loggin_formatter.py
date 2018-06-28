import logging


log1 = logging.getLogger('log1')
log1.setLevel(logging.ERROR)
h1 = logging.FileHandler('/var/log/nginx.log')
h1.setLevel(logging.WARNING)
# 没有设置formatter，使用缺省值'%(message)s'
print('log1 formatter', h1.formatter)
log1.addHandler(h1)
print('log1', log1.handlers)


log2 = logging.getLogger('log1.log2')
log2.setLevel(logging.CRITICAL)
h2 = logging.FileHandler('/var/log/nginx.log')
h2.setLevel(logging.WARNING)
print('log2 formatter', h2.formatter)
# 创建Formatter
f2 = logging.Formatter('log2 %(name)s %(asctime)s %(message)s')
# handler添加Formatter
h2.setFormatter(f2)
print('log2 formatter', h2.formatter)
log2.addHandler(h2)
print('log2', log2.handlers)
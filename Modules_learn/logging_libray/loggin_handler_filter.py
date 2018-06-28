import logging


FORMAT = '%(asctime)s Thread info: %(thread)d %(threadName)s %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)


log1 = logging.getLogger('log1')
log1.setLevel(logging.WARNING)

h1 = logging.StreamHandler()
h1.setLevel(logging.INFO)
fmt1 = logging.Formatter('log1-h1 %(message)s')
h1.setFormatter(fmt=fmt1)
log1.addHandler(h1)


# log2
log2 = logging.getLogger('log1.log2')
# 继承父的level，WARNING
print(log2.getEffectiveLevel())
h2 = logging.StreamHandler()
h2.setLevel(logging.INFO)
fmt2 = logging.Formatter('log2-h2 %(message)s')
# 定义过滤器
f2 = logging.Filter('log1')
h2.addFilter(f2)
log2.addFilter(h2)
log2.warning('log2 warning')
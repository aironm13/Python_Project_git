# if handlers is None:
#     filename = kwargs.pop("filename", None)
#     mode = kwargs.pop("filemode", 'a')
#     # 1，如果设置文件名，则为根logger加一个输出到文件的Handler；
#     if filename:
#         h = FileHandler(filename, mode)
#     # 2，如果没有设置文件名，则为根logger加一个StreamHandler，默认输出到sys.stderr
#     else:
#         stream = kwargs.pop("stream", None)
#         h = StreamHandler(stream)
#     handlers = [h]
# # 3，根logger一定会至少有一个handler

import logging

FORMAT = '%(asctime)s %(name)s %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)

# 创建一个新的logger
logger = logging.getLogger('Test')
print(logger.name, type(logger))
logging.info('line1')

# 自定义handler
handler = logging.FileHandler('/tmp/line.log', 'w')
# 添加自定义handler
logger.addHandler(handler)
logger.info('line2')

# 日志流：
FORMAT = '%(asctime)s %(name)s %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)
# 返回根logger
root = logging.getLogger()

# 创建一个新的logg，继承自根logg
log1 = logging.getLogger('log1')
# log1.setLevel(logging.INFO) # 分别测试 # log1自定义level级别；不继承
# log1.setLevel(logging.WARNING) # 分别测试 # log1自定义level级别；不继承
# log1.setLevel(logging.ERROR) # 分别测试 # log1自定义level级别；不继承

# log2实例，如果设置了level，就用它和信息的级别比较，否则；继承最近的祖先的level。
log2 = logging.getLogger('log1.log2')
log2.warning('log2 warning')
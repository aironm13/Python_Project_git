import logging

FORMAT = '%(asctime)-15s\tThread info: %(thread)d %(threadName)s %(message)s'
# 不指定level，默认warning
logging.basicConfig(format=FORMAT)

# 不显示
logging.info('I m info {}'.format(20))

# 显示
logging.warning('Im warning {}'.format(30))

# 显示
logging.error('Im error {}'.format(40))

# 字符串


# format:定义日志格式
# level：定义日志级别
FORMAT = '%(asctime)s\t %(thread)d %(threadName)s %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)

logging.info("I'm {}".format(20))
logging.info("Im %d %s", 20, 'years old')

# 日志级别和字符串扩展
# extra：定义扩展字符串
FORMAT = '%(asctime)s\t %(thread)d %(threadName)s %(message)s %(school)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)

s1 = {'school':'jinshan'}
logging.info('Im info %s %s', 20, 'year old', extra = s1)
logging.warning('Im warning %s %s', 20, 'years old', extra = s1)

# 修改日期格式
# datefmt：指定输出时间格式
FORMAT = '%(asctime)s %(message)s'
logging.basicConfig(format=FORMAT, datefmt='%Y/%m/%d %I:%M:%s')
logging.warning('This event warning logged.')

# 输出到文件，而不是输出到显示器
# filename：指定文件路径和文件名称
# filemode：指定文件打开的方式，a表示追加等
FORMAT = '%(asctime)s %(message)s'
logging.basicConfig(format=FORMAT, filename='/var/log/nginx.log')

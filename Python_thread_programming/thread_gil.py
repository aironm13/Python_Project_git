# import datetime
# import logging
#
#
# FORMAT = "%(asctime)s %(threadName)s %(thread)d %(message)s"
# logging.basicConfig(format=FORMAT, level=logging.INFO)
# start = datetime.datetime.now()
#
# def calc():
#     sum = 0
#     for _ in range(1000000000):
#         sum += 1
#
# if __name__ == '__main__':
#     # 在主线程下依次运行5次calc函数
#     calc()
#     calc()
#     calc()
#     calc()
#     calc()
#     delta = (datetime.datetime.now() - start).total_seconds()
#     logging.info(delta)
#



# 多线程
import threading
import datetime
import logging


FORMAT = "%(asctime)s %(threadName)s %(thread)d %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)
start = datetime.datetime.now()

def calc():
    sum = 0
    for _ in range(1000000000):
        sum += 1

if __name__ == '__main__':
    # 创建一个线程池
    ts = []
    for i in range(1, 6):
        t = threading.Thread(target=calc, name='thread-{}'.format(i))
        t.start()
        ts.append(t)

    # 使用join让5个线程join；必须等待join的线程完成，后面的线程才会执行
    for t in ts:
        t.join()

    delta = (datetime.datetime.now() - start).total_seconds()
    logging.info(delta)
import multiprocessing
import datetime
import logging


FORMAT = "%(asctime)s %(threadName)s %(thread)d %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)
start = datetime.datetime.now()

def calc(num):
    sum = 0
    for _ in range(100000000):
        sum += 1
    logging.info('{}'.format(sum))
    return  sum

if __name__ == '__main__':
    # 实例化一个线程池，有5个线程可供使用
    pools = multiprocessing.Pool(5)
    for i in range(5):
        # 使用异步的方式执行
        pools.apply_async(calc, args=(i,), callback=lambda x:logging.info('{}.in callback'.format(x)))
    # 关闭线程池
    pools.close()
    pools.join()
    delta = (datetime.datetime.now() - start).total_seconds()
    print(delta)
from concurrent import futures
import threading
import time
import logging


FORMAT = "%(asctime)s %(threadName)s %(thread)d %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)


def worker(num):
    logging.info('Begin to worker {}'.format(num))
    time.sleep(5)
    logging.info('Finished {}'.format(num))

if __name__ == '__main__':
    # 创建一个线程池，大小为3
    executor = futures.ThreadPoolExecutor(max_workers=3)
    # 创建一个列表，用于放工作任务
    fs = []
    for i in range(3):
        future = executor.submit(worker, i)
        fs.append(future)

    for i in range(3, 6):
        future = executor.submit(worker, i)
        fs.append(future)

    while True:
        time.sleep(2)
        # 显示当前活动线程
        logging.info(threading.enumerate())

        flag = True
        for f in fs:
            # f.done();Future实例的done，如果函数调用被成功的执行完成或成功的取消，则返回True
            logging.info(f.done())
            flag = flag and f.done()
        print('-'*30)
        if flag:
            # flag为True，则关闭线程池
            executor.shutdown()
            # 在输出当前活动的线程
            logging.info(threading.enumerate())
            break
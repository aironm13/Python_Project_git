from threading import Thread, Lock
import time
import logging


FORMAT = "%(asctime)s %(threadName)s %(thread)d %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)

cpus = []
lock = Lock()


def worker(count=10):
    logging.info('Im working for U.')
    flag = False
    while True:
        # 获取锁；每个线程生产前到append之间只有这个线程能操作；防止线程切换导致多append
        lock.acquire()
        if len(cpus) >= count:
            flag = True
        time.sleep(1)
        if not flag:
            cpus.append(1)
        lock.release()
        if flag:
            break
    logging.info('I finished. cpus={}'.format(len(cpus)))

for _ in range(10):
    Thread(target=worker, args=(100,)).start()
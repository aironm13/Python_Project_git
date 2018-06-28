import threading
from concurrent import futures
import time
import logging


FORMAT = "%(asctime)s %(threadName)s %(thread)d %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)


def worker(num):
    logging.info('Begin to worker {}.'.format(num))
    time.sleep(5)
    logging.info('Finished {}'.format(num))

if __name__ == '__main__':

    proces = futures.ProcessPoolExecutor(max_workers=3)
    ps = []
    for i in range(3):
        future = proces.submit(worker, i)
        ps.append(future)

    for i in range(3, 6):
        future = proces.submit(worker, i)
        ps.append(future)

    while True:
        time.sleep(2)
        flag = True
        for f in ps:
            logging.info(f.done())
            flag = flag and f.done()
        print('--------------stop--------------')
        if flag:
            proces.shutdown()
            break
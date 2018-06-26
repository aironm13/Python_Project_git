from threading import Semaphore
import threading
import time
import logging


FORMAT = "%(asctime)s %(threadName)s %(thread)d %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)

def worker(semp):
    logging.info('in sub thread')
    logging.info(semp.acquire())
    logging.info('sub thread over')

if __name__ == '__main__':
    # 初始化三个信号量
    s = Semaphore(3)
    # 拿走一个
    logging.info(s.acquire())
    print(s._value)
    # 继续拿走一个
    logging.info(s.acquire())
    print(s._value)
    # 再拿走一个
    logging.info(s.acquire())
    print(s._value)
    # 创建一个线程，在线程内部拿走一个；总共3个，拿走4次，直接阻塞
    threading.Thread(target=worker, args=(s,)).start()

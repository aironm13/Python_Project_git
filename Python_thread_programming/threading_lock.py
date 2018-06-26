import threading
from threading import Lock
import time


class Counter:
    def __init__(self):
        self._val = 0
        self.__lock = Lock()

    @property
    def value(self):
        # 使用with上下文进行锁管理
        with self.__lock:
            return self._val

    def inc(self):
        try:
            # 加锁
            self.__lock.acquire()
            self._val += 1
        # 在finally中释放锁
        finally:
            self.__lock.release()

    def dec(self):
        with self.__lock:
            self._val -= 1

def run(c, count=100):
    # 循环count次数
    for _ in range(count):
        for i in range(-50, 50):
            if i < 0:
                c.dec()
            else:
                c.inc()

def main():
    c = Counter()
    c1 = 10
    c2 = 1000

    # 运行10个线程
    for i in range(c1):
        threading.Thread(target=run, args=(c, c2)).start()

    while True:
        time.sleep(1)
        if threading.active_count() == 1:
            print(threading.enumerate())
            print(c.value)
            break

if __name__ == '__main__':
    main()
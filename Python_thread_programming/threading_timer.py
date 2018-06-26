
import threading
import time
import logging


FORMAT = "%(asctime)s %(threadName)s %(thread)d %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)

def worker():
    logging.info('in worker')
    time.sleep(2)

# 创建一个Timer线程；等待5秒执行
timerthread = threading.Timer(5, worker)
timerthread.setName('timerthread')
# 启动线程
timerthread.start()
# 输出当前所有活动的线程
print(threading.enumerate())
# 等待5秒才执行timerthred.cancel()方法，这时线程已经进入到worker内部，所以cancel无效
time.sleep(5)
# cancel方法取消，必须在线程进入执行worker函数之前取消
timerthread.cancel()
time.sleep(1)
print(threading.enumerate())
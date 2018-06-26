import threading
from threading import Barrier
import logging


FORMAT = "%(asctime)s %(threadName)s %(thread)d %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)

def worker(barrier:Barrier):
    logging.info('waiging for {} threads.'.format(barrier.n_waiting))
    try:
        # 等待条件满足，继续执行
        # 当所有线程都运行到barrier.wait()，当条件到达，屏障打开，所有线程停止等待，开始执行！
        barrier_id = barrier.wait()
        logging.info('After barrier {}.'.format(barrier_id))
    except threading.BrokenBarrierError:
        logging.info('Broken Barrier')

if __name__ == '__main__':
    barrier = Barrier(3)
    for i in range(3):
        threading.Thread(target=worker, name='worker-{}'.format(i), args=(barrier,)).start()
    logging.info('=========stop========')
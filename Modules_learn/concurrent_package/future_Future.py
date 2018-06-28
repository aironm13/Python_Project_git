from concurrent import futures

# with futures.ThreadPoolExecutor(max_workers=1) as exector:
#     future = exector.submit(pow, 200, 200)
#     print(future.result())

import threading
import time
import logging


FORMAT = "%(asctime)s %(threadName)s %(thread)d %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)

def worker(num):
    logging.info('Begin to worker {}'.format(num))
    time.sleep(5)
    logging.info('Finished {}.'.format(num))
    return num + 100

if __name__ == '__main__':
    with futures.ProcessPoolExecutor(max_workers=3) as exector:
        fs = []
        for i in range(3):
            # 执行函数worker，取进程池中的进程来执行
            future = exector.submit(worker, i)
            fs.append(future)

        for i in range(3, 6):
            # 执行函数worker，取进程池中的进程来执行
            future = exector.submit(worker, i)
            fs.append(future)

        while True:
            time.sleep(2)
            logging.info(threading.enumerate())

            flag = True
            for f in fs:
                logging.info(f.done())
                # done()：如果调用被成功的取消或者执行完成，返回True
                falg = flag and f.done()
                if f.done:
                    # result(timeout=None)：取返回的结果，timeout为None，一致等待返回；
                    logging.info('Result = {}.'.format(f.result()))
            print('-'*30)
            if flag: break
    logging.info('+++++++++end++++++++')
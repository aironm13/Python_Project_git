import multiprocessing
import datetime


def calc(num):
    sum = 0
    for _ in range(10000000):
        sum += 1
    print(num, sum)

if __name__ == '__main__':
    start = datetime.datetime.now()
    pros = []

    for i in range(5):
        # 创建进程对象和线程对象的方法是一样的
        p = multiprocessing.Process(target=calc, args=(i,), name='calc-{}'.format(i))
        pros.append(p)
        p.start()

    for p in pros:
        p.join()

    delta = (datetime.datetime.now() - start).total_seconds()
    print(delta)
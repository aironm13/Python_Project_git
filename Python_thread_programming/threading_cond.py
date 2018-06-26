from threading import Thread, Event, Condition
import random
import logging


FORMAT = "%(asctime)s %(threadName)s %(thread)d %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)


class Dispather:
    def __init__(self):
        self.data = None
        self.event = Event()
        self.cond = Condition()

    def produce(self, total):
        for _ in range(total):
            data = random.randint(0, 100)
            # 使用上下文，开始生产数据
            with self.cond:
                logging.info(data)
                self.data = data
                # 通知所有等待的消费者
                self.cond.notify_all()
            # 使用event.wait让当前线程等待，切换到消费线程
            self.event.wait(1)
        self.event.set()

    def consume(self):
        while not self.event.is_set():
            with self.cond:
                # 等待数据
                self.cond.wait()
                logging.info('receive {}'.format(self.data))
                self.data = None
            # 消费者消费完成，使用wait等待，线程切换到生产者线程
            self.event.wait(0.5)

def main():
    d = Dispather()
    pro = Thread(target=d.produce, args=(10, ), name='produce')
    con = Thread(target=d.consume, name='consume')
    pro.start()
    con.start()

if __name__ == '__main__':
    main()
import socket
import threading
import datetime
import logging


FORMAT = "%(asctime)s %(threadName)s %(thread)d %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)

class TClient:
    # 初始化客户端需要连接的信息
    def __init__(self, sip='127.0.0.1', sport=6666):
        self.sock = socket.socket()
        self.saddr = (sip, sport)
        self.event = threading.Event()

    # start中定义connect方法连接到远端服务器
    def start(self):
        self.sock.connect(self.saddr)
        # 连接成功发送一条消息
        self.sock.send('hello'.encode())
        # 启动一个线程；用来循环接收服务器响应的消息
        threading.Thread(target=self.recv, name='Recv').start()

    def recv(self):
        while not self.event.is_set():
            try:
                data = self.sock.recv(1024)
            except Exception as e:
                logging.error(e)
                break
            msg = "{:%Y/%m/%d %H:%M:%S} {}:{}\n{}\n".format(datetime.datetime.now(), *self.saddr, data.decode().strip())
            logging.info(msg)

    # send方法是客户端向建立连接的sock发送消息
    def send(self, msg):
         data = '{}\n'.format(msg.strip()).encode()
         self.sock.send(data)

    # stop释放socket申请的资源；
    def stop(self):
        self.sock.close()
        self.event.clear()
        logging.info('Client Stop')

def main():
    cc = TClient()
    cc.start()
    # 定义一个循环可以让我们循环发送消息
    while True:
        cmd = input('>>>').strip()
        # 在客户端输入quit，则关闭建立连接的sock并退出
        if cmd == 'quit':
            cc.stop()
            break
        cc.send(cmd) # 调用自定义的send方法，发送消息

if __name__ == '__main__':
    main()


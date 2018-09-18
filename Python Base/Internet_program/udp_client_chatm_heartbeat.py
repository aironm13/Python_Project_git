import socket
import threading
import datetime
import logging


FORMAT = "%(asctime)s %(threadName)s %(thread)d %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)


class ChatClientHb:
    def __init__(self, ip='127.0.0.1', port=6666, interval=10):
        self.addr = (ip, port)
        self.sock =socket.socket(type=socket.SOCK_DGRAM)
        self.clients = {}
        self.event = threading.Event()
        self.interval = interval

    def start(self):
        self.sock.bind(self.addr)
        threading.Thread(target=self.recv, name='recv').start()

    def recv(self):
        while not self.event.is_set():
            localset = set()
            data, raddr = self.sock.recvfrom(1024)
            current = datetime.datetime.now().timestamp()

            # 约定心跳b'^_^'；如果有心跳则把远端加入到客户端字典中
            if data.strip() == b'^_^':
                print('^_^', raddr)
                self.clients[raddr] = current
                continue
            # 如果是quit，则pop弹出这个客户端连接
            elif data.strip() == b'quit':
                self.clients.pop(raddr, None)
                logging.info('{} leaving'.format(raddr))
                continue
            # 如果是普通消息，则添加这个客户端；current是时间戳
            self.clients[raddr] = current

            # 发送消息；把接收的data消息封装一下
            msg = '{} from {}:{}'.format(data.decode(), *raddr)
            logging.info(msg)
            msg = msg.encode()
            # 从clients中迭代，判断时间戳和interval，如果超时就添加到localset中；否则就发送
            # 重点：字典在迭代中是不可删除、增加元素，但是可以修改vlaue
            for c, stamp  in self.clients.items():
                if current - stamp > self.interval:
                    localset.add(c)
                else:
                    self.sock.sendto(msg, c)
            # 迭代已经失效的UDP客户端，在clients中删除
            for c in localset:
                self.clients.pop(c)

    def stop(self):
        for c in self.clients:
            self.sock.sendto(b'bye bye!!', c)
        self.sock.close()


def main():
    cs = ChatClientHb()
    cs.start()

    while True:
        cmd = input('>>>').strip()
        if cmd == 'quit':
            cs.stop()
            break
        logging.info(threading.enumerate())
        logging.info(cs.clients)

if __name__ == '__main__':
    main()
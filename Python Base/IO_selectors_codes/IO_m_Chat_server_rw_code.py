import socket
import threading
import datetime
import selectors
from queue import Queue
import logging


FORMAT = "%(asctime)s %(threadName)s %(thread)d %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)


class ChatServer:
    def __init__(self, ip='127.0.0.1', port=6666):
        self.sock = socket.socket()
        self.addr = (ip, port)
        self.clients = {}
        self.event = threading.Event()
        self.selector = selectors.DefaultSelector()

    def start(self):
        self.sock.bind(self.addr)
        self.sock.listen()
        self.sock.setblocking(False)
        self.selector.register(self.sock, selectors.EVENT_READ, self.accept)
        threading.Thread(target=self.select, name='selector', daemon=True).start()

    def select(self):
        while not self.event.is_set():
            events = self.selector.select() # 返回一个列表；列表中包含多个(key, mask)元组；key是准备就绪的SelectorKey实例。mask是这个文件对象上准备好的事件的位掩码
            print(events)
            for key, mask in events:
                if callable(key.data): # 判断是否可调用accept返回的不可调用；
                    callback = key.data
                    callback(key.fileobj, mask)
                else:
                    callback = key.data[0]
                    callback(key, mask)

    def accept(self, sock, mask):
        conn, raddr = sock.accept() # 阻塞
        conn.setblocking(False) # newsock非阻塞
        self.clients[raddr] = (self.handle, Queue())
        self.selector.register(conn, selectors.EVENT_READ | selectors.EVENT_WRITE, self.clients[raddr]) # 注册newsock并且是非阻塞的

    def handle(self, key, mask): # mask有三种情况：1，2，3
        if mask & selectors.EVENT_READ: # read=1;取mask与read与
            sock = key.fileobj
            raddr = sock.getpeername()
            data = sock.recv(1024)

            if not data or data == b'quit':
                self.selector.unregister(sock)
                sock.close()
                self.clients.pop(raddr)
                return
            msg = '{:%Y/%m/%d %H:%M:%S} {}:{}\n{}\n'.format(datetime.datetime.now(),
                                                            *raddr,
                                                            data.decode())
            logging.info(msg)
            msg = msg.encode()

            for k in self.selector.get_map().values():
                logging.info(k)
                if isinstance(k.data, tuple):
                    k.data[1].put(data)

        if mask & selectors.EVENT_WRITE: # wirte = 2，取mask与write与
            if not key.data[1].empty(): # 如果Queue不是空；就send发送
                key.fileobj.send(key.data[1].get()) # 从Queue中拿出数据发送

    def stop(self):
        self.event.set()
        fobjs = []
        for fd, key in self.selector.get_map().items():
            fobjs.append(key.fileobj)

        for fobj in fobjs:
            self.selector.unregister(fobj)
            fobj.close()
        self.selector.close()

def main():
    cs = ChatServer()
    cs.start()

    while True:
        cmd = input('>>>').strip()
        if cmd == 'quit':
            cs.stop()
            threading.Event.wait(3)
            break

if __name__ == '__main__':
    main()
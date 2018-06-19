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
            events = self.selector.select()

            for key, mask in events:
                if callable(key.data):
                    callback = key.data
                    callback(key.fileobj, mask)
                else:
                    callback = key.data[0]
                    callback(key, mask)
    def accept(self, sock, mask):
        conn, raddr = sock.accept()
        conn.setblocking(False)
        self.clients[raddr] = (self.handle, Queue())
        self.selector.register(conn, selectors.EVENT_READ | selectors.EVENT_WRITE, self.clients[raddr])

    def handle(self, key, mask):
        if mask & selectors.EVENT_READ:
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

        if mask & selectors.EVENT_WRITE:
            if not key.data[1].empty():
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
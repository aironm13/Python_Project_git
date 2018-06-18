import socket
import threading
import datetime
import selectors
import logging


FORMAT = "%(asctime)s %(threadName)s %(thread)d %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)


class ChatServer:
    def __init__(self, ip='127.0.0.1', port=6666):
        self.sock = socket.socket()
        self.addr = (ip, port)
        self.event = threading.Event()
        self.selector = selectors.DefaultSelector() # 创建selector

    def start(self):
        self.sock.bind(self.addr)
        self.sock.listen()
        self.sock.setblocking(False) # 非阻塞
        self.selector.register(self.sock, selectors.EVENT_READ, self.accept) # 注册
        threading.Thread(target=self.select, name='selector', daemon=True).start()

    def select(self): # 阻塞
        while not self.event.is_set():
            events = self.selector.select() # 监视所有注册的事件
            for key, mask in events:
                logging.info(key)
                logging.info(mask)
                callback = key.data
                callback(key.fileobj)

    def accept(self, sock:socket.socket):
        conn, raddr = sock.accept() # 阻塞
        conn.setblocking(False) # newsock非阻塞
        self.selector.register(conn, selectors.EVENT_READ, self.recv) # 注册newsock

    # recv 接收客户端数据
    def recv(self, sock:socket.socket):
        data = sock.recv(1024) # 阻塞接收
        if not data: # if data == b'':
            self.selector.unregister(sock)
            sock.close()
            return # 中断
        msg = "{:%Y/%m/%d %H:%M:%S} {}:{}\n{}\n".format(datetime.datetime.now(),
                                                        *sock.getpeername(),
                                                        data.decode())
        logging.info(msg)
        msg = msg.encode()

        # 群发
        for key in self.selector.get_map().values():
            # 每个newsock连接都是调用recv方法，所以注册中sock对象的value都是同一个recv对象。
            if key.data == self.recv: # 排除accept对象
                key.fileobj.send(msg)

    def stop(self):
        self.event.clear()
        fojbs = []
        for fd, key in self.selector.get_map().items():
            fojbs.append(key.fileobj)
        for fobj in fojbs:
            self.selector.unregister(fojb)
            fobj.close()
        self.selector.close()

def main():
    cs = ChatServer()
    cs.start()
    while True:
        cmd = input('>>>').strip()
        if cmd == 'quit':
            cs.stop()
            threading.Event.wait(3) # 等待3秒
            break
        logging.info(threading.enumerate())

if __name__ == '__main__':
    main()



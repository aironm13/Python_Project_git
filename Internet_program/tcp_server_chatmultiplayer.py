import socket
import threading
import logging


FORMAT = "%(asctime)s %(threadName)s %(thread)d %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)

class TServer:
    # init中初始化一些常用的变量
    def __init__(self, ip='127.0.0.1', port=6666):
        self.sock = socket.socket()
        self.addr = (ip, port)
        self.clients = {}
        self.event = threading.Event()

    # start用于启动一个线程，阻塞accept；等待多个客户端建立连接
    def start(self):
        self.sock.bind(self.addr)
        self.sock.listen()
        threading.Thread(target=self.accept, name='Accept').start()

    # accept方法是一个循环；可以一直接收客户端连接
    def accept(self):
        while not self.event.is_set():
            newsock, raddr = self.sock.accept() # 阻塞；等待客户端连接并返回新建立的sock对象
            self.clients[raddr] = newsock # 把新建立的sock放到一个字典中；用于群发消息
            # 创建一个线程，维护每个建立连接的sock
            threading.Thread(target=self.recv, args=(newsock, raddr), name='Recv').start()

    # recv方法用来接收和发送客户端的消息
    def recv(self, sock:socket, rip):
        while  not self.event.is_set():
            data = sock.recv(1024) # recv默认是阻塞的
            logging.info('{}{}'.format(rip, data.decode()))
            # 迭代self.clients中所有建立连接的sock；并向它们发送消息
            for socks in self.clients.values():
                socks.send('ACK {}'.format(data.decode()).encode())

    # stop方法用来释放sock资源
    def stop(self):
        for sock in self.clients.values():
            sock.close()
        self.sock.close()
        self.event.clear()

def main():
    ts = TServer()
    ts.start()
    # while循环中用来显示当前的启动了多少活动的线程
    while True:
        cmd = input('>>>').strip()
        if cmd == 'quit':
            ts.stop()
            break
        logging.info(threading.enumerate())

if __name__ == '__main__':
    main()

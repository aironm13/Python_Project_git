import selectors
import threading
import socket
import logging


FORMAT = "%(asctime)s %(threadName)s %(thread)d %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)

# 构造缺省性能最优selector
selector = selectors.DefaultSelector()


# 回调函数
def accept(sock, mask): # 需要两个参数
    conn, raddr = sock.accept()
    conn.setblocking(False) # newsock连接非阻塞
    key = selector.register(conn, selectors.EVENT_READ, read) # 注册监听socket
    logging.info(key) # 打印key对象

# 回调函数
def read(conn:socket.socket, mask):
    data = conn.recv(1024) # conn对象recv接收来自客户端的数据
    # if not data or data == b'quit':
    #     conn.close()
    #     return
    msg = "Your msg is {}".format(repr(data))
    conn.send(msg.encode()) # conn连接send发送数据到客户端

# 创建TCP server
sock = socket.socket()
sock.bind(('127.0.0.1', 6666))
sock.listen()
logging.info(sock)
sock.setblocking(False) # sock非阻塞

# 注册文件对象sock关注读事件，返回SelectorKey
key = selector.register(sock, selectors.EVENT_READ, accept) # 注册sock关注读事件
# key的4个对象
# fileobj
# fd
# events
# data
logging.info(key)


event = threading.Event() # event对象
def select(event):
    while not event.is_set():
        events = selector.select() # 开始监视事件是否有触发，返回(key, mask)元组
        print('-'*30)
        for key, mask in events:
            logging.info(key)
            logging.info(mask)
            callback = key.data # 回调函数
            callback(key.fileobj, mask) # 函数调用

def main():
    while not event.is_set():
        cmd = input('>>>')
        if cmd.strip() == 'quit':
            event.clear()
            fobjs = []
            logging.info('{}'.format(list(selector.get_map().items())))

            for fd, key in selector.get_map().items(): # 返回注册项
                print(fd, key)
                print(key.fileobj)
                fobjs.append(key.fileobj)

            for fobj in fobjs:
                selector.unregister(fobj) # 取消注册
                fobj.close()
            selector.close()

if __name__ == '__main__':
    threading.Thread(target=select, args=(event,), name='selector').start()
    main()
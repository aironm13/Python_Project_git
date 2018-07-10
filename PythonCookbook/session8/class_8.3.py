
# 对象支持上下文管理协议(with语句)

# 一个对象兼容with语句，需要实现__enter__()和__exit__()方法

# Version1：

from socket import socket, AF_INET, SOCK_STREAM

class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.sock = None

    def __enter__(self):
        if self.sock is not None:
            raise RuntimeError('Already connected')
        self.sock = socket(self.family, self.type)
        self.sock.connect(self.address)
        return self.sock

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.sock.close()
        self.sock = None

# 上面的类表示了一个网络连接，但是初始化的时候并没有做任何事情(没有建立一个连接)
# 连接的建立和关闭使用with语句自动完成

from functools import partial
conn = LazyConnection(('www.python.org', 80))
with conn as s:
    s.send(b'GET /index.html HTTP/1.0\r\n')
    s.send(b'Host: www.python.org\r\n')
    s.send(b'\r\n')
    resp = b''.join(iter(partial(s.recv, 8192), b''))

# 总结：编写上下文管理器的主要原理是你的代码会放到with语句块中执行
# 当出现with语句的时候，对象的__enter__()方法被触发，它返回的值会被赋值给as声明的变量
# 然后，with语句块里面的代码开始执行，最后，__exit__()方法被触发进行清理工作



# Versino2：允许多个连接

from socket import socket, AF_INET, SOCK_STREAM

class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.connections = []

    def __enter__(self):
        sock = socket(self.family, self.type)
        sock.connect(self.address)
        self.connections.append(sock)
        return sock

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connections.pop().close()

from functools import partial
conn = LazyConnection(('www.python.org', 80))
with conn as s1:
    pass
    with conn as s2:
        pass
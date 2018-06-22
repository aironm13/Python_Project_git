import socket

# 创建一个socket对象
tserver = socket.socket()
# 对tserver对象绑定IP和端口
tserver.bind(('127.0.0.1', 6666))
# 启动监听
tserver.listen()

# 阻塞等待客户端连接，并返回新的socket给s1
s1, info = tserver.accept()

# 循环接收s1连接发送的消息
while True:
    # 阻塞；等待客户端发送数据；recv必须给定大小
    data = s1.recv(1024)
    # socket发送的是字节，即bytes对象；所以需要解码
    # decode()需要注意客户端和服务器端的编码；否则会出现解码失败
    print(data.decode())
    # send发送的必须是字节，需要编码
    # 如果send中文，则需要指定编码，否则因为操作系统原因会出现异常
    s1.send('Ack {}'.format(data.decode()).encode())
# 因为上面的while是死循环；所以永远不会执行close
tserver.close()
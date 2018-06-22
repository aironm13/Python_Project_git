import socket

# 创建一个UDP的socket对象
udpclient = socket.socket(socket.SOCK_DGRAM)
# 指定远端服务器的IP和端口
raddr = ('127.0.0.1', 6666)

while True:
    # 向远端服务器发送消息
    udpclient.sendto('hello word'.encode(), raddr)
    # 接收消息；recvfrom返回消息和远端地址信息
    data1, raddr = udpclient.recvfrom(1024)
    print(data1, raddr)
    # 接收消息
    data2 = udpclient.recv(1024)
    print(data2)
udpclient.close()
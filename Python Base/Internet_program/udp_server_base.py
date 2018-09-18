import socket


# 定义socket类型为UDP
udpserver = socket.socket(type=socket.SOCK_DGRAM)
ipaddr = ('127.0.0.1', 6666)
# 绑定IP和端口
udpserver.bind(ipaddr)

# 接收数据；UDP是无连接的所以不需要accept；只要有数据往socket绑定的端口上发送
data1 = udpserver.recv(1024)
print(data1)
# 通过recvfrom返回远程主机的IP和端口信息
data2, raddr = udpserver.recvfrom(1024)
print(data2)

# 通过sendto发送消息到raddr
udpserver.sendto('Ack {}'.format(data2.decode()).encode(), raddr)
udpserver.close()
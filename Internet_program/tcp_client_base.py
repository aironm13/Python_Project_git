import socket

# 创建一个TCP的socket对象
clienttcp = socket.socket()
# 服务器端的IP和端口
serveraddr = ('127.0.0.1', 6666)
# 使用connect连接到远端服务器提供的IP和端口
clienttcp.connect(serveraddr)
# 客户端向服务器端发送一条消息；注意socket使用TCP传输的是字节流，字符需要编码
clienttcp.send("I'm client".encode())

while True:
    # 接收服务器端发送的消息
    data = clienttcp.recv(1024)
    print(data.decode())
# close永远不会执行
clienttcp.close()

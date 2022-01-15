import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 连接服务器
sock.connect(("localhost", 8080))
# 将消息输出到发送缓冲 send buffer
sock.sendall(b"hello")
# 从接收缓冲 recv buffer 中读响应
print(sock.recv(1024))
# 关闭套接字...
sock.close()

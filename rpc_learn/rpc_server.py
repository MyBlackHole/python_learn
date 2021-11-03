import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("localhost", 8080))
# 监听客户端连接
sock.listen(1)
while True:
    # 接收一个客户端连接
    conn, addr = sock.accept()
    # 从接收缓冲读消息 recv buffer
    print(conn.recv(1024))
    # 将响应发送到发送缓冲 send buffer
    conn.sendall(b"world")
    # 关闭连接
    conn.close()

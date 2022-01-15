import select
import socket


def send_file_2_client(new_client_socket, file_name):
    # 1. 接收客户端 需要下载的文件名
    # 接收客户端发送过来的 要下载的文件名
    print("客户端(%s)需要下载文件是：%s" % (str(new_client_socket), file_name))

    file_content = None

    # 2. 打开这个文件，读取数据
    byt_image = b''
    try:
        with open(file_name, 'rb') as f:
            file_content = f.read()
        len_image = len(file_content)
        status = "status: 1"
        str_image = "len_image: " + str(len_image)
        byt_image = bytes(str_image, 'utf8')
        a = 200 - len(byt_image)
        byt_image = byt_image + b' ' * a
    except Exception as ret:
        print("没有要下载的文件(%s)" % file_name)
        print(file_content)
        # file_content = byt_image + file_content
    # 3. 发送文件的数据给客户端
    print(file_content)
    print(len(file_content))
    if file_content:
        new_client_socket.send(byt_image)
        new_client_socket.send(file_content)

    # new_client_socket.close()
    # del new_client_socket


def main():
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # 2. 绑定
    tcp_server_socket.bind(("*", 7890))

    # 3. 变为监听套接字
    tcp_server_socket.listen(128)
    # tcp_server_socket.setblocking(False)  # 将套接字变为非堵塞

    # 创建一个epoll对象
    epl = select.epoll()

    # 将监听套接字对应的fd注册到epoll中
    epl.register(tcp_server_socket.fileno(), select.EPOLLIN)

    fd_event_dict = dict()

    while True:

        fd_event_list = epl.poll()  # 默认会堵塞，直到 os监测到数据到来 通过事件通知方式 告诉这个程序，此时才会解堵塞
        print(fd_event_list)

        # [(fd, event), (套接字对应的文件描述符, 这个文件描述符到底是什么事件 例如 可以调用recv接收等)]
        for fd, event in fd_event_list:
            print(1, event, select.EPOLLIN)
            # 等待新客户端的链接
            if fd == tcp_server_socket.fileno():
                new_socket, client_addr = tcp_server_socket.accept()
                epl.register(new_socket.fileno(), select.EPOLLIN)
                fd_event_dict[new_socket.fileno()] = new_socket
            elif event == select.EPOLLIN:
                # 判断已经链接的客户端是否有数据发送过来
                file_name = fd_event_dict[fd].recv(1024).decode("utf-8")
                if file_name:
                    send_file_2_client(fd_event_dict[fd], file_name)
                else:
                    fd_event_dict[fd].close()
                    epl.unregister(fd)
                    del fd_event_dict[fd]
            else:
                fd_event_dict[fd].close()
                epl.unregister(fd)
                del fd_event_dict[fd]

    # 关闭监听套接字
    tcp_server_socket.close()


if __name__ == "__main__":
    main()

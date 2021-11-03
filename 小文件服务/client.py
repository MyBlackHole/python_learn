import re
import socket


def main():
    # 1. 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. 获取服务器的ip port
    dest_ip = input("请输入下载服务器的ip:")
    dest_port = int(input("请输入下载服务器的port:"))

    # 3. 链接服务器
    tcp_server_socket.connect((dest_ip, dest_port))

    # 4. 获取下载的文件名字
    download_file_name = input("请输入要下载的文件名字：")

    # 5. 将文件名字发送到服务器
    tcp_server_socket.send(download_file_name.encode("utf-8"))
    print("1>>" * 30)
    print(tcp_server_socket)

    recv_data = tcp_server_socket.recv(200)
    print(recv_data)
    print(recv_data.decode('utf-8'))
    ret = re.match(r'len_image: (\d+)', recv_data.decode('utf-8'))
    count = ret.group(1)
    recv_data = tcp_server_socket.recv(int(ret.group(1)))
    while True:
        print(count)
        print(len(recv_data))
        print(type(count))
        print(type(len(recv_data)))
        if count != str(len(recv_data)):
            print(1)
            recv_data += tcp_server_socket.recv(int(ret.group(1)))
        else:
            break
    if recv_data:
        # 7. 保存接收到的数据到一个文件中
        with open("[新]" + download_file_name, "wb") as f:
            f.write(recv_data)

    # 8. 关闭套接字
    tcp_server_socket.close()


if __name__ == "__main__":
    main()

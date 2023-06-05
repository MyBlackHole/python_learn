from time import sleep, time

import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname="192.168.78.212", username="root", password="Atf2022")
stdin, stdout, stderr = ssh.exec_command("ls")
print(stdout.readlines())
print(stdout.channel.recv_exit_status())

chan = ssh._transport.open_session(timeout=10)
# 数据量大堵塞
query = "cd /;ls -lshAR -h"
chan.exec_command(query)

# # 可以读取大数量
# for i in range(10):
#     if chan.recv_ready():
#         data = chan.recv(1024)
#         while data:
#             print(data)
#             data = chan.recv(1024)
#     sleep(1)
if combine_stderr:
    channel.set_combine_stderr(True)

while not chan.recv_exit_status():
    if chan.recv_ready():
        data = chan.recv(1024)
        while data:
            print(data)
            data = chan.recv(1024)

    if chan.recv_stderr_ready():
        error_buff = chan.recv_stderr(1024)
        while error_buff:
            print(error_buff)
            error_buff = chan.recv_stderr(1024)
    exist_status = chan.recv_exit_status()
    if 0 == exist_status:
        break

# # 数据量少,不堵塞
# query = 'cd /;ls -lshA -h'
# chan.exec_command(query)
# while not chan.recv_exit_status():
#     if chan.recv_ready():
#         data = chan.recv(1024)
#         while data:
#             print(data)
#             data = chan.recv(1024)

#     if chan.recv_stderr_ready():
#         error_buff = chan.recv_stderr(1024)
#         while error_buff:
#             print(error_buff)
#             error_buff = chan.recv_stderr(1024)
#     exist_status = chan.recv_exit_status()
#     if 0 == exist_status:
#         break

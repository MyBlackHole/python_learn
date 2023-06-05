#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Black Hole"

import os
from time import sleep

import paramiko


def ssh_func():
    # 连接 ssh
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname="127.0.0.1", username="black", password="1358")
    stdin, stdout, stderr = ssh.exec_command("ls")
    # ssh.keep_this = ssh
    print(stdout.readlines())
    sleep(100)
    stdin, stdout, stderr = ssh.exec_command("ls")
    print(stdout.readlines())


# def sftp_func():
#     ssh = paramiko.SSHClient()
#     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     ssh.connect(hostname="127.0.0.1", username="root", password="root")
#     sftp = paramiko.SFTPClient.from_transport(ssh.get_transport())
#     sftp.put(
#         "/home/black/PycharmProjects/WeiBoProjects/URun-weibo_crawler/test/URun-weibo_crawler.zip",
#         "/root/URun-weibo_crawler.zip",
#     )


if __name__ == "__main__":
    print(os.getpid())
    ssh_func()

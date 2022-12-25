#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

""" 
------------------------------------------------- 
   File Name:   1 
   Description: 
   Author:      Black Hole 
   date:        2021/1/15 

------------------------------------------------- 
   Change Activity: 
                2021/1/15: 
------------------------------------------------- 
"""

__author__ = 'Black Hole'

import paramiko


def ssh_func():
    # 连接 ssh
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname="127.0.0.1", username="root", password="root")
    stdin, stdout, stderr = ssh.exec_command("ls")
    print(stdout.readlines())


def sftp_func():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname="127.0.0.1", username="root", password="root")
    sftp = paramiko.SFTPClient.from_transport(ssh.get_transport())
    sftp.put("/home/black/PycharmProjects/WeiBoProjects/URun-weibo_crawler/test/URun-weibo_crawler.zip",
             "/root/URun-weibo_crawler.zip")


if __name__ == '__main__':
    pass

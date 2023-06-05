#!/usr/bin/python
# -*- coding:utf-8 -*-

import paramiko
import logging

logging.basicConfig(level=logging.DEBUG)

# # black id_rsa
# private_key = paramiko.RSAKey.from_private_key_file(
#     "/home/black/.ssh/id_rsa",
# )

# # root id_rsa
# private_key = paramiko.RSAKey.from_private_key_file(
#     "/home/black/.ssh/root_id_rsa",
# )

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# ssh.connect(hostname="127.0.0.1", port=22, username="root", pkey=private_key)
ssh.connect(
    hostname="127.0.0.1",
    port=1234,
    username="black",
    # pkey=private_key,
    timeout=10000,
)

stdin, stdout, stderr = ssh.exec_command("id")

result = stdout.read()
print(result.decode())
ssh.close()

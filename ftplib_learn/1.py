#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:   1
   Description:
   Author:      Black Hole
   date:        2020/6/18
-------------------------------------------------
   Change Activity:
                2020/6/18:
-------------------------------------------------
"""

__author__ = 'Black Hole'

import ftplib
from pathlib import Path
# '183.131.241.10:21;dc;hfqYMevpaEZGborovbgzS5Jf'
# ftp_info = {
#     'ip': '127.0.0.1',
#     'port': 21,
#     'user': 'ftp',
#     'pwd': '123456'
# }
ftp_info = {
    'ip': '183.131.241.9',
    'port': 21,
    'user': 'dc',
    'pwd': 'hfqYMevpaEZGborovbgzS5Jf'
}


if __name__ == "__main__":
    # l = Path('lingshi').iterdir()


    ftp = ftplib.FTP()
    ftp.set_pasv(False)
    ftp.connect(ftp_info['ip'], ftp_info['port'])
    ftp.login(ftp_info['user'], ftp_info['pwd'])
    # print(ftp.nlst())
    # print(ftp.nlst('/urun_company/weiboxmlnew/20200617'))
    print(ftp.cwd('/urun_company/weiboxmlnew/20200618'))
    # print(ftp.cwd('/bright_network/weiboxmlnew/'))
    # print(ftp.cwd('/bright_network/weiboxmlnew/20200618'))
    # print(ftp.nlst('/bright_network/weiboxmlnew'))
    # print(ftp.nlst())
    # l = ftp.nlst('/bright_network/weiboxmlnew')
    l = ftp.nlst('/urun_company/weiboxmlnew/20200618/')
    print(l)
    # l = ftp.nlst()

    # # 重命名
    # try:
    #     for item in l:
    #         if '.Xml' in item:
    #             ftp.rename(item, item[:-3] + item[-3:].replace('X', 'x'))
    # except Exception as e:
    #     print(f'{e} {item}')

    # # 删除文件
    # for item in l:
    #     if '.Xml' in item:
    #         ftp.delete(item)

    # # 删除文件夹
    # ftp.rmd('/bright_network/weiboxmlnew/20200618')

    # # 下载
    # for item in l:
    #     if '.Xml' in item:
    #         with open('bat/' + str(item), 'wb') as f:
    #             ftp.retrbinary("RETR " + str(item), f.write)

    # # 上传
    # for item in l:
    #     with open(str(item), 'rb') as f:
    #         ftp.storbinary("STOR " + item.name, f)

    # print(ftp.nlst('/bright_network/weiboxmlnew/'))
    print(ftp.nlst('/urun_company/weiboxmlnew/20200618/'))
    ftp.close()

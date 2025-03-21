#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          1
   Description:
   Author:             Black Hole
   date:               2020/8/17
-------------------------------------------------
   Change Activity:    2020/8/17:
-------------------------------------------------
"""

__author__ = "Black Hole"

# # 加载压缩文件，创建ZipFile对象
# # class zipfile.ZipFile(file[, mode[, compression[, allowZip64]]])
# # 参数file表示文件的路径或类文件对象(file-like object)
# # 参数mode指示打开zip文件的模式，默认值为'r'，表示读已经存在的zip文件，也可以为'w'或'a'，
# # 'w'表示新建一个zip文档或覆盖一个已经存在的zip文档，'a'表示将数据附加到一个现存的zip文档中
# # 参数compression表示在写zip文档时使用的压缩方法，它的值可以是zipfile. ZIP_STORED 或zipfile. ZIP_DEFLATED。
# # 如果要操作的zip文件大小超过2G，应该将allowZip64设置为True。
# file_dir = 'D:/text.zip'
# zipFile = zipfile.ZipFile(file_dir)
#
# # 01 ZipFile.infolist() 获取zip文档内所有文件的信息，返回一个zipfile.ZipInfo的列表
# print(zipFile.infolist())
# # 02 ZipFile.namelist() 获取zip文档内所有文件的名称列表
# print(zipFile.namelist())
# # 03 ZipFile.printdir() 将zip文档内的信息打印到控制台上
# print(zipFile.printdir())

# # 解压文件
# zipFile = zipfile.ZipFile(file_dir)
# for file in zipFile.namelist():
#     zipFile.extract(file, 'd:/Work')
# zipFile.close()


# 压缩
import os
import zipfile

z_file = zipfile.ZipFile("text.zip", "w")
z_file.write("baidu_news_163.py")
z_file.write("__init__.py")
z_file.close()

source_dir = "/project/source"  # pwd查看绝对路径替换
zipname = "/project/target/compress_complete.zip"  # pwd查看绝对路径替换

startdir = source_dir  # 要压缩的文件夹路径
file_news = zipname  # 压缩后文件夹的名字
z = zipfile.ZipFile(file_news, "w", zipfile.ZIP_DEFLATED)  # 参数一：文件夹名
for dirpath, dirnames, filenames in os.walk(startdir):
    fpath = dirpath.replace(startdir, "")
    fpath = fpath and fpath + os.sep or ""
    for filename in filenames:
        z.write(os.path.join(dirpath, filename), fpath + filename)
        print("压缩成功")
z.close()

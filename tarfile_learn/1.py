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

__author__ = 'Black Hole'

import os
import tarfile

# 创建压缩包名
tar = tarfile.open("/tmp/tartest.tar.gz.bz2", "w:bz2")
# 创建压缩包
for root, dir, files in os.walk("/tmp/tartest"):
    for file in files:
        fullpath = os.path.join(root, file)
        tar.add(fullpath)
tar.close()


def extract(tar_path, target_path):
    try:
        tar = tarfile.open(tar_path, "r:bz2")
        file_names = tar.getnames()
        for file_name in file_names:
            tar.extract(file_name, target_path)
        tar.close()
    except Exception as e:
        print(f'error:{e}')


if __name__ == "__main__":
    extract('202007130210-gz_opinion.tar.gz.bz2', 'tmp')

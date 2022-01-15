#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          tar.gz.bz2
   Description:
   Author:             Black Hole
   date:               2020/8/12
-------------------------------------------------
   Change Activity:    2020/8/12:
-------------------------------------------------
"""

__author__ = 'Black Hole'

import tarfile
from pathlib import Path
from threading import Thread

from loguru import logger


def extract(tar_path, target_path, mode="r:bz2"):
    try:
        tar = tarfile.open(tar_path, mode=mode)
        file_names = tar.getnames()
        for file_name in file_names:
            tar.extract(file_name, target_path)
        tar.close()
        logger.debug(f'{tar_path} 解压成功')
    except Exception as e:
        logger.info(f'error:{e} tar_path:{tar_path}')


def extract_many(path):
    path = Path(path)
    for item in path.rglob('*.tar.gz.bz2'):
        if item.is_file():
            target_path = Path(path.resolve().__str__() + "_unzip/" + item.name.split('.')[0])
            extract(tar_path=item, target_path=target_path)
            logger.debug(f'{item} 解压成功')
        else:
            logger.info(f'{item} 不是文件')


def th_extract_many(path):
    path = Path(path)
    hs = list(path.rglob('*.tar.gz.bz2'))
    for i in range(0, len(hs), 10):
        th_list = []
        for item in hs[i:i + 10]:
            if item.is_file():
                target_path = Path(path.resolve().__str__() + "_unzip/" + item.name.split('.')[0])
                t = Thread(target=extract, args=(item, target_path))
                t.start()
                th_list.append(t)
            else:
                logger.info(f'{item} 不是文件')

        for t in th_list:
            t.join()


if __name__ == "__main__":
    # extract('202007130210-gz_opinion.tar.gz.bz2', 'tmp')
    th_extract_many(r"C:\Users\BlackHole\Downloads\dump_hzwp_data")

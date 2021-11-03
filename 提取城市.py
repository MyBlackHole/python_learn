#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

""" 
------------------------------------------------- 
   File Name:   提取城市 
   Description: 
   Author:      Black Hole 
   date:        2021/1/5 

------------------------------------------------- 
   Change Activity: 
                2021/1/5: 
------------------------------------------------- 
"""

__author__ = 'Black Hole'

from pathlib import Path

from loguru import logger

from utility.base_file import loads_file, dumps_file

if __name__ == '__main__':
    area_list = loads_file(Path("/home/black/PycharmProjects/python_learn/area.json"))
    key_list = []
    for area in area_list:
        _id = area['id']
        if '04' == _id[:2]:
            key_list.append(area['word'])
            logger.info(f"{area}")
    dumps_file(path=Path("key_list.txt"), data="|".join(key_list))

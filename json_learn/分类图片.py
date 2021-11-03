#!/usr/bin/env python
# -*- coding: utf-8 -*- 

""" 
------------------------------------------------- 
   File Name:   分类图片 
   Description: 
   Author:      Black Hole 
   date:        2021/1/21 

------------------------------------------------- 
   Change Activity: 
                2021/1/21: 
------------------------------------------------- 
"""

__author__ = 'Black Hole'

import shutil
from pathlib import Path

local_path = Path("/home/black/Pictures/BJ_EQ/")
local5_path = Path("/home/black/Pictures/25")
local5_path.mkdir(exist_ok=True, parents=True)
_list = local_path.rglob("*_25.jpg")

for pic in _list:
    shutil.copyfile(str(pic), str(local5_path / pic.name))

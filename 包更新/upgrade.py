#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:       upgrade
   Description:
   Author:          Black Hole
   date:            2020/7/5
-------------------------------------------------
   Change Activity: 2020/7/5:
-------------------------------------------------
"""

__author__ = 'Black Hole'

from subprocess import call

from pip._internal.utils.misc import get_installed_distributions

for dist in get_installed_distributions():
    # 此处使用python3所以是pip3,如果使用python2版本,去掉3
    # Linux下如果不适用sudo会造成权限不够导致安装出错
    # Windows下去掉sudo
    # call(f"pip3 install --upgrade {dist.project_name} -i https://mirrors.163.com/pypi/simple", shell=True)
    call(f"pip3 install --upgrade {dist.project_name} -i https://mirrors.163.com/pypi/simple", shell=True)

# 终端运行
# python3 upgrade.py

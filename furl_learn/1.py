#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:   1
   Description:
   Author:      Black Hole
   date:        2020/5/21
-------------------------------------------------
   Change Activity:
                2020/5/21:
-------------------------------------------------
"""

__author__ = 'Black Hole'

from furl import furl

u = furl('http://www.dggdjt.com/node/128.htmx?a=1')
print(type(u))
# 主机
print(u.host)
# 路径
print(u.path)
# 端口
print(u.port)
# 参数
print(u.args)
# 相对全路径
# print(u.join('/in'))
# url
print(u.url)
# furl 对象详情
print(u.asdict())
# 深拷贝
print(id(u))
print(id(u.copy()))
#
print(u.load('https://www.baidu.com'))
print(u.add({'a': 1}).url)
print(u.set({'a': 2}).url)
print(u.remove({'a': 2}).url)

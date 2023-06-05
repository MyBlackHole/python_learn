#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:   物理地址获取
   Description:
   Author:      Black Hole
   date:        2020/5/26
-------------------------------------------------
   Change Activity:
                2020/5/26:
-------------------------------------------------
"""

__author__ = "Black Hole"

import psutil
import re

str_s = ["以太网", "本地链接"]
snicaddrs = psutil.net_if_addrs()
for key in snicaddrs.keys():
    for s in str_s:
        if s in key:
            print(snicaddrs[key])
            for snicaddr in snicaddrs[key]:
                if snicaddr.family == -1:
                    print(snicaddr.address)

# print(snicaddrs)
# print(
#     re.findall(
#         r"address='([0-9A-F]{2}-[0-9A-F]{2}-[0-9A-F]{2}-[0-9A-F]{2}-[0-9A-F]{2}-[0-9A-F]{2})'",
#         str(snicaddrs),
#     )
# )
print(
    re.search(
        r"address='([0-9A-F]{2}-[0-9A-F]{2}-[0-9A-F]{2}-[0-9A-F]{2}-[0-9A-F]{2}-[0-9A-F]{2})'",
        str(snicaddrs),
    )
)
# print(re.findall(r"(?P<di>[0-9A-F]{2})-(?P)", str(snicaddrs)))
# print(re.findall(r"([0-9A-F]{2})-\1", str(snicaddrs)))

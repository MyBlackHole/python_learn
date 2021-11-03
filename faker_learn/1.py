#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:   1
   Description:
   Author:      Black Hole
   date:        2020/5/22
-------------------------------------------------
   Change Activity:
                2020/5/22:
-------------------------------------------------
"""

__author__ = 'Black Hole'

from faker import Faker

# 地址信息生成
fake = Faker('zh_CN')
print(fake.name())
print(fake.address())
print(fake.city())
# 王娟
# 海南省磊市门头沟韩路R座 894680
# 桂珍县
# fake = Faker()
# print(fake.name())
# print(fake.address())
# print(fake.city())
# # Crystal Jackson
# # Unit 2787 Box 0755
# # DPO AE 63175
# # West Keith

# 地址
# 地名、街道名

print(fake.street_name())
# 县
print(fake.city_suffix())
# 房名
print(fake.street_address())
# 坐标
print(fake.longitude())
# 山名
print(fake.district())

# 汽车
print(fake.license_plate())

print(fake.user_agent())

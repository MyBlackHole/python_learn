#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          导出所有城市与地区
   Description:
   Author:             Black Hole
   date:               2020/8/21
-------------------------------------------------
   Change Activity:    2020/8/21:
-------------------------------------------------
"""

__author__ = 'Black Hole'

import json

import pandas as pd

df = pd.read_csv('中国新冠疫情2020-07-31.csv')

province_dict = {}

for province in df['province']:
    if province_dict.get(province, None):
        continue
    city_list = df[df['province'] == province]['city'].values.tolist()
    if '境外输入' in city_list:
        city_list.remove('境外输入')
    province_dict[province] = city_list

print(province_dict)

with open('province_city.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(province_dict, ensure_ascii=False))

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          2
   Description:
   Author:             Black Hole
   date:               2020/11/17
-------------------------------------------------
   Change Activity:    2020/11/17:
-------------------------------------------------
"""

__author__ = 'Black Hole'

import json

"""
1
"""


def func1():
    with open('城市列表.json', 'r', encoding='utf-8') as f:
        _str = f.read()
    _list_dict = json.loads(_str)
    _list = []
    for _dict in _list_dict:
        _list.append(_dict['provinceName'])
        mallCityList = _dict.get('mallCityList', [])
        for city in mallCityList:
            _list.append(city['cityName'])
            mallAreaList = city.get('mallAreaList', [])
            for area in mallAreaList:
                _list.append(area['areaName'])

    print(_list)
    print(len(_list))
    _list = list(set(_list))
    with open('城市列表.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(_list, ensure_ascii=False))
    print(len(set(_list)))


if __name__ == '__main__':
    func1()

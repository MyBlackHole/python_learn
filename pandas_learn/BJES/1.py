#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
File Name:   1
Description:
Author:      Black Hole
date:        2021/05/14 15:12:54:

-------------------------------------------------
Change Activity:
             2021/05/14 15:12:54:
-------------------------------------------------
"""

# import pandas as pd

# datafrom = pd.read_json('qqqqq.json')

# datafrom.sort_values("brand", inplace=True)

# style = datafrom['style'].str.split(' ', expand=True)

# print(datafrom)

import re
import json


# def is_NF(_str:str):
#     all_list = re.findall(r'\d{4}[版|款]', _str)
#     return all_list, len(all_list)

# def is_T(_str:str):
#     all_list = re.findall(r'\d\.\dT', _str)
#     return all_list, len(all_list)


if __name__ == "__main__":
    # print(is_T("2021款 Sportback 35 TFSI 进取致雅型"))

    with open('qqqqq.json', 'r', encoding='utf-8') as f:
        text = f.read()

    car_dict_list = json.loads(text)

    s = set()

    for car_dict in car_dict_list:
        style = car_dict['style']

        chile_list = style.split(' ')
        for chile in chile_list:
            s.add(chile)
    
    with open('dict.txt', 'w', encoding='utf-8') as f:
        f.write(json.dumps(list(s), ensure_ascii=False))
    #     for chile in chile_list:
    #         if is_NF(chile):
    #             car_dict['NF'] = chile
    #             continue


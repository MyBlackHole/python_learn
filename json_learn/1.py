#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:       1
   Description:
   Author:          Black Hole
   date:            2020/7/4
-------------------------------------------------
   Change Activity: 2020/7/4:
-------------------------------------------------
"""

__author__ = 'Black Hole'

from pathlib import Path

import requests

from utility.base_file import loads_file
from utility.bio_request import bio_get


def dow_img():
    _json = loads_file(Path("/home/black/PycharmProjects/python_learn/pandas_learn/img_3dim.json"))
    dict_list = _json['RECORDS']
    for item in dict_list:
        dir_path = Path(f"/home/black/Pictures/BJ_EQ/{item['color']}")
        dir_path.mkdir(exist_ok=True, parents=True)
        url = f"http://192.168.1.114:38016/{item['img_url']}"
        file_name = f"{item['ser_id']}_{item['index']}.jpg"
        resp = requests.get(url=url)
        with open(str(dir_path / file_name), "wb") as f:
            f.write(resp.content)


if __name__ == '__main__':
    dow_img()

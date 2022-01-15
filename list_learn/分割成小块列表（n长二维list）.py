#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:       分割成小块列表（n长二维list）
   Description:
   Author:          Black Hole
   date:            2020/7/2
-------------------------------------------------
   Change Activity: 2020/7/2:
-------------------------------------------------
"""

__author__ = 'Black Hole'

import numpy as np


# 方法一
def list_of_groups(init_list, list_len):
    """
    init_list为初始化的列表，list_len初始化列表中的几个数据组成一个小列表
    :param init_list:
    :param list_len:
    :return:
    """
    list_of_group = zip(*(iter(init_list),) * list_len)
    end_list = [list(i) for i in list_of_group]
    count = len(init_list) % list_len
    end_list.append(init_list[-count:]) if count != 0 else end_list
    return end_list


if __name__ == '__main__':
    # 方法二
    data = [i for i in range(15)]
    n = 3  # 大列表中几个数据组成一个小列表
    print([data[i:i + n] for i in range(0, len(data), n)])
    # print(list_of_groups(data, 4))

    # # 方法三
    # a = np.array(data)
    # print(a)
    # a.shape = (3, 5)
    # print(a)

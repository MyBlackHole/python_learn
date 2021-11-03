#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          2
   Description:
   Author:             Black Hole
   date:               2020/10/29
-------------------------------------------------
   Change Activity:    2020/10/29:
-------------------------------------------------
"""

__author__ = 'Black Hole'

import hashlib

import requests


def get_md5(text):
    sign = hashlib.md5(text.encode(encoding='UTF-8')).hexdigest()
    return sign


def get_times(url_list: list):
    ret_list = []
    for url in url_list:
        _id = get_md5(url.strip())
        _url = f'http://hd.weibo.yunrunyuqing.com:38015/search/common/weibo/select?token=52337ecd-8238-4825-951a-b98036035bc0&ID={_id}'
        resp = requests.get(_url)
        _json = resp.json()
        results = _json.get('results')
        if results:
            _time = results[0]['Time']
        else:
            _time = 0
        ret_list.append([url.strip(), _time])
    return ret_list


def get_time_blog(blog_list: list):
    ret_list = []
    for blog_id in blog_list:
        _url = f'http://hd.weibo.yunrunyuqing.com:38015/search/common/weibo/select?token=52337ecd-8238-4825-951a-b98036035bc0&BlogID={blog_id}&starttime=20000101&endtiem=20201029'
        resp = requests.get(_url)



if __name__ == '__main__':
    with open('weibo_url.txt', 'r') as f:
        _url_list = f.readlines()
        data_list = get_times(_url_list)

    with open('data.txt', 'w') as f:
        for data in data_list:
            f.write(f"{data[0]} {data[1]}\n")
    # with open('return.txt', 'w') as f:
    #     f.write()

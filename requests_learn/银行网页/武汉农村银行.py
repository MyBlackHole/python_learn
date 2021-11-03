#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:       武汉农村银行
   Description:
   Author:          Black Hole
   date:            2020/7/14
-------------------------------------------------
   Change Activity: 2020/7/14:
-------------------------------------------------
"""

__author__ = 'Black Hole'

import requests

headers = {
    # "Host": "[图片]mp.weixin.qq.com",
    # "Connection": "keep-alive",
    # "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; OPPO R17 Pro Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36 MMWEBID/7166 MicroMessenger/7.0.12.1620(0x27000C34) Process/toolsmp NetType/WIFI Language/zh_CN ABI/arm32",
    # "Accept": "text/回头ml,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    # "x-wechat-key": "3d88e0f333d7b7f7ea66849a80406b049eae7f19f8aeb81b9af8748da738fc4e3c3b12220e39be765643f222e06c53f385a2671077a9ad3337ad4470e64649fd0864e868816615d2aefa3a62183f7da8",
    # "x-wechat-uin": "Mjk2MjQ2NDUyOQ%3D%3D",
    # "Accept-Encoding": "gzip, deflate",
    # "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
}
resp = requests.get(url='http://www.whrcbank.com/zhuzhan/FinancialProduct/index.html', headers=headers)
print(resp.text)

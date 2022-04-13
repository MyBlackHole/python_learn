#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
File Name:   2
Description:
Author:      Black Hole
date:        2021/03/19 16:45:20:

-------------------------------------------------
Change Activity:
             2021/03/19 16:45:20:
-------------------------------------------------
"""

import base64
import json
import os.path
from io import BytesIO

import requests

# Python3 base64官方API：https://docs.python.org/3/library/base64.html

"""
操作字符串
"""
test_str = "hello world!"
# 编码
encode_str = base64.encodebytes(test_str.encode("utf8"))  # b'aGVsbG8gd29ybGQh\n'
print(encode_str.decode())  # 默认以utf8解码，结果 aGVsbG8gd29ybGQh
# 解码
decode_str = base64.decodebytes(encode_str)  # b'hello world!'
print(decode_str.decode())  # 默认以utf8解码，结果 hello world!

"""
操作本地图片
"""
# 编码
with open("D:\\redis.png", "rb") as f:
    encode_img = base64.b64encode(f.read())
    file_ext = os.path.splitext("D:\\redis.png")[1]
    print("data:image/{};base64,{}".format(file_ext[1:], encode_img.decode()))
    f.close()
# 解码
with open("D:\\redis2.png", "wb") as f:
    f.write(base64.b64decode(encode_img))
    f.close()

"""
操作网络图片
"""
# 编码
response = requests.get(
    "https://login.sina.com.cn/cgi/pin.php?r=24365533&s=0&p=gz-7c16232cd167e7a4a5ed764688cda14f06bf"
)
encode_wimg = base64.b64encode(BytesIO(response.content).read())
print("data:image/png;base64,%s" % encode_wimg.decode())
# 解码
with open("D:\\web.png", "wb") as f:
    f.write(base64.b64decode(encode_wimg))
    f.close()

"""
操作字典
"""
test_dict = {"hello": "world", "year": 2019}
# 编码
encode_dict = base64.encodebytes(json.dumps(test_dict, ensure_ascii=False).encode())
print(encode_dict.decode())  # 结果 eyJoZWxsbyI6ICJ3b3JsZCIsICJ5ZWFyIjogMjAxOX0=
# 解码
decode_dict = base64.decodebytes(encode_dict)
print(decode_dict.decode())  # 结果 {"hello": "world", "year": 2019}

"""
操作URL
"""
test_url = "https://docs.python.org/3/library/base64.htm?a=~"
# 编码
encode_url = base64.encodebytes(test_url.encode())  # 普通编码
print(encode_url.decode())  # 结果 eyJoZWxsbyI6ICJ3b3JsZCIsICJ5ZWFyIjogMjAxOX0=

safe_encode_url = base64.urlsafe_b64encode(test_url.encode())  # URL安全编码
print(
    safe_encode_url.decode()
)  # 结果 aHR0cHM6Ly9kb2NzLnB5dGhvbi5vcmcvMy9saWJyYXJ5L2Jhc2U2NC5odG0_YT1-

safe_encode_url = base64.b64encode(
    test_url.encode(), b"-_"
)  # 编码时使用'-' 替换'+' 使用 '_'替换'/' ，效果与前例相同
print(
    safe_encode_url.decode()
)  # 结果 aHR0cHM6Ly9kb2NzLnB5dGhvbi5vcmcvMy9saWJyYXJ5L2Jhc2U2NC5odG0_YT1-

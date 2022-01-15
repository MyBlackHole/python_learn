#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:   1
   Description:
   Author:      Black Hole
   date:        2020/6/19
-------------------------------------------------
   Change Activity:
                2020/6/19:
-------------------------------------------------
"""

__author__ = 'Black Hole'

import base64
import hashlib
import hmac
import time
from urllib import parse

import requests


def din_din(text: str):
    timestamp = round(time.time() * 1000)
    secret = 'SECdfcaacc9f7d4993dd4a94c70707b68aa8d859cdbcf0efd843fcc0f913a3f82ae'
    secret_enc = secret.encode()
    string_to_sign = '{}\n{}'.format(timestamp, secret)
    string_to_sign_enc = string_to_sign.encode()
    hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = parse.quote_plus(base64.b64encode(hmac_code))
    print(timestamp)
    print(sign)
    j = {
        'msgtype': "text",
        'text': {
            "content": text
        }
    }
    url = f"https://oapi.dingtalk.com/robot/send?access_token=014748917f39fdb64e3f47ee05f44b038c115fcb00b2e1281886712ad4b24186&timestamp={timestamp}&sign={sign}"
    resp = requests.post(url=url, json=j)
    print(resp.status_code)
    print(resp.text)


if __name__ == "__main__":
    din_din("我来试试")
    pass

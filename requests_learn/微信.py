#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          微信
   Description:
   Author:             Black Hole
   date:               2020/7/29
-------------------------------------------------
   Change Activity:    2020/7/29:
-------------------------------------------------
"""

__author__ = "Black Hole"

import requests

"""
GET https://mp.weixin.qq.com/s?__biz=MzI1Nzc0MTIwNQ==&mid=2247507371&idx=1&sn=a8ca6a5085e03f83bd4c1e33022b5e96&chksm=ea104551dd67cc47152ccff2f2699342c033bbf2f738fa3a57e1795cf5f5d5c439ae35dd900d&ascene=1&devicetype=android-22&version=27000f34&nettype=WIFI&abtest_cookie=AAACAA%3D%3D&lang=zh_CN&exportkey=AzN%2BKbBRvQxhCW12JTg7I%2BY%3D&pass_ticket=3PUwnjjMYzsedZo%2B%2FIQTOkTRIAK%2BasCRNZMByn4HOCDQ9FpHC4U0JsXucp1oNH%2Fq&wx_header=1 HTTP/1.1
'Host':'mp.weixin.qq.com',
'Connection':'keep-alive',
'Cache-Control':'max-age=0',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Linux; Android 5.1.1; SM-N960F Build/JLS36C; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36 MMWEBID/128 MicroMessenger/7.0.15.1680(0x27000F34) Process/toolsmp WeChat/arm32 NetType/WIFI Language/zh_CN ABI/arm32',
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
'x-wechat-uin':'MTgwMTkwNTE5NA%3D%3D',
'x-wechat-key':'135152bf1bf066a68dd069b7496d980258067fde1f6985df835f369f014c7cdd87503e96dad1aba259054d143e50a5d8f4e132e552de0b6cd0f3eecdc4af2d2fa97c3d54651077810eab373553aa0172',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
'Cookie':'rewardsn=; wxtokenkey=777; wxuin=1801905194; devicetype=android-22; version=27000f34; lang=zh_CN; pass_ticket=3PUwnjjMYzsedZo+/IQTOkTRIAK+asCRNZMByn4HOCDQ9FpHC4U0JsXucp1oNH/q; wap_sid2=CKrIm9sGElxocTh6UmRtQko2NC11b3JFQU95cnN3OWVuVm1Sb3cyRXhrMERfQ1lUOFB1Qm52U1BmZnh0SF9GWjZxaXh4ckUwb2dIeHBtSm02ZDh0aVVXYjd4VzdEREFFQUFBfjCnlYX5BTgNQAE=',
'X-Requested-With':'com.tencent.mm',
If-Modified-Since: Wed, 29 Jul 2020 18:01:13 +0800
"""
if __name__ == "__main__":
    headers = {
        "Host": "mp.weixin.qq.com",
        "Connection": "keep-alive",
        "Cache-Control": "max-age=0",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; SM-N960F Build/JLS36C; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36 MMWEBID/128 MicroMessenger/7.0.15.1680(0x27000F34) Process/toolsmp WeChat/arm32 NetType/WIFI Language/zh_CN ABI/arm32",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "x-wechat-uin": "MTgwMTkwNTE5NA%3D%3D",
        "x-wechat-key": "135152bf1bf066a68dd069b7496d980258067fde1f6985df835f369f014c7cdd87503e96dad1aba259054d143e50a5d8f4e132e552de0b6cd0f3eecdc4af2d2fa97c3d54651077810eab373553aa0172",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "Cookie": "rewardsn=; wxtokenkey=777; wxuin=1801905194; devicetype=android-22; version=27000f34; lang=zh_CN; pass_ticket=3PUwnjjMYzsedZo+/IQTOkTRIAK+asCRNZMByn4HOCDQ9FpHC4U0JsXucp1oNH/q; wap_sid2=CKrIm9sGElxocTh6UmRtQko2NC11b3JFQU95cnN3OWVuVm1Sb3cyRXhrMERfQ1lUOFB1Qm52U1BmZnh0SF9GWjZxaXh4ckUwb2dIeHBtSm02ZDh0aVVXYjd4VzdEREFFQUFBfjCnlYX5BTgNQAE=",
        "X-Requested-With": "com.tencent.mm",
    }
    resp = requests.get(
        url="https://mp.weixin.qq.com/s?__biz=MzI1Nzc0MTIwNQ==&mid=2247507371&idx=1&sn=a8ca6a5085e03f83bd4c1e33022b5e96&chksm=ea104551dd67cc47152ccff2f2699342c033bbf2f738fa3a57e1795cf5f5d5c439ae35dd900d&ascene=1&devicetype=android-22&version=27000f34&nettype=WIFI&abtest_cookie=AAACAA%3D%3D&lang=zh_CN&exportkey=AzN%2BKbBRvQxhCW12JTg7I%2BY%3D&pass_ticket=3PUwnjjMYzsedZo%2B%2FIQTOkTRIAK%2BasCRNZMByn4HOCDQ9FpHC4U0JsXucp1oNH%2Fq&wx_header=1",
        headers=headers,
        verify=False,
    )
    print(resp.text)

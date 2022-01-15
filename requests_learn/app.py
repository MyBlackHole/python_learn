#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          app
   Description:
   Author:             Black Hole
   date:               2020/9/9
-------------------------------------------------
   Change Activity:    2020/9/9:
-------------------------------------------------
"""

__author__ = 'Black Hole'

import requests

url = 'https://aweme-lq.snssdk.com/aweme/v1/aweme/post/?max_cursor=0&sec_user_id=MS4wLjABAAAAG_eAuuWeG2F0apjYw3DFbRUcD99uB3eJ_6WGtTbRcrY&count=20&retry_type=no_retry&iid=1301428203435632&device_id=729724667829326&ac=wifi&channel=wandoujia_aweme2&aid=1128&app_name=aweme&version_code=780&version_name=7.8.0&device_platform=android&ssmix=a&device_type=VOG-AL10&device_brand=huawei&language=zh&os_api=22&os_version=5.1.1&uuid=863064010768234&openudid=8ff3c21e933014ce&manifest_version_code=780&resolution=540*960&dpi=160&update_version_code=7802&_rticket=1599640884795&mcc_mnc=46007&ts=1599640884&app_type=normal&js_sdk_version=1.25.0.1'
"""
https://aweme-lq.snssdk.com/aweme/v1/aweme/post/?max_cursor=0&sec_user_id=MS4wLjABAAAAG_eAuuWeG2F0apjYw3DFbRUcD99uB3eJ_6WGtTbRcrY&count=20&retry_type=no_retry&iid=1301428203435632&device_id=729724667829326&ac=wifi&channel=wandoujia_aweme2&aid=1128&app_name=aweme&version_code=780&version_name=7.8.0&device_platform=android&ssmix=a&device_type=VOG-AL10&device_brand=huawei&language=zh&os_api=22&os_version=5.1.1&uuid=863064010768234&openudid=8ff3c21e933014ce&manifest_version_code=780&resolution=540*960&dpi=160&update_version_code=7802&_rticket=1599640884795&mcc_mnc=46007&ts=1599640884&app_type=normal&js_sdk_version=1.25.0.1
{'cookies': '', 'accept-encoding': 'gzip', 'sdk-version': '1', 'user-agent': 'okhttp/3.10.0.1', 'x-ss-req-ticket': '', 'x-gorgon': '0401002008008de7c19181b06107d840f0342f55a8659f071833', 'x-khronos': '1599640886'}
"""
headers = {'cookies': '', 'accept-encoding': 'gzip', 'sdk-version': '1', 'user-agent': 'okhttp/3.10.0.1',
           'x-ss-req-ticket': '', 'x-gorgon': '0401002008008de7c19181b06107d840f0342f55a8659f071833',
           'x-khronos': '1599640886'}

# response = requests.get(url=url, headers=headers, timeout=30, proxies=get_zdy_proxy())
# response = requests.get(url=url, proxies=get_zdy_proxy())
# url = 'https://google.com'
response = requests.get(url=url, headers=headers)
# response = requests.get(url=url)
print(response.status_code)
print(response.text)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/10/19
# @Author : Twinkle
# @File : rebang.py
# @Version    : 
# @Description:
import base64
import random
import time

import requests


def getCsInfo(city_name, province_name):
    # jsondata = ('{"city_name":"'+city_name+'","submit_time":'+str(int(time.time()))+',"province_name":"'+province_name+'"}').encode()
    jsondata = '{"city_name":"柳州","submit_time":1603096955,"province_name":"广西"}'.encode("utf8")
    bytes_list = []
    for i in range(len(jsondata)):
        if jsondata[i] < 0:
            jsondata[i] = jsondata[i] - 255

        x = jsondata[i] ^ -99
        print(f"{jsondata[i]}-{x}")
        bytes_list.append(x)
    print(b"".join(bytes_list))
    return base64.urlsafe_b64encode(b"".join(bytes_list))


def getDid():
    headers = {
        'Host': 'is-lq.snssdk.com',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'User-Agent': 'com.ss.android.article.news/7501 (Linux; U; Android 5.1.1; zh_CN; VOG-AL10; Build/HUAWEIVOG-AL10; Cronet/TTNetVersion:b97574c0 2019-09-24)',
    }
    did = ''.join(random.choice("0123456789") for i in range(16))
    location_url = f'https://is-lq.snssdk.com/location/suusci/?device_id={did}&ac=wifi&channel=gdt_pr_jrtt_kp4&aid=13&app_name=news_article&version_code=750&version_name=7.5.0&device_platform=android&ab_version=668779%2C660830%2C662176%2C1859936%2C662099%2C668774%2C2001175%2C2020941%2C2067367%2C668775%2C2033166%2C1965361%2C2063713%2C1877264&ab_group=100168&ab_feature=102749%2C94563&ssmix=a&device_type=VOG-AL10&device_brand=Android&language=zh&os_api=22&os_version=5.1.1&manifest_version_code=7501&resolution=540*960&dpi=160&update_version_code=75017&_rticket={str(int(time.time() * 1000))}&plugin=18762&tma_jssdk_version=1.42.1.8&rom_version=22&cdid=9fde137c-59c7-4e80-a43a-ca12dd40532e'
    csinfo = "5r_-9OnkwvP88Pi_p797Ai54KgO_sb_u6P_w9OnC6fTw-L-nrKutrq2kq6SoqLG_7e_y6_Tz_vjC8_zw-L-nv3gkInU4Ir_g"  # 柳州
    data = f'csinfo={csinfo}&device_id={did}&ac=wifi&channel=gdt_pr_jrtt_kp4&aid=13&app_name=news_article&version_code=750&version_name=7.5.0&device_platform=android&ab_version=668779%2C660830%2C662176%2C1859936%2C662099%2C668774%2C2001175%2C2020941%2C2067367%2C668775%2C2033166%2C1965361%2C2063713%2C1877264&ab_group=100168&ab_feature=102749%2C94563&ssmix=a&device_type=VOG-AL10&device_brand=Android&language=zh&os_api=22&os_version=5.1.1&manifest_version_code=7501&resolution=540*960&dpi=160&update_version_code=75017&_rticket=1603097099972&plugin=18762&tma_jssdk_version=1.42.1.8&rom_version=22&cdid=9fde137c-59c7-4e80-a43a-ca12dd40532e'
    requests.post(location_url, headers=headers, data=data)
    # {"err_no":0,"err_msg":"success","err_tip":"success","data":null} 这里表示成功切换到柳州
    return did


def getHot(did):
    headers = {
        'Host': 'i-lq.snssdk.com',
        'accept': 'application/json, text/plain, */*',
        'user-agent': 'com.ss.android.article.news/7501 (Linux; U; Android 5.1.1; zh_CN; VOG-AL10; Build/HUAWEIVOG-AL10; Cronet/TTNetVersion:b97574c0 2019-09-24)',
    }
    url = f'https://i-lq.snssdk.com/toutiao/normandy/local_trending/list/?category=news_hot&business_data=%7B%22entrance%22%3A%22channel%22%2C%22log_pb%22%3A%22%7B%5C%22hot_tab_name%5C%22%3A%5C%2210_top_hot_talks%5C%22%7D%22%7D&local_id=0&device_id={did}&ac=wifi&mac_address=5E%3A01%3A7C%3A3C%3A27%3A43&channel=gdt_pr_jrtt_kp4&aid=13&app_name=news_article&version_code=750&version_name=7.5.0&device_platform=android&ab_version=660830%2C662176%2C1859936%2C662099%2C668774%2C668775%2C2067367%2C1965361%2C2063713%2C2020941%2C2033166%2C2001175%2C668779%2C1877264&ab_group=100168&ab_feature=102749%2C94563&ssmix=a&device_type=VOG-AL10&device_brand=Android&language=zh&os_api=22&os_version=5.1.1&manifest_version_code=7501&resolution=540*960&dpi=160&update_version_code=75017&_rticket={str(int(time.time() * 1000))}&plugin=18762&tma_jssdk_version=1.42.1.8&rom_version=22&cdid=9fde137c-59c7-4e80-a43a-ca12dd40532e'
    response = requests.get(url, headers=headers)
    for item in response.json()["data"]["list"]:
        # it = {
        #     "title": item["title"],
        #     "user_name": item["user_name"],
        #     "create_time": item["create_time"],
        #     "url": f'https://www.toutiao.com/a{item["group_id"]}/' # 可能有问题
        # }
        print(item)


if __name__ == '__main__':
    # did = getDid()
    # getHot(did)
    xx = getCsInfo("柳州", "广西")
    print(xx)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          so.html5.qq
   Description:
   Author:             Black Hole
   date:               2020/9/17
-------------------------------------------------
   Change Activity:    2020/9/17:
-------------------------------------------------
"""

__author__ = 'Black Hole'

import arrow

from utility.request import post

_json = {"pageIndex": 4,
         "cookieItem": {
             "dataname_deduplication": {},
             "subpager": {
                 "firstpage": {
                     "sBloomFilter": "bs85JO-@jlR}8XGzLOOqZNiMCjdd]ppXa+005AI3KEl~jEd1=$N*eP]F.C@6Dp#[kbwXeBnXTvAAoTOQYi"
                 },
                 "d3_news": {
                     "iCurPos": 30, "iIsEnd": 0,
                     "sBloomFilter": "bs85cm]GLfCdr+768BykOUwA5CI[n0L2i92mpZ4gg~I6P?EkR0s@]-Bme=`0e}br34}!kARrP9kc=RCm;gZt01;pe0001D2tz;s0f12mKm.9OKv-Qm02Dv~03r-k3?*6@gh2oR01f~E06-u*Kmnj)LaG2jzyJ",
                     "sExpandInfo": "{\"ir\":{\"cur_pos\":27,\"bloom_filter\":\"f00600408004120202004010100420001001200000400000080080508040a0805000004a000204000000000000000000080040060020100800040440080041080000200c000000420803400001804000000400080000400000000000000004000c12800200400000000c0000000004004001a04002800000c00001000002000016008000800000000000000000850088000000c08400000050800000020000882000010000800801018405002000020c108800009000400000104000000000200040000000001108400400204058000000044000002208000000000084010000000000000040000000010021402a00400000\"},\"vec\":{\"cur_pos\":12,\"bloom_filter\":\"f0060040800400020000000000002000000000000000000008000040800000a0000000480002040004000080000000000800000200200000000000400800010800010004000000000003400000004000000000000000410000000000000000000012800000000000000200000000040040008040020000008000000000000000000080000000000010000000000410000000000004000000008000000000600800000100010000000000010020000004900000000000000000000000000000200000000000001000400001200040000100100000000008000400000080000000000000000000000000000000002200000000\"}}"},
                 "page_self_tencent_video": {"iCurPos": 0, "iIsEnd": 1, "sBloomFilter": "bs85cm]Cf 07O0"}},
             "session_id": "e9422cdb4d10ef1741f367868b5e0fe0",
             "test_info": "246655;245588;136;136;136;136;195277;136;227815;136;0;0;0;0",
             "card_num": "140", "card_exposed_count": 30}, "tabId": "87", "bigCardIndex": 30,
         "conds": [], "q": "%E5%B9%BF%E5%B7%9E+%E6%9E%AA%E5%87%BB%E6%A1%88",
         "token": "7d0941650682728ba7fa88ea2d10f62536cae310a9d0f73dfbe084fa9ebb3cbcd7dc09aea116917d8a99877af0d9e37939b13adc7c982cb3ce7059d319b74070a878d0910360a8b298041ec8755362a96e31c366650a8c5835b0a05fa8e0719c4f9b8153f3ad35db70817a72e7a065c219d8c037f42be4a2d2240655d1e2ce4e5650ab1261de7a4aaa5b0a473dbd03c12a6eb6d1e16ea469e525a3f96598578cf0630f0a31bfe398da771408b6bc4badf1a7b0e0ce363a0bf8dac785d55ab1af",
         "r": arrow.now().timestamp * 1000, "updateQuery": False}

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 9; MIX 2 Build/PKQ1.190118.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.101 Mobile Safari/537.36 qnreading/'
}

url = 'https://so.html5.qq.com/ajax/real/kb_search_result?q=%E5%B9%BF%E5%B7%9E+%E6%9E%AA%E5%87%BB%E6%A1%88&entrytime=1600315807036&app_id=003&jump_from=&inlet=search_homepage_search&devid=f27739074b8684a8&appver=28_areading_6.7.80&tabId=&omgid=86d56102e2f0b5407b4ba96b9bf43d4cc041001021320c'
results = post(url=url, json=_json, headers=headers)
print(results.resp.json())

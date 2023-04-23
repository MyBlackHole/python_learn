#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
File Name:   1
Description:
Author:      Black Hole
date:        2021/05/10 10:06:12:

-------------------------------------------------
Change Activity:
             2021/05/10 10:06:12:
-------------------------------------------------
"""

from requests_html import HTMLSession

session = HTMLSession()

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Cookie": "BIDUPSID=7B8EC87D2405738D5BE949F485F7AF33; PSTM=1650960576; BAIDUID=F1FB6EED6B2A9571F8B962D96057AC0F:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=36309_31660_35914_36167_34584_35978_35801_36233_26350_36302_36061; delPer=0; PSINO=7; BAIDUID_BFESS=F1FB6EED6B2A9571F8B962D96057AC0F:FG=1; BA_HECTOR=20a08h2l24012ka0671h6k0va0q; BDRCVFR[X_XKQks0S63]=mk3SLVN4HKm; userFrom=www.baidu.com; firstShowTip=1; indexPageSugList=%5B%22%E5%B0%8F%E5%A7%90%E5%A7%90%22%5D; cleanHistoryStatus=0; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; ab_sr=1.0.1_MGQxNWMyMGVlMjNjNTFmMzRlMTZkZmQ3MGUzY2I1Y2M4ZGY3NGUxNWFiOGJhZTRiZDUxYmM1MzE2YzQwMzAzNzAwZGZmNTBkMzUzYjAzZmI5YWI2MTk3YTZlN2ZhNWRhNDRlNTgwNWQyNjUxM2M0ZjBiNTcwMTM4MzdkOTE4ODA3YWU4ZmIzMzVlMDExMTMzMDdiYmM3OTgxNmVlNzk5NQ==",
    "Pragma": "no-cache",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.50",
    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="100", "Microsoft Edge";v="100"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Linux"',
}
resp = session.get(
    url="https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=index&fr=&hs=0&xthttps=111110&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E5%B0%8F%E5%A7%90%E5%A7%90&oq=%E5%B0%8F%E5%A7%90%E5%A7%90&rsp=-1",
    headers=headers,
)

# resp.html.render()

# print(resp.html)
print(resp.html.html)

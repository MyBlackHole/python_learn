import requests

# cookies = {
#     # "_s_tentry": "www.baidu.com",
#     # "Apache": "6712409683332.314.1585018131002",
#     # "SINAGLOBAL": "6712409683332.314.1585018131002",
#     # "ULV": "1585018131021:1:1:1:6712409683332.314.1585018131002:",
#     # "login_sid_t": "9f05d72cdc02a4c4ae926e15dd5cacaf",
#     # "cross_origin_proto": "SSL",
#     # "WBtopGlobal_register_version": "3d5b6de7399dfbdb",
#     # "UOR": "www.baidu.com,open.weibo.com,login.sina.com.cn",
#     # "un": "15077459464",
#     # "wvr": '6',
#     # "SCF": "Aod9r5VgyBUgLQi5WrKC3EJW8mUsTUId6KS-eKzbTc_t5dzyNhywZ2LjGcMtkSvxWUrPQZvVq1s3WorfkAW50nQ.",
#     "SUB": "_2A25zj5AYDeRhGeNM7VEY8i3EwzuIHXVQ_IbQrDV8PUNbmtAfLROikW9NTh6JOEGra8vFBrt1CfT-448D4nryaD8O",
#     # "SUBP": "0033WrSXqPxfM725Ws9jqgMF55529P9D9WW85uUya2OdwLseHmb2YIC25JpX5KMhUgL.Fo-ESoe4eoeR1hM2dJLoIpjLxK.L1-zLBoqLxKBLBo.L12zLxKqL1-eLB-zt",
#     # "SUHB": "0z1AHSlXfOjmfB",
#     # "ALF": "1617758035",
#     # "SSOLoginState": "1586225224",
#     # "webim_unReadCount": "%7B%22time%22%3A1586225331377%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A4%2C%22msgbox%22%3A0%7D",
#     # "WBStorage": "42212210b087ca50|undefined",
# }

# headers = {
#     'cookie': '_s_tentry=www.baidu.com; Apache=6712409683332.314.1585018131002; SINAGLOBAL=6712409683332.314.1585018131002; ULV=1585018131021:1:1:1:6712409683332.314.1585018131002:; login_sid_t=9f05d72cdc02a4c4ae926e15dd5cacaf; cross_origin_proto=SSL; WBtopGlobal_register_version=3d5b6de7399dfbdb; UOR=www.baidu.com,open.weibo.com,login.sina.com.cn; un=15077459464; wvr=6; SCF=Aod9r5VgyBUgLQi5WrKC3EJW8mUsTUId6KS-eKzbTc_t5dzyNhywZ2LjGcMtkSvxWUrPQZvVq1s3WorfkAW50nQ.; SUB=_2A25zj5AYDeRhGeNM7VEY8i3EwzuIHXVQ_IbQrDV8PUNbmtAfLROikW9NTh6JOEGra8vFBrt1CfT-448D4nryaD8O; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WW85uUya2OdwLseHmb2YIC25JpX5KMhUgL.Fo-ESoe4eoeR1hM2dJLoIpjLxK.L1-zLBoqLxKBLBo.L12zLxKqL1-eLB-zt; SUHB=0z1AHSlXfOjmfB; ALF=1617758035; SSOLoginState=1586225224; webim_unReadCount=%7B%22time%22%3A1586225331377%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A4%2C%22msgbox%22%3A0%7D; WBStorage=42212210b087ca50|undefined'
# }

# # res = requests.get(url='https://s.weibo.com/weibo/%25E9%2595%25BF%25E6%25B2%2599%252B?topnav=1&wvr=6', headers=headers)
# res = requests.get(url='https://s.weibo.com/weibo/%25E9%2595%25BF%25E6%25B2%2599%252B?topnav=1&wvr=6', cookies=cookies)
# print(res.text)

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': 'www.baidu.com',
    # 'Referer': 'https://wappass.baidu.com/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'cross-site',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
}
# url = 'https://www.baidu.com/s?tn=news&rtt=4&bsst=1&cl=2&wd=%E4%B8%B4%E6%B1%BE+%E7%81%BE%E5%AE%B3%E4%BA%8B%E6%95%85&medium=1&x_bfe_rqs=20001&x_bfe_tjscore=0.714732&tngroupname=organic_news&newVideo=12&rsv_dl=news_b_pn&pn=10&p_tk=2506yugq4GzNxVn72iK%2FnUFN1H9sNparRt6fhSky7bbDW%2FtXldpcd%2BqRQj8BQQuLcgLQsOEl1yCJtxntkVDl6w35SKHMcRGg%2B6WSHT2qOF0CLg4%3D&p_timestamp=1601007660&p_signature=fb158093a36432407bc726f90010102f'
# url = 'http://tieba.baidu.com/f/search/res?ie=utf-8&qw=长沙&only_thread=0&pn=3'
url = "https://0.0.0.0:8000/todos/?a=0"

res = requests.get(url, verify=False)
print(res.text)
# while True:
#     try:
#         res = requests.get(url)
#         print(res.status_code)
#         print(res.text)
#         if res.status_code == 200:
#             cookies = res.cookies
#             print(cookies)
#     except Exception as e:
#         print(e)

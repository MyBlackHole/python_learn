import re
import requests

url = "https://s.weibo.com/weibo?q=梧州&typeall=1&suball=1&Refer=SWeibo_box"

cookies = {
    'SUB': '_2A25z2d1UDeThGeNN7VQS8yzMyjSIHXVQr0mcrDV_PUNbm9AfLRj8kW9NSWocDZmbkR6PK9_9kgmKRa7QWFBErfas',
    # 'SUBP': '0033WrSXqPxfM725Ws9jqgMF55529P9D9WhZWVLNJqk1rwGIpzll8Za55JpX5KzhUgL.Fo-0Soq0e0z7eKn2dJLoIEXLxKnLBoMLB-qLxKML1KMLBoBLxKML12zL1hzLxKqL1heLBoeLxKqL1-zLBozt',
    # 'SUHB': '0HTxLheWKdV3gL'
}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4164.2 Safari/537.36",
    "Host": "s.weibo.com",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Upgrade-Insecure-Requests": "1",
    'sec-ch-ua': '"\\Not;A\"Brand";v="99", "Google Chrome";v="85", "Chromium";v="85"'
}

response = requests.get(url=url, verify=False, cookies=cookies, headers=headers)
html = response.text
print(html)

p = re.findall(r'action-type="feed_list_item" mid="(\d*)"[\S\s]*?href="//weibo.com/(\d*)\?refer_flag=', html)
print(p)

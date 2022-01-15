import requests

cookies = {
    'SUB': '_2A25ztmxWDeRhGeBL7lUW9ybMzj-IHXVQwtqerDV8PUNbmtANLWfTkW9NRu5yTJ5SCVmtimDBFutMBn_cjVCi6uS8',
    # 'SUBP': '0033WrSXqPxfM725Ws9jqgMF55529P9D9WhZWVLNJqk1rwGIpzll8Za55JpX5KzhUgL.Fo-0Soq0e0z7eKn2dJLoIEXLxKnLBoMLB-qLxKML1KMLBoBLxKML12zL1hzLxKqL1heLBoeLxKqL1-zLBozt',
    # 'SUHB': '0HTxLheWKdV3gL'
}

# url = "https://s.weibo.com/weibo?q=梧州&typeall=1&suball=1&Refer=SWeibo_box"
url = "http://t.cn/A6AME2k2"

resp = requests.get(url=url, cookies=cookies)
print(resp.content.decode())
print(resp.raw)
print(resp.cookies)
print(resp.cookies.get('YF-Page-G0'))
print(dir(resp.cookies))

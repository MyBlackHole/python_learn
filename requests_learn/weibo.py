import requests

i = 1
count = 0
headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4093.3 Mobile Safari/537.36"
}
while True:
    url = (
        "https://m.weibo.cn/api/container/getIndex?containerid=100103type%3D1%26q%3D%E5%9B%BD%E5%8D%83&sudaref=m.weibo.cn&display=0&retcode=6102&page_type=searchall&page="
        + str(i)
    )
    rep = requests.get(url=url, headers=headers)
    i += 1
    print(i)
    print(rep.text)

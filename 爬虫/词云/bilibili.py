import requests

str = '78005204878162'
while True:
    url = 'https://bangumi.bilibili.com/review/web_api/short/list?media_id=427&folded=0&page_size=20&sort=0&cursor=%s' % str
    res = requests.get(url=url)
    res = res.json()
    pl_list = res['result']['list']
    str = pl_list[-1]['cursor']
    print(str)
    for i in pl_list:
        with open('bilibili评论.txt', 'a+', encoding='utf-8') as f:
            f.write(i['content'] + '\n')

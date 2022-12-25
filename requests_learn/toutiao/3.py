import requests
import hashlib
import json

def func1():
    s = set()
    offset=20
    page = 1
    while True:
        url = f"https://ib.snssdk.com/api/feed/forum_hot/v1/?query_id=6570895765428767246&count=20&offset={offset}&iid=100314522761"

        headers = {
            'Host': 'ib.snssdk.com',
            'accept': 'application/json',
            'user-agent': 'com.ss.android.article.news/7501 (Linux; U; Android 5.1.1; zh_CN; VOG-AL10; Build/HUAWEIVOG-AL10; Cronet/TTNetVersion:b97574c0 2019-09-24)'
        }

        response = requests.request("GET", url, headers=headers)

        _dict = json.loads(response.json()['data'][0]['content'])
        text = _dict['raw_data']['rich_title']
        print(text)
        print(page)

        h = hashlib.md5()
        h.update(text.encode())
        md5 = h.hexdigest()
        if md5 in s:
            print(f"md5={md5}")
        s.add(md5)
        offset += 20
        page += 1



if __name__ == "__main__":
    func1()


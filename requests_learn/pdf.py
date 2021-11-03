import requests

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4136.7 Safari/537.36',
}
resp = requests.get(url='http://www.mtrsz.com.cn/files/20200428/410007154资格预审公告0.pdf', headers=headers)
print(resp.raw)
print(resp.content)
print(resp.headers)

with open('1.pdf', 'bw') as f:
    f.write(resp.content)

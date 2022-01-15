import requests
from lxml import etree

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
    'Referer': 'https://music.163.com/',
}
headers1 = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
    'Referer': 'https://music.163.com/',
    'Upgrade-Insecure-Requests': '1',
    'cookie': ' __remember_me=true; _iuqxldmzr_=32; _ntes_nnid=e5c109ea91eb4b6fdb843b4b77d106ef,1567727413279; _ntes_nuid=e5c109ea91eb4b6fdb843b4b77d106ef; ntes_kaola_ad=1; WM_TID=GbSCjA%2BVH5xABRRBEFYt8xFKtneovi4l; P_INFO=wdd1998_1104@163.com|1569066325|0|youdaonote|00&99|null&null&null#shd&371500#10#0|&0||wdd1998_1104@163.com; usertrack=ezq0ZV2HOnyFhnSuFNUJAg==; WM_NI=zRRApnGf%2FVElw9UC%2FVFTEXkOjdS1hQMZhSsyjd7DySPATRv7HCXvzrGFq%2BKUWcpr26WQ%2BHNUoy3fgPKlTVTVCqppi2kBngE1yd482xHig7Ro8W1us%2Fp7xecgYK1yQahUcmQ%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee97f6439bb5a98fe93f8db48ab2c84b838b9faaf279afeda48fee698deb9ed1c42af0fea7c3b92aba8e9ea2f36685bae1b7c868b5e79ba4ae5e868c8bb9ea45aabc9dd2eb5b8f86a8b4f273aabcf9a5fc59949f9cb3f53d8c9d9897f97a859abfccca5f95bdc093b13e958fe5a9cd5fada7fd87e65c89b49cb7d75e81afc091ec3aa99ea288c83bbbbcfcd9b1748cb7a9d8d165fc89ff96f225b4e9b886e26d9b95ff9ad46bac8bad8ed437e2a3; JSESSIONID-WYYY=TDyW%5Clr9Ug%5Cv%2BsgrRcPNF9qc%2Ff8NA99J2WjZseWujBhAV8Af4hA0qleTHOKKPP5d%5C7N4Nze9zGzBsZqY3TuxFD8cQITnYrzJgdGppR0hG26vrINaODBx1S%5CDV2xslNC95Flms1IkADJyHh6utWdRBa3JKemnIOO5By0jhj0D6RXdC%5C0%2F%3A1569505549927; MUSIC_U=18cb38a196fcfcd8fde6499b18755cd3855d9593190e9b1a44cf9967b37d826990f905fc6a8bbf85bf55b575f572e26b93b9937ec34e61980e51664f974a9ba221fe15f086d8dfe7de39c620ce8469a8; __csrf=e9d6bed3928b908f753911d08a8cac97'
}
url = 'https://music.163.com/discover/toplist?id=3779629'
res = requests.get(url=url, headers=headers).text
ele = etree.HTML(res)
l = ele.xpath("//div[@id='song-list-pre-cache']/ul//li/a/@href")
print(l)
# name = ele.xpath("//div[@id='song-list-pre-cache']/ul//li/a/text()")
# for i in l:
#     id = i[9:]
#     # 歌曲外部链接
#     urls = 'http://m10.music.126.net/20190912091631/218e2e218c66463a45fa4c6b956d5265/ymusic/fa90/df9c/'+str(id)+'.mp3'
#     # print(urls)
#     res1 = requests.get(url=urls,headers=headers1).content
#     print(res1)
#     with open(i[1] + '.mp3', 'wb') as f:
#         f.write(res1)
#         print(i)

import re

import requests
from 猫眼评分.ana_api import analysis

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.17 Safari/537.36',
}
res = requests.get(url='https://maoyan.com/board/7', headers=headers)
url_list = re.findall(r'.*(/films/\d*).*', res.text)

print(url_list)
for i in url_list:
    details = requests.get(url='https://maoyan.com' + i, headers=headers).text
    name = re.findall(r'.*<h3 class="name">(.*)</h3>.*', details)
    print(name[0])
    score = re.findall(r'.*span class="stonefont">&#x(.*);\.&#x(.*);</span>.*', details)
    # print(score)
    # print(score[0][0])
    # print(score[0][1])
    font_url = re.findall(r'.*(//vfile\.meituan\.net/colorstone/\w*\.woff).*', details)
    # print(font_url)
    with open('tff.woff', 'wb') as f:
        f.write(requests.get(url='http:' + font_url[0], headers=headers).content)

    out_tff = analysis(score[0], 'tff.woff')
    print(out_tff[0], out_tff[1])
    print('*' * 20)

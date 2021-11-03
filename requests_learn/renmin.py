import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",
    'Connection': 'close'
}

# proxy = 'Administrator:HzsurunData@#12@60.190.238.166:38012'
# proxy = '60.190.238.166:38012'
proxy = '127.0.0.1:1081'

proxies = {
    'http': 'http://' + proxy,
    'https': 'http://' + proxy
}

if __name__ == '__main__':
    # run()
    url = 'https://app.peopleapp.com/WapApi/610/GovApi/govInfo?gov_id=2&securitykey=06b9af190cd492b417741e849223e7f8&interface_code=610'
    # html = requests.get(url=url, headers=headers, timeout=60).json()
    html = requests.get(url=url, headers=headers, proxies=proxies, timeout=60).json()
    print(html)

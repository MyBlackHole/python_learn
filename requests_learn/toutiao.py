import requests

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4136.7 Safari/537.36",
    "referer": "https://www.toutiao.com/a6823917063761822216/",
}

# cookies = {
#     '__ac_nonce': '05eb55a5400fec2f8e3fa',
#     '__ac_signature': 'iWYDtAAgEBAZmYEfwqX844lnQqAANfgHx0STTSRYEiEs3hOKXnGi9zjLKay9U5lIG--hYgKr-3kY0gxu7WqI6FnmtYT1NiAFE3DuoahTN1MHxlMMhkJgsmU5NE58u1B23.L'
# }
cookies = {
    "__ac_nonce": "05eb57fde00aba5eedf95",
    # '__ac_signature': 'iWYDtAAgEBAZmYEfwqX844lnQqAANfgHx0STTSRYEiEs3hOKXnGi9zjLKay9U5lIG--hYgKr-3kY0gxu7WqI6FnmtYT1NiAFE3DuoahTN1MHxlMMhkJgsmU5NE58u1B23.L',
    "__ac_signature": "BrpWcAAgEBAcoMC0Ad4MLwa7F2AAFgVgAtN8ldPtql65plcDHVcYwNp7hVk.KBk0PrDFeP3ZcLxl6fa6v59ZsNqly8ckRiwS.gzHxRRO2RR5XHGpVREUcXf7ZCRwWZJZgXo",
}

# resp = requests.get(url='https://sf1-ttcdn-tos.pstatp.com/obj/rc-web-sdk/acrawler.js', headers=headers)

resp = requests.get(
    url="https://www.toutiao.com/a6823917063761822216/",
    cookies=cookies,
    headers=headers,
)

res = resp.cookies.get_dict()
print(resp.text)
print(res)

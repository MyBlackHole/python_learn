import time

import requests
from requests.adapters import HTTPAdapter

s = requests.Session()
s.mount("http://", HTTPAdapter(max_retries=3))
s.mount("https://", HTTPAdapter(max_retries=3))
print(time.strftime("%Y-%m-%d %H:%M:%S"))

json = {"type": "1", "data": "1, 2"}

try:
    r = s.post(
        "http://119.3.212.162:38017/repeatJudge/judge/weibo", json=json, timeout=5
    )
    print(r.text)
except requests.exceptions.RequestException as e:
    print(e)

print(time.strftime("%Y-%m-%d %H:%M:%S"))

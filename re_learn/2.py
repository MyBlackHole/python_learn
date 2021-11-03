import re
import json

with open('./1.html') as f:
    text = f.read()


print(text)
p = re.search(r'var picdata=({.*})', text)
if p:
    data_str = p.group(1)

    _json = json.loads(data_str)
    data = _json.get('data', {})
    currPicList = data.get('currPicList')

    for i in currPicList:
        print(i.get('url'))
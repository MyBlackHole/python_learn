import re
from pathlib import Path

# 解析提取uid、mid与页数
p = Path('weibosearch.html')
html = p.open(encoding='utf-8').read()
p = re.findall(r'action-type="feed_list_item" mid="(\d*)"[\S\s]*?href="//weibo.com/(\d*)\?refer_flag=', html)
page = re.findall(r'>第(\d*?)页</a>', html)
print(p)
print(page)
# p = re.findall(r'href="//weibo.com/(\d*)/([A-Za-z]*)\?refer_flag=', html)
# p = re.findall(r'uid=(\d*)&mid=(\d*)&', html)
# print(len(p))
# print(len(set(p)))

# # 移动端blog
# url = "http://m.weibo.cn/{0}/{1}"
# response = requests.get(url="http://m.weibo.cn/1904947977/3926262076515093")
# html = response.text
# p = re.findall(r'var \$render_data = \[([\S\s]*)\]\[0\]', html)
# j = json.loads(p[0])
# with open('blog.json', 'w', encoding='utf-8') as f:
#     f.write(json.dumps(j))
# print(j)

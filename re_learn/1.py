import re

url = "https://weibo.com/2803301701/IARkXknHD?from=page_1002062803301701_profile&wvr=6&mod=weibotime&type=comment#_rnd1585733964484"

# url_split = url.split('/')
# print(url_split)
# print(len(url_split))

mtc = re.search("weibo.com/(\d+)", url)
print("search:", mtc.group())

mtc = re.findall("weibo.com/(\d+)", url)
print("findall:", mtc)

print("ok")

url = "https://app.thepaper.cn/clthttps://file.thepaper.cn/clt/img/defHeadNew.png"

print(re.search(r".*(https://.*?)$", url).group(1))

p = re.findall(r"abc.*|.*dbc.*", "abcdbcsdjk")
print(p)

print("*" * 10)
text = '"source": "<a href="https://weibo.com/" rel="nofollow">明星资讯 · 视频社区</a>"'
p_list = "".join(re.findall(r"<.*>(.*)</a>", text))
print(p_list)

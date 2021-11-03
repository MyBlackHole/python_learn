import requests

data = []
page = 1
_id = -1
DataSet = set()
while True:
    # # m.weibo接口
    # response = requests.get(url="https://m.weibo.cn/api/statuses/repostTimeline?id=4498651474933230&page={}".format(page))

    # app接口
    response = requests.get(
        url="https://api.weibo.cn/2/comments/build_comments?networktype=wifi&is_show_bulletin=2&c=android&s=33333333&id=4498648148376951&from=10A4195010&gsid=_2A25zpTpGDeRxGeNM7VEY8i3EwzuIHXVu88qOrDV6PUJbkdAKLW_MkWpNTh6JOGzR7qL8uWzb-fV_S294syjcwNZP&page={}".format(
            page))

    json = response.json()
    if page != 3:
        _id = json['root_comments'][0]['id']
        data += json['root_comments']
        page += 1
    else:
        break

print(len(data))
for i in data:
    DataSet.add(i['id'])

print(len(DataSet))

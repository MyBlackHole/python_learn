import arrow

i = arrow.now()
print(i)
print(i.timestamp)

# # arrow.get
# print(arrow.get('2012-06-05 16:20:03', 'YYYY-MM-DD HH:mm:ss'))
# print(arrow.get(1504384602))
# print(arrow.get('2005年01月01日', 'YYYY年MM月DD日'))
# print(arrow.get('2020-01-01'))
# print(arrow.get('2005/01/01'))
# print(arrow.get('2019.1.1'))

# a = arrow.get('2020.6.17 07:22:00')
a = arrow.get('16:28', 'mm:ss')
print(a.datetime)
# print(type(a))
# local_time = a.to('local')
# print(type(local_time))
# present = arrow.utcnow()
# print(a.humanize(present, locale='zh'))
# -*- coding: utf-8 -*-
# coding=utf-8

# local = utc.to('US/Pacific') # 时区修改
# local = utc.to('Asia/Shanghai') # 时区修改
local = arrow.now('local')  # 获取当前时间（推荐）
print(local)
print('-------------')

# 时间重设
print(local.replace(year=1))
print(local.replace(month=1))
print(local.replace(day=5))
print(local.replace(hour=23))
print(local.replace(minute=10))
print(local.replace(second=59))
print('-------------')

# 时间增减
print(local.shift(years=-1))
print(local.shift(months=-1).naive)
print(local.shift(days=-5))
print(local.shift(hours=-24))
print(local.shift(minutes=-10))
print(local.shift(seconds=-60))
print('-------------')

# 字符串转时间
print(arrow.get('2017-10-28T00:00:00+0800'))
# print(arrow.get('2017-10-28', 'YYYY-MM-DD'))  # 字符串转时间（不推荐这样用，没有设时区）
print(arrow.get('2017-10-28', 'YYYY-MM-DD', tzinfo='local'))  # （推荐）
print(arrow.get('2017-10-28', 'YYYY-MM-DD', tzinfo='Asia/Shanghai'))  # 这样也可以
print(arrow.get('2017-10-28 05:30:30', 'YYYY-MM-DD HH:mm:ss', tzinfo='local'))  # （推荐）
print('-------------')

# 时间戳 ?
print(local.timestamp)  # 时间戳
print(arrow.get('1509120000', tzinfo='local'))  # 时间戳字符串，转换为本时区的时间

# 时间转为字符串，输出（格式化）
print(local.format("YYYY-MM-DD"))
print(local.format("YYYY-MM-DD HH:mm:ss"))
print(local.replace(minutes=-1).humanize(locale='zh'))  # 本地化个性时间短语： 刚才，1分钟前，1天前，等　　（zh_tw  更多语言的支持，去查看arrow/locales.py）

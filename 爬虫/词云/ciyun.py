import re

import jieba
from wordcloud.wordcloud import WordCloud

datas = []
with open('bilibili评论.txt', 'r', encoding='utf-8') as w:
    text = w.readlines()
for i in text:
    i = re.sub(r'[\n()（）.。!！^/,，]', '', i)
    fenci = jieba.cut(i)
    fenci = ','.join(fenci).split(',')
    for j in fenci:
        datas.append(j)
print(datas)
for i in datas:
    with open('data.txt', 'a+', encoding='utf-8') as f:
        f.write(i + '\n')

with open('data.txt', 'r') as f:
    data_list = f.read()
w = WordCloud(font_path='simhei.ttf', width=500, height=500, margin=10, background_color='pink')
w.generate(data_list)
w.to_file('fist.jpg')

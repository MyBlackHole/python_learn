import json
import jieba

with open('qqqqq.json', 'r', encoding='utf-8') as f:
    text = f.read()

car_dict_list = json.loads(text)

s = set()

jieba.load_userdict('dict.txt')

with open('dict-2.txt', 'w', encoding='utf-8') as f:
    for car_dict in car_dict_list:
        style = car_dict['style']
        chile_list = jieba.cut(style.replace(" ", ""))
        _str = "(" + style + ") --- " + str(list(chile_list)) + "\n"
        f.write(_str)
        print(_str)
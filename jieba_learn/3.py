import json
import jieba

with open('dict-1.txt', 'r', encoding='utf-8') as f:
    text = f.read()

_str_list = json.loads(text)


jieba.load_userdict('dict.txt')

s = set()

for _str in _str_list:
    chile_list = jieba.cut(_str)
    for chile in chile_list:
        s.add(chile)


with open('dict-2.txt', 'w', encoding='utf-8') as f:
    f.write(json.dumps(list(s), ensure_ascii=False))
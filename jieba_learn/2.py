import jieba

jieba.load_userdict("dict.txt")

s_list = jieba.cut("e-tron 2019款 e-tron 纯电智酷型")
print(list(s_list))

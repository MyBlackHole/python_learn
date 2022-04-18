# -*- coding: utf-8 -*-
# @Project: company
# @Author: little fly
# @File name: test
# @Create time: 2020/10/31 9:51
import jieba
import joblib
import numpy as np
from gensim.models.word2vec import Word2Vec

# 加载词向量模型
word2vec = Word2Vec.load("word2vec.model")
# 加载svm分类模型
model = joblib.load("weather_svm.pkl")

# 封装词转换词向量的方法，list型
def total_vector(words):
    vec = np.zeros(128).reshape((1, 128))
    for word in words:
        try:
            vec += word2vec.wv[word].reshape((1, 128))
        except KeyError:
            continue
    return vec


# 封装预测方法
def svm_predict(query):
    words = jieba.lcut(str(query))
    words_vec = total_vector(words)
    result = model.predict(words_vec)
    if int(result) == 1:
        print("类别：天气")
    elif int(result) == 0:
        print("类别：其他")


# 调用预测
while 1:
    str_ = input("请输入：")
    svm_predict(str_)

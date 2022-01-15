# -*- coding: utf-8 -*-

# 导入必要的包
import jieba
import numpy as np
import pandas as pd
from gensim.models.word2vec import Word2Vec
import joblib
from sklearn.svm import SVC

# 读取两个类别的语料
pos = pd.read_csv('weather_pos.txt', encoding='UTF-8', header=None)
neg = pd.read_csv('weather_neg.txt', encoding='UTF-8', header=None)

# 进行分词处理
pos['words'] = pos[0].apply(lambda x: jieba.lcut(x))
neg['words'] = neg[0].apply(lambda x: jieba.lcut(x))

# 将正负语料进行合并成训练语料然后并打上标签，正语料打上标签1，负语料打上标签0
x = np.concatenate((pos['words'], neg['words']))
y = np.concatenate((np.ones(len(pos)), np.zeros(len(neg))))

# 训练词向量128维
word2vec = Word2Vec(x,
                    size=128,
                    window=3,
                    min_count=5,
                    sg=1,
                    hs=1,
                    iter=10,
                    workers=25)
word2vec.save('word2vec.model')


# 封装词转换词向量的方法，list型
def total_vector(words):
    vec = np.zeros(128).reshape((1, 128))
    for word in words:
        try:
            vec += word2vec.wv[word].reshape((1, 128))
        except KeyError:
            continue
    return vec


# 对x所有词转换成词向量，即合成训练集
train_vec = np.concatenate([total_vector(words) for words in x])

# 开始训练分类模型
model = SVC(kernel='rbf', verbose=True)
model.fit(train_vec, y)

# 保存模型为pkl文件
joblib.dump(model, 'weather_svm.pkl')

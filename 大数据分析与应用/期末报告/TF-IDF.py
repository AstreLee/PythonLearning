# -*- coding: utf-8 -*-
"""
@Author : xiaoxinxin
@Date : 2022/5/23 - 15:27
@File : TF-IDF.py
@IDE : PyCharm
"""

import jieba
import pandas as pd
from pandas import read_excel
from pyecharts import options as opts
from pyecharts.charts import Bar, Pie
from pyecharts.globals import ThemeType
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

df = read_excel(r'.\Resource\中国医生热评.xlsx', engine='openpyxl')
list1 = []
for length in range(len(df)):
    temp = str(df.iloc[length, 4]).encode('gbk', errors='ignore').decode('gbk').encode('utf-8').decode('utf-8')
    list1.append(temp.split('...')[0].strip().replace('\n', '').replace(' ', ''))
file = open('.\Resource\StopWord.txt')
Comment = file.read()
StopWordList = Comment.split('\n')
for index in range(len(list1)):
    array = jieba.lcut(list1[index])
    strArray = []
    for word in array:
        if word not in StopWordList:
            strArray.append(word)
    list1[index] = ' '.join(strArray)
print(list1)

vectorizer = CountVectorizer()  # 该类会将文本中的词语转换为词频矩阵，矩阵元素a[i][j] 表示j词在i类文本下的词频
transformer = TfidfTransformer()  # 该类会统计每个词语的tf-idf权值
tfidf = transformer.fit_transform(
    vectorizer.fit_transform(list1))  # 第一个fit_transform是计算tf-idf，第二个fit_transform是将文本转为词频矩阵
word = vectorizer.get_feature_names()  # 获取词袋模型中的所有词语
weight = tfidf.toarray().sum(axis=0)  # 将tf-idf矩阵抽取出来，元素a[i][j]表示j词在i类文本中的tf-idf权重

df = pd.DataFrame({'word': word, 'tfidf': weight.tolist()})
b = df.sort_values(by="tfidf", ascending=False)
for count in range(10):
    print(b.iloc[count, 0], ' <-> ', b.iloc[count, 1])

# --------------------------------------------------------------------------
# 对评论list1进行词频统计
# 首先创建一个字典
frequencyDict1 = {}
for commentList in list1:
    array = commentList.split(' ')
    for item in array:
        if frequencyDict1.get(item) is not None:
            frequencyDict1[item] += 1
        else:
            frequencyDict1[item] = 1

# 对字典内容进行排序，返回的结果是一个列表，列表中的每一个元素是元组类型
a1 = sorted(frequencyDict1.items(), key=lambda x: x[1], reverse=True)
# 绘制柱图
gx = []
gy = []
for num in range(9, -1, -1):
    gx.append(str(a1[num][0]))
    gy.append(int(a1[num][1]))
(
    Bar(init_opts=opts.InitOpts(theme=ThemeType.CHALK, width='1000px', height='500px'))
    .add_xaxis(gx)
    .add_yaxis("", gy)
    .reversal_axis()
    .set_global_opts(
    title_opts=opts.TitleOpts(title='词频柱状图', subtitle='数据来源：已知数据', pos_left='center'),
    )
).render('.\横向统计词频柱状图.html')

# --------------------------------------------------------------------------
# 对评论list1进行词性标注
# 首先创建一个字典
import jieba.posseg as ps
frequencyDict2 = {}
for commentList in list1:
    array = ps.cut(commentList.replace(' ', ''))
    for item in array:
        if frequencyDict2.get(item.word) is not None:
            frequencyDict2[item.word]['value'] += 1
        else:
            frequencyDict2[item.word] = {}
            frequencyDict2[item.word]['value'] = 1
            frequencyDict2[item.word]['wordType'] = item.flag
# 创建字典统计词性
wordType = {}
for item in frequencyDict2:
    if wordType.get(frequencyDict2[item]['wordType']) is not None:
        wordType[frequencyDict2[item]['wordType']] += 1
    else:
        wordType[frequencyDict2[item]['wordType']] = 1
a2 = sorted(wordType.items(), key=lambda x: x[1], reverse=True)
for length in range(10):
    print(a2[length][0], "->", a2[length][1])

# 绘制饼图统计词性
# # 首先绘制饼图
# 1. 获取数据
# 首先获取所有的省份数据
gx = []
gy = []
for count in range(10):
    gx.append(str(a2[count][0]))
    gy.append(int(a2[count][1]))
(
    Pie(init_opts=opts.InitOpts(theme=ThemeType.DARK, width='700px', height='400px'))
    .add("", list(zip(gx, gy)))
).render('.\饼图.html')



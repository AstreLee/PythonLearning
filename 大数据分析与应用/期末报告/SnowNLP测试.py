# -*- coding: utf-8 -*-
"""
@Author : xiaoxinxin
@Date : 2022/5/18 - 22:54
@File : SnowNLP测试.py
@IDE : PyCharm
"""

from pandas import read_excel
from snownlp import SnowNLP
import matplotlib.pyplot as plt
import numpy as np



df = read_excel(r'.\Resource\中国医生热评.xlsx', engine='openpyxl')
list1 = []
for length in range(len(df)):
    temp = str(df.iloc[length, 4]).encode('gbk', errors='ignore').decode('gbk').encode('utf-8').decode('utf-8')
    list1.append(temp.split('...')[0].strip().replace('\n', '').replace(' ', ''))

list2 = []
for item in list1:
    s = SnowNLP(item)
    list2.append(s.sentiments)
plt.hist(list2, bins=np.arange(0, 1, 0.01), facecolor='g')
plt.xlabel('Sentiments Probability')
plt.ylabel('Quantity')
plt.title('Analysis of Sentiments')
plt.show()


# ------------------------------------------------------------------
# 情感波动分析
result = []
i = 0
while i < len(list2):
    result.append(list2[i] - 0.5)
    i = i + 1

plt.plot(np.arange(0, 930, 1), result, 'k-')
plt.xlabel('Number')
plt.ylabel('Sentiment')
plt.title('Analysis of Sentiments')
plt.show()


# 将list2写入到文件中，方便后期词云图的展示
file = open(".\Resource\comment.txt", "w")
for item in list1:
    file.write(item)
    file.write('\n')



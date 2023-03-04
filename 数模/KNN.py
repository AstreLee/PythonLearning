# -*- coding: utf-8 -*-
"""
@Author : xiaoxinxin
@Date : 2022/9/17 - 17:08
@File : KNN.py
@IDE : PyCharm
"""

from sklearn.neighbors import KNeighborsClassifier
from pandas import read_excel
from sklearn.model_selection import train_test_split

data = read_excel("data/数据增强合并后的结果.xlsx")
df1 = read_excel("data/附件.xlsx", sheet_name="表单3")
df_train, df_test = train_test_split(data, test_size=.3, random_state=42)

y_train = df_train.iloc[:, 0]
y_test = df_test.iloc[:, 0]
X_train = df_train.drop(columns=['类型'], axis=1)
X_test = df_test.drop(columns=['类型'], axis=1)

neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(X_train, y_train)

# 对附件3的结果进行预测，0表示铅钡玻璃，1表示高钾玻璃
predict_target = neigh.predict(df1)
print(predict_target)

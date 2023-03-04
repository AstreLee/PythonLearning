# -*- coding: utf-8 -*-
"""
@Author : xiaoxinxin
@Date : 2022/9/16 - 17:22
@File : Logistic.py
@IDE : PyCharm
"""

from sklearn.linear_model import LogisticRegression
import pandas as pd
from sklearn.model_selection import train_test_split

df1 = pd.read_excel("data/附件.xlsx", sheet_name="表单3")
data = pd.read_excel('data/数据增强合并后的结果.xlsx')
df_train, df_test = train_test_split(data, test_size=0.2, random_state=40)


y_train = df_train.iloc[:, 0]
y_test = df_test.iloc[:, 0]
X_train = df_train.drop(columns=['类型'], axis=1)
X_test = df_test.drop(columns=['类型'], axis=1)

clf = LogisticRegression(random_state=0).fit(X_train, y_train)

# 对结果进行预测
y_pred = clf.predict(df1)
print(y_pred)

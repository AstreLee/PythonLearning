# -*- coding: utf-8 -*-
"""
@Author : xiaoxinxin
@Date : 2022/9/16 - 20:05
@File : smo数据平衡.py
@IDE : PyCharm
"""
# 使用imblearn库中上采样方法中的SMOTE接口
from imblearn.over_sampling import SMOTE
from pandas import read_excel
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# 定义SMOTE模型，random_state相当于随机数种子的作用
# 可通过radio参数指定对应类别要生成的数据的数量
smo = SMOTE(sampling_strategy=1, random_state=42)
df1 = read_excel("data/附件.xlsx", sheet_name="表单3")
data = read_excel("data/pb1.xlsx")
X_smo, y_smo = smo.fit_resample(data.drop(columns=['类型'], axis=1), data.iloc[:, 0])

# X = read_excel("data/高钾铅钡平衡后的数据.xlsx")
# df_train, df_test = train_test_split(data, test_size=.3, random_state=42)
#
# y_train = df_train.iloc[:, 0]
# y_test = df_test.iloc[:, 0]
# X_train = df_train.drop(columns=['类型'], axis=1)
# X_test = df_test.drop(columns=['类型'], axis=1)
#
# clf = LogisticRegression(random_state=0).fit(X_train, y_train)
# y_pred = clf.predict(df1)
# print(y_pred)

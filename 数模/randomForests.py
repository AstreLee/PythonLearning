# -*- coding: utf-8 -*-
"""
@Author : xiaoxinxin
@Date : 2022/9/16 - 19:27
@File : randomForests.py
@IDE : PyCharm
"""

from sklearn.ensemble import RandomForestClassifier
from pandas import read_excel
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

data = read_excel("data/数据增强合并后的结果.xlsx")
df1 = read_excel("data/附件.xlsx", sheet_name="表单3")
df_train, df_test = train_test_split(data, test_size=.3, random_state=42)

y_train = df_train.iloc[:, 0]
y_test = df_test.iloc[:, 0]
X_train = df_train.drop(columns=['类型'], axis=1)
X_test = df_test.drop(columns=['类型'], axis=1)

clf = RandomForestClassifier(max_depth=4, random_state=40)
clf.fit(X_train, y_train)
predict_target = clf.predict(X_test)
print(predict_target)
result = mean_squared_error(y_test, predict_target) ** 0.5
print(f'The RMSE of prediction is: {result}')


import time
import numpy as np

start_time = time.time()
importances = clf.feature_importances_
std = np.std([tree.feature_importances_ for tree in clf.estimators_], axis=0)
elapsed_time = time.time() - start_time
print(f"Elapsed time to compute the importances: {elapsed_time:.3f} seconds")

import pandas as pd

forest_importances = pd.Series(importances, index=['二氧化硅(SiO2)', '氧化钠(Na2O)', '氧化钾(K2O)', '氧化钙(CaO)',
                                                   '氧化镁(MgO)', '氧化铝(Al2O3)', '氧化铁(Fe2O3)', '氧化铜(CuO)',
                                                   '氧化铅(PbO)',
                                                   '氧化钡(BaO)', '五氧化二磷(P2O5)', '氧化锶(SrO)', '氧化锡(SnO2)',
                                                   '二氧化硫(SO2)', '有无风化'])

fig, ax = plt.subplots()
forest_importances.plot.bar(yerr=std, ax=ax)
ax.set_title("Feature importances using MDI")
ax.set_ylabel("Mean decrease in impurity")
fig.show()

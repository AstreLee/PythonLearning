# -*- coding: utf-8 -*-
"""
@Author : xiaoxinxin
@Date : 2022/9/16 - 16:30
@File : lightGbm.py
@IDE : PyCharm
"""

import pandas as pd
from sklearn.model_selection import train_test_split
import lightgbm as lgb

df1 = pd.read_excel("data/附件.xlsx", sheet_name="表单3")
data = pd.read_excel("data/all_after_data strenth.xlsx")
df_train, df_test = train_test_split(data, test_size=0.3, random_state=42)

# 开始装载数据
y_train = df_train.iloc[:, 0]
y_test = df_test.iloc[:, 0]
X_train = df_train.drop(columns=['类型'], axis=1)
X_test = df_test.drop(columns=['类型'], axis=1)

# 为lightgbm创建数据集
lgb_train = lgb.Dataset(X_train, y_train)
lgb_eval = lgb.Dataset(X_test, y_test, reference=lgb_train)

# 将所有的配置保存在字典对象中
params = {
    'boosting_type': 'gbdt',
    'objective': 'binary',
    'metric': {'l2', 'l1'},
    'num_leaves': 31,
    'learning_rate': 0.05,
    'feature_fraction': 0.9,
    'bagging_fraction': 0.8,
    'bagging_freq': 5,
    'verbose': 0
}

# 训练开始
gbm = lgb.train(params,
                lgb_train,
                num_boost_round=20,
                valid_sets=[lgb_eval],
                callbacks=[lgb.early_stopping(stopping_rounds=5)])

# 对附件3的结果进行预测，0表示铅钡玻璃，1表示高钾玻璃
y_pred = gbm.predict(df1)
List = y_pred.tolist()
for index in range(len(List)):
    if List[index] > 0.5:
        List[index] = 1
    else:
        List[index] = 0
print(List)

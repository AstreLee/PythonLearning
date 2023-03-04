# -*- coding: utf-8 -*-
"""
@Author : xiaoxinxin
@Date : 2022/9/16 - 20:43
@File : rfplotting.py
@IDE : PyCharm
"""
from sklearn.ensemble import RandomForestClassifier
from pandas import read_excel
from sklearn.model_selection import train_test_split
from sklearn.tree import export_graphviz

data = read_excel("data/pb1.xlsx")
df_train, df_test = train_test_split(data, test_size=.2, random_state=42)

y_train = df_train.iloc[:, 0]
y_test = df_test.iloc[:, 0]
X_train = df_train.drop(columns=['类型'], axis=1)
X_test = df_test.drop(columns=['类型'], axis=1)

clf = RandomForestClassifier(random_state=0, max_depth=10)
clf.fit(X_train, y_train)

estimator = clf.estimators_[90]

# 导出为dot文件，可以通过安装graphviz库来转换.dot文件，也可以通过在线转换工具进行转换
export_graphviz(estimator, out_file='tree.dot',
                feature_names=['二氧化硅(SiO2)', '氧化钠(Na2O)', '氧化钾(K2O)', '氧化钙(CaO)',
                               '氧化镁(MgO)', '氧化铝(Al2O3)', '氧化铁(Fe2O3)', '氧化铜(CuO)', '氧化铅(PbO)',
                               '氧化钡(BaO)', '五氧化二磷(P2O5)', '氧化锶(SrO)', '氧化锡(SnO2)', '二氧化硫(SO2)', '有无风化'
                               ],
                # class_names=['类型'],
                # rounded=True, proportion=False,
                precision=3)

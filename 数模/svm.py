# -*- coding: utf-8 -*-
"""
@Author : xiaoxinxin
@Date : 2022/9/17 - 17:00
@File : svm.py
@IDE : PyCharm
"""

from sklearn.inspection import DecisionBoundaryDisplay
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from pandas import read_excel
from pylab import *

# 添加支持中文字体
mpl.rcParams['font.sans-serif'] = ['SimHei']
warnings.filterwarnings("ignore")

data = read_excel("data/pb1.xlsx")
df1 = read_excel("data/附件.xlsx", sheet_name="表单3")
df_train, df_test = train_test_split(data, test_size=.2, random_state=42)

y_train = df_train.iloc[:, 0]
y_test = df_test.iloc[:, 0]
# X_train = df_train.drop(columns=['类型'], axis=1)
# X_test = df_test.drop(columns=['类型'], axis=1)
X_train = df_train.drop(columns=['类型', '二氧化硅(SiO2)', '氧化钠(Na2O)', '氧化钙(CaO)', '氧化钾(K2O)',
                                 '氧化镁(MgO)', '氧化铝(Al2O3)', '氧化铁(Fe2O3)', '氧化铜(CuO)',
                                 '五氧化二磷(P2O5)', '氧化锶(SrO)', '氧化锡(SnO2)', '二氧化硫(SO2)', '有无风化'
                                 ],
                        axis=1)
X_test = df_test.drop(columns=['类型', '二氧化硅(SiO2)', '氧化钠(Na2O)', '氧化钙(CaO)', '氧化钾(K2O)',
                               '氧化镁(MgO)', '氧化铝(Al2O3)', '氧化铁(Fe2O3)', '氧化铜(CuO)',
                               '五氧化二磷(P2O5)', '氧化锶(SrO)', '氧化锡(SnO2)', '二氧化硫(SO2)', '有无风化'
                               ],
                      axis=1)

clf = make_pipeline(StandardScaler(), SVC(gamma='auto', kernel="linear", class_weight={1: 20}))
clf.fit(X_train, y_train)
Pipeline(steps=[('standardscaler', StandardScaler()),
                ('svc', SVC(gamma='auto'))])
predict_target = clf.predict(X_test)
print(predict_target)

result = mean_squared_error(y_test, predict_target) ** 0.5
print(f'The RMSE of prediction is: {result}')

# 绘制散点图，看看模型在测试集上面的划分效果，这里选取的是氧化铅和氧化钡
colors = []
List = X_train.index.tolist()
print(List)
for item in List:
    if data.iloc[item, 0] == 1:
        colors.append('y')
    else:
        colors.append('b')

plt.scatter(X_train.loc[:, '氧化钡(BaO)'], X_train.loc[:, '氧化铅(PbO)'], c=colors, edgecolors="k")
# plot the decision functions for both classifiers

ax = plt.gca()
disp = DecisionBoundaryDisplay.from_estimator(
    clf,
    X_train,
    plot_method="contour",
    colors="r",
    levels=[0],
    alpha=0.5,
    linestyles=["-"],
    ax=ax,
)

# plot decision boundary and margins for weighted classes
wdisp = DecisionBoundaryDisplay.from_estimator(
    clf,
    X_train,
    plot_method="contour",
    colors="r",
    levels=[0],
    alpha=0.5,
    linestyles=["-"],
    ax=ax,
)


plt.show()

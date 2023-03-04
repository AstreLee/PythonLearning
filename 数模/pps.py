# -*- coding: utf-8 -*-
"""
@Author : xiaoxinxin
@Date : 2022/9/17 - 11:33
@File : pps.py
@IDE : PyCharm
"""

import seaborn as sns
import ppscore as pps
from pandas import DataFrame
from pandas import read_excel
from pylab import *
import warnings

# 添加支持中文字体
mpl.rcParams['font.sans-serif'] = ['SimHei']
warnings.filterwarnings("ignore")

data = read_excel("data/高钾原始数据.xlsx")
df = pps.matrix(data)
List = []
for i in range(15):
    subList = []
    for row in range(i * 15, (i + 1) * 15):
        subList.append(df.iloc[row, 2])
    List.append(subList)

df.to_excel("data/高钾pps.xlsx")
df1 = DataFrame(List, columns=['二氧化硅(SiO2)', '氧化钠(Na2O)', '氧化钾(K2O)', '氧化钙(CaO)',
                               '氧化镁(MgO)', '氧化铝(Al2O3)', '氧化铁(Fe2O3)', '氧化铜(CuO)', '氧化铅(PbO)',
                               '氧化钡(BaO)', '五氧化二磷(P2O5)', '氧化锶(SrO)', '氧化锡(SnO2)', '二氧化硫(SO2)', '有无风化'
                               ], index=['二氧化硅(SiO2)', '氧化钠(Na2O)', '氧化钾(K2O)', '氧化钙(CaO)',
                                         '氧化镁(MgO)', '氧化铝(Al2O3)', '氧化铁(Fe2O3)', '氧化铜(CuO)', '氧化铅(PbO)',
                                         '氧化钡(BaO)', '五氧化二磷(P2O5)', '氧化锶(SrO)', '氧化锡(SnO2)',
                                         '二氧化硫(SO2)', '有无风化'
                                         ])

plt.figure(figsize=(16, 12))
# 注意下面计算pps得分的热力图和corr相关性的热力图一次只能画一个，画其中一个的
# 时候需要注释掉另外一个的绘图代码
# 计算pps得分的热力图
sns.heatmap(df1, annot=True, fmt=".2f", cmap="Blues")
plt.show()
# 计算corr相关性矩阵(
sns.heatmap(data.corr(), vmin=-1, vmax=1, annot=True, fmt=".2f", cmap="Blues")
plt.show()

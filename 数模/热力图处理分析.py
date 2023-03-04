# -*- coding: utf-8 -*-
"""
@Author : xiaoxinxin
@Date : 2022/9/17 - 12:17
@File : 热力图处理分析.py
@IDE : PyCharm
"""

from pandas import read_excel
from pandas import DataFrame

df = read_excel("热力图.xlsx")

List = []
for i in range(15):
    subList = []
    for row in range(i * 15, (i + 1) * 15):
        subList.append(df.iloc[row, 2])
    List.append(subList)

df1 = DataFrame(List, columns=['二氧化硅(SiO2)', '氧化钠(Na2O)', '氧化钾(K2O)', '氧化钙(CaO)',
                               '氧化镁(MgO)', '氧化铝(Al2O3)', '氧化铁(Fe2O3)', '氧化铜(CuO)', '氧化铅(PbO)',
                               '氧化钡(BaO)', '五氧化二磷(P2O5)', '氧化锶(SrO)', '氧化锡(SnO2)', '二氧化硫(SO2)', '有无风化'
                               ], index=['二氧化硅(SiO2)', '氧化钠(Na2O)', '氧化钾(K2O)', '氧化钙(CaO)',
                                         '氧化镁(MgO)', '氧化铝(Al2O3)', '氧化铁(Fe2O3)', '氧化铜(CuO)', '氧化铅(PbO)',
                                         '氧化钡(BaO)', '五氧化二磷(P2O5)', '氧化锶(SrO)', '氧化锡(SnO2)',
                                         '二氧化硫(SO2)', '有无风化'
                                         ])
df1.to_excel("新热力图.xlsx")

# -*- coding: utf-8 -*-
"""
@Author : xiaoxinxin
@Date : 2022/9/17 - 9:00
@File : mixup数据增强.py
@IDE : PyCharm
"""

import random
from pandas import read_excel
from numpy.random import beta
from pandas import DataFrame

df_K = read_excel("data/newk.xlsx")
df_Pb = read_excel("data/newPb.xlsx")

alpha = 0.3

List = []
for row in range(len(df_K)):
    subList = []
    for col in range(16):
        subList.append(df_K.iloc[row, col])
    List.append(subList)

count = 0
newList = []
while count < 1960:
    index1 = random.randint(0, len(df_K) - 1)
    index2 = random.randint(0, len(df_K) - 1)
    point_i = List[index1]
    point_j = List[index2]
    lam = beta(alpha, alpha)
    subList = []
    for index in range(0, 16):
        if index == 15:
            if lam > 0.5:
                lam = 1
                subList.append(lam * point_i[index] + (1 - lam) * point_j[index])
            else:
                lam = 0
                subList.append(lam * point_i[index] + (1 - lam) * point_j[index])
            continue
        subList.append(round((lam * point_i[index] + (1 - lam) * point_j[index]), 3))
    newList.append(subList)
    count += 1

df = DataFrame(newList, columns=['类型', '二氧化硅(SiO2)', '氧化钠(Na2O)', '氧化钾(K2O)', '氧化钙(CaO)',
                                 '氧化镁(MgO)', '氧化铝(Al2O3)', '氧化铁(Fe2O3)', '氧化铜(CuO)', '氧化铅(PbO)',
                                 '氧化钡(BaO)', '五氧化二磷(P2O5)', '氧化锶(SrO)', '氧化锡(SnO2)', '二氧化硫(SO2)',
                                 '有无风化'
                                 ])

df.to_excel("data/strength_K_1.xlsx", index=False)



List = []
for row in range(len(df_Pb)):
    subList = []
    for col in range(16):
        subList.append(df_Pb.iloc[row, col])
    List.append(subList)

count = 0
newList = []
while count < 1960:
    index1 = random.randint(0, len(df_Pb) - 1)
    index2 = random.randint(0, len(df_Pb) - 1)
    point_i = List[index1]
    point_j = List[index2]
    lam = beta(alpha, alpha)
    subList = []
    for index in range(0, 16):
        if index == 15:
            if lam > 0.5:
                lam = 1
                subList.append(lam * point_i[index] + (1 - lam) * point_j[index])
            else:
                lam = 0
                subList.append(lam * point_i[index] + (1 - lam) * point_j[index])
            continue
        subList.append(round((lam * point_i[index] + (1 - lam) * point_j[index]), 3))
    newList.append(subList)
    count += 1

df = DataFrame(newList, columns=['类型', '二氧化硅(SiO2)', '氧化钠(Na2O)', '氧化钾(K2O)', '氧化钙(CaO)',
                                 '氧化镁(MgO)', '氧化铝(Al2O3)', '氧化铁(Fe2O3)', '氧化铜(CuO)', '氧化铅(PbO)',
                                 '氧化钡(BaO)', '五氧化二磷(P2O5)', '氧化锶(SrO)', '氧化锡(SnO2)', '二氧化硫(SO2)',
                                 '有无风化'
                                 ])

df.to_excel("data/strength_Pb_1.xlsx", index=False)

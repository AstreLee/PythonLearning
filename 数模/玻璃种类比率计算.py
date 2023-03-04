# -*- coding: utf-8 -*-
"""
@Author : xiaoxinxin
@Date : 2022/9/16 - 13:41
@File : 玻璃种类比率计算.py
@IDE : PyCharm
"""

from pandas import read_excel
from pandas import DataFrame

rate_K = []  # 钾玻璃的比率
rate_Pb = []  # 铅钡玻璃的比率

# 钾玻璃风化前各种元素含量的平均值
elem_K_before = [67.028, 0.976, 8.937, 0.036, 0.169, 0.087, 4.571, 1.059, 1.804, 2.272, 0.38, 0.513, 1.234, 5.899]
# 钾玻璃风化后各种元素含量的平均值
elem_K_after = [93.963, 0, 0.543, 0, 0, 0, 0.87, 0.197, 0.265, 1.562, 0, 0, 0.28, 1.93]

# 铅钡玻璃风化前各种元素含量的平均值
elem_Pb_before = [53.444, 0.772, 0.258, 1.232, 0.492, 3.195, 23.594, 10.499, 0.904, 0.297, 0.065, 0.282, 0.933, 1.557]
# 铅钡玻璃风化后各种元素含量的平均值
elem_Pb_after = [33.615, 0.953, 0.143, 2.346, 0.701, 3.838, 36.872, 10.487, 4.155, 0.366, 0.056, 0.987, 0.556, 1.996]

for index in range(14):
    if elem_K_after[index] != 0:
        rate_K.append(elem_K_before[index] / elem_K_after[index])
    else:
        rate_K.append(elem_K_before[index])
    rate_Pb.append(elem_Pb_before[index] / elem_Pb_after[index])

# 首先计算高钾玻璃的风化前的含量，去遍历k.xlsx文件中的行
List_K = []
df_K = read_excel("k.xlsx")
for row in range(len(df_K)):
    if df_K.iloc[row, 18] == '风化':
        subList = [str(df_K.iloc[row, 0])]
        for col in range(1, 15):
            if df_K.iloc[row, col] == 0:
                subList.append(round(df_K.iloc[row, col] + elem_K_before[col - 1], 2))
            else:
                if rate_K[col - 1] == elem_K_before[col - 1]:
                    subList.append(round(df_K.iloc[row, col] + elem_K_before[col - 1], 2))
                else:
                    subList.append(round(df_K.iloc[row, col] * rate_K[col - 1], 2))
        List_K.append(subList)

tran_K = DataFrame(List_K, columns=['文物编号', '二氧化硅(SiO2)', '氧化钠(Na2O)', '氧化钾(K2O)', '氧化钙(CaO)',
                                    '氧化镁(MgO)', '氧化铝(Al2O3)', '氧化铁(Fe2O3)', '氧化铜(CuO)', '氧化铅(PbO)',
                                    '氧化钡(BaO)', '五氧化二磷(P2O5)', '氧化锶(SrO)', '氧化锡(SnO2)', '二氧化硫(SO2)'])

tran_K.to_excel("高钾风化前元素含量预测.xlsx")

# 再来计算铅钡玻璃的风化前的含量
df_Pb = read_excel("pb.xlsx")
List_Pb = []
for row in range(len(df_Pb)):
    if df_Pb.iloc[row, 18] == '风化':
        subList = [str(df_Pb.iloc[row, 0])]
        for col in range(1, 15):
            if df_Pb.iloc[row, col] == 0:
                subList.append(round(df_Pb.iloc[row, col] + elem_Pb_before[col - 1], 2))
            else:
                subList.append(round(df_Pb.iloc[row, col] * rate_Pb[col - 1], 2))
        List_Pb.append(subList)


tran_Pb = DataFrame(List_Pb, columns=['文物编号', '二氧化硅(SiO2)', '氧化钠(Na2O)', '氧化钾(K2O)', '氧化钙(CaO)',
                                    '氧化镁(MgO)', '氧化铝(Al2O3)', '氧化铁(Fe2O3)', '氧化铜(CuO)', '氧化铅(PbO)',
                                    '氧化钡(BaO)', '五氧化二磷(P2O5)', '氧化锶(SrO)', '氧化锡(SnO2)', '二氧化硫(SO2)'])


tran_Pb.to_excel("铅钡风化前元素含量预测.xlsx")

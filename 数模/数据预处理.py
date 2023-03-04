# -*- coding: utf-8 -*-
"""
@Author : xiaoxinxin
@Date : 2022/9/18 - 1:43
@File : 数据预处理.py
@IDE : PyCharm
"""

from pandas import read_excel

# # 首先对高钾进行处理
# df_K = read_excel("data/k.xlsx")
# rate_K = []  # 声明K的各元素所占的比例
# sum = 0
# for col in range(1, 15):
#     sum += df_K.iloc[20, col]
# for col in range(1, 15):
#     rate_K.append(df_K.iloc[20, col] / sum)
# # 现在开始填充
# for row in range(len(df_K)):
#     subSum = 0
#     for col in range(1, 15):
#         subSum += df_K.iloc[row, col]
#     redundant = 100 - subSum
#     for col in range(1, 15):
#         if df_K.iloc[row, col] == 0:
#             df_K.iloc[row, col] = round(redundant * rate_K[col - 1], 2)
#
# df_K.to_excel("data/k.xlsx")


# 再来对铅钡进行处理
df_Pb = read_excel("data/pb.xlsx")
rate_Pb = []  # 声明K的各元素所占的比例
sum = 0
for col in range(1, 15):
    sum += df_Pb.iloc[49, col]
for col in range(1, 15):
    rate_Pb.append(df_Pb.iloc[49, col] / sum)
# 现在开始填充
for row in range(len(df_Pb)):
    subSum = 0
    for col in range(1, 15):
        subSum += df_Pb.iloc[row, col]
    redundant = 100 - subSum
    for col in range(1, 15):
        if df_Pb.iloc[row, col] == 0:
            df_Pb.iloc[row, col] = round(redundant * rate_Pb[col - 1], 2)

df_Pb.to_excel("data/pb.xlsx")

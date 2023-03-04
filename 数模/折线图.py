# -*- coding: utf-8 -*-
"""
@Author : xiaoxinxin
@Date : 2022/9/15 - 19:39
@File : 折线图.py
@IDE : PyCharm
"""

# from pandas import read_excel
#
# # df = read_excel("附件.xlsx")
# # print(df)
#
# # ----------------
# #
# # import pandas as pd
#
# df = read_excel("附件.xlsx", sheet_name="表单2")
# List = []
#
# # for row in range(len(df)):
# #     List.append(df.iloc[row, 0])
# # print(List)
# for row in range(len(df)):
#     new_dict = {'name': df.iloc[row, 0], 'type': 'line'}
#     subList = []
#     for col in range(1, 15):
#         subList.append(df.iloc[row, col])
#     new_dict['data'] = subList
#     List.append(new_dict)
# print(List)

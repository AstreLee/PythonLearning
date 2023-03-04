# -*- coding: utf-8 -*-
"""
@Author : xiaoxinxin
@Date : 2022/3/30 - 17:11
@File : 08_关于iloc和ioc的完整版总结.py
@IDE : PyCharm
"""
from pandas import DataFrame

df0 = {'Ohio': [0, 6, 3], 'Texas': [7, 4, 1], 'California': [2, 8, 5]}
df = DataFrame(df0, index=['a', 'c', 'd'])
# print(df.sort_values(by=['California', 'Texas']))
print(df.sort_values(by=['California', 'Texas']))

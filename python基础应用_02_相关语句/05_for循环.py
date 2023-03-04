# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/7/31 - 8:26
@file : 05_for循环.py
@ide : PyCharm
"""

str1 = "itheima"
for i in str1:
    print(i, end='')  # 取消换行
print()
str2 = 'itheima'
for i in str2:
    if i == 'e':
        print('遇到e不打印', end='')
        continue
    print(i, end='')


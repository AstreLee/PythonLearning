# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/9/16 - 22:34
@file : 3_3.py
@ide : PyCharm
"""


sum = 0
for i in range(1, 101):
    if i % 4 == 0:
        sum += i
print("1~100以内所有能被4整除的数字之和为：", sum)

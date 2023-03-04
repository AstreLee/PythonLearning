# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/9/19 - 10:34
@file : 5_5.py
@ide : PyCharm
"""


def func(n):
    if n % 2 == 0:
        sum1 = 0
        for i in range(2, 2*n + 1, 2):
            sum1 += 1 / i
        return sum1
    else:
        sum2 = 0
        for j in range(1, 2 * n + 2, 2):
            sum2 += 1 / j
        return sum2


a = int(input("请输入一个整数："))
print(f'和为：{func(a)}')

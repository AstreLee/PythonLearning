# -*- coding: utf-8 -*-
"""
@Author : xiaoxinxin
@Date : 2021/10/14 - 16:02
@File : 7_4.py
@IDE : PyCharm
"""


import timeit


def sumI():
    res = 0
    for i in range(1, 10001):
        res += i


print("该函数执行的时间为：", timeit.timeit(stmt=sumI, number=1))

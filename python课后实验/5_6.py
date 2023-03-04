# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/9/19 - 10:34
@file : 5_6.py
@ide : PyCharm
"""


def diGuiFunc(x):
    if x < 1:
        return -1
    elif x == 1:
        return 10
    else:
        return diGuiFunc(x - 1) + 2


def notDiDuiFunc(x):
    year = 10
    for i in range(x - 1):
        year += 2
    return year


print("递归函数实现：年龄为：", diGuiFunc(5))
print("非递归函数实现：年龄为：", notDiDuiFunc(5))

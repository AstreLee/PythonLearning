# -*- coding: utf-8 -*-
"""
@Author : xiaoxinxin
@Date : 2021/12/23 - 16:09
@File : Question2.py
@IDE : PyCharm
"""


def sumPaduowa(n):
    if n == 1 or n == 2 or n == 3:
        return 1
    else:
        return sumPaduowa(n - 2) + sumPaduowa(n - 3)


# 主程序开始
sumAll = 0
for i in range(1, 11):
    sumAll += sumPaduowa(i)
print("前十项和为：", sumAll)

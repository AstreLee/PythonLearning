# -*- coding: utf-8 -*-
"""
@Author : xiaoxinxin
@Date : 2021/10/14 - 16:03
@File : 7_5.py
@IDE : PyCharm
"""


import random
import numpy


list1 = []
for i in range(12):
    list1.append(random.randint(1, 100))
numpy.array(list1).reshape(3, 4)
average = 0
sumCount = 0
for i in range(len(list1)):
    sumCount += list1[i]
average = sumCount / len(list1)
print("数组平均值为：", average)

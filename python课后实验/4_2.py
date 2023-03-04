# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/9/17 - 19:30
@file : 4_2.py
@ide : PyCharm
"""


import random


list1 = []
for i in range(10):
    list1.append(random.randint(1, 100))
j = 0
for i in list1:
    if i % 2 == 0:
        list1[j] = i**3
    else:
        list1[j] = i**2
    j += 1

print(list1)

# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/9/17 - 19:54
@file : 4_5.py
@ide : PyCharm
"""


import random


list1 = []
for i in range(20):
    list1.append(random.randint(1, 10))
tuple1 = tuple(list1)
for i in range(1, 11):
    print(f'{i}出现的次数为：{tuple1.count(i)}')
print(tuple1)



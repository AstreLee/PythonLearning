# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/9/16 - 22:12
@file : 2_6.py
@ide : PyCharm
"""


list0 = [i for i in range(1, 11)]


def isEvenNumber(x):
    if x % 2 == 0:
        return x


def isOddNumber(x):
    if x % 2 != 0:
        return x


list1 = list(filter(isEvenNumber, list0))
list2 = list(filter(isOddNumber, list0))
print(list1)
print(list2)
list3 = []
for i in range(len(list1)):
    list3.append(list1[i] * 10 + list2[i])
print(list3)

# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/9/17 - 19:36
@file : 4_3.py
@ide : PyCharm
"""


# 方式一
list1 = [3, 8, 11, 26, 47]
a = int(input("请输入一个整数："))
list1.append(a)
for i in range(len(list1) - 1):
    for j in range(len(list1) - i - 1):
        if list1[j] > list1[j + 1]:
            list1[j], list1[j + 1] = list1[j + 1], list1[j]
print(list1)


# 方式二
list2 = [3, 8, 11, 26, 47]
b = int(input("请输入一个整数："))
j = 0
for i in list2:
    if i < b:
        j += 1
        continue
    else:
        list2.insert(j, b)
        break
print(list2)

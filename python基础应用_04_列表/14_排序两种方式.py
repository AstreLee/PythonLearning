# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/9/9 - 23:09
@file : 14_排序两种方式.py
@ide : PyCharm
"""

# 冒泡排序
list1 = [1, 3, 2, 6, 4, 5, 1, 4, 8]
for i in range(len(list1) - 1):
    for j in range(len(list1) - 1 - i):
        if list1[j] < list1[j + 1]:
            list1[j] = list1[j] + list1[j + 1]
            list1[j + 1] = list1[j] - list1[j + 1]
            list1[j] = list1[j] - list1[j + 1]
print(list1)

# 选择排序方式一
list2 = [1, 3, 2, 6, 4, 5, 1, 4, 8]
for i in range(len(list2) - 1):
    for j in range(i + 1, len(list2)):
        if list2[i] > list2[j]:
            list2[i] = list2[i] + list2[j]
            list2[j] = list2[i] - list2[j]
            list2[i] = list2[i] - list2[j]
print(list2)

# 选择排序方式二
list3 = [1, 3, 2, 6, 5, 4, 7, 8, 1, 9]
for i in range(len(list3) - 1):
    k = i
    for j in range(i + 1, len(list3)):
        if list3[k] > list3[j]:
            k = j
    if k != i:
        list3[i] = list3[k] + list3[i]
        list3[k] = list3[i] - list3[k]
        list3[i] = list3[i] - list3[k]
print(list3)
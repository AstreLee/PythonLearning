# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/9/9 - 22:57
@file : 13_查找两种方式.py
@ide : PyCharm
"""

# 1. 线性查找
list1 = [1, 3, 56, 34, 23, 11, 16, 90, 100, 8, 22]
search = int(input("请输入您要查找的数字:"))
for i in list1:
    if i == search:
        print("找到了!")
        break
else:
    print("没有找到!")

# 2. 折半查找
list2 = [1, 3, 56, 34, 23, 11, 16, 90, 100, 8, 22]
list2.sort()
search = int(input("请输入您要查找的数字:"))
low = 0
high = len(list2) - 1
while low <= high:
    middle = int((low + high) / 2)
    if list2[middle] < search:
        low = middle + 1
    if list2[middle] > search:
        high = high - 1
    if list2[middle] == search:
        print("找到了!")
        break
else:
    print("没有找到!")


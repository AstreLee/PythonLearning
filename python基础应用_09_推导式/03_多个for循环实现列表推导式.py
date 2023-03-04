# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/8/1 - 15:35
@file : 03_多个for循环实现列表推导式.py
@ide : PyCharm
"""

list3 = []
for i in range(1, 3):
    for j in range(3):
        list3.append((i, j))
print(list3)
list1 = [(i, j) for i in range(1, 3) for j in range(3)]  # 实际上就是两个for嵌套循环
print(list1)

list2 = [(i, j, k) for i in range(2) for j in range(2) for k in range(2)]
print(list2)

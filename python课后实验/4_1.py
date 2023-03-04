# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/9/17 - 19:18
@file : 4_1.py
@ide : PyCharm
"""


list1 = [1, 2, 3]
list2 = [4, 5, 6]
# 方法一
list3 = []
list3 = list1 + list2
print(list3)


# 方法二
list4 = []
for i in list1:
    list4.append(i)
for i in list2:
    list4.append(i)
print(list4)

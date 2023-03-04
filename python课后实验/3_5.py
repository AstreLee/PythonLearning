# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/9/16 - 22:39
@file : 3_5.py
@ide : PyCharm
"""


list1 = [1, 2, 3, 4]
list2 = []
count = 0
for i in range(4):
    for j in range(4):
        for k in range(4):
            for temp in list2:
                if list1[i]*100 + list1[j]*10 + list1[k] == temp:
                    continue
            else:
                list2.append(list1[i]*100 + list1[j]*10 + list1[k])
                count += 1
count1 = 0
for i in list2:
    print(i, end=" ")
    count1 += 1
    if count1 == 20:
        print()
        count1 = 0
print()

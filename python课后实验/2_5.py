# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/9/16 - 21:54
@file : 2_5.py
@ide : PyCharm
"""


str1 = input("请输入一个4位整数：")
list1 = []
# 数字变换
i = 0
while i < len(str1):
    temp = int(str1[i])
    temp += 5
    temp %= 10
    list1.append(temp)
    i += 1
# 交换顺序
list1[0], list1[3] = list1[3], list1[0]
list1[1], list1[2] = list1[2], list1[1]
print("加密后的数据为：", end="")
for i in list1:
    print(i, end="")





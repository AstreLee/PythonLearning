# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/9/19 - 10:34
@file : 5_7.py
@ide : PyCharm
"""


def isWs(n):
    list1 = []
    for i in range(1, n):
        if n % i == 0:
            list1.append(i)
    sum = 0
    for i in list1:
        sum += i
    if sum == n:
        return True
    else:
        return False


a = int(input("请输入一个整数："))
if isWs(a):
    print(f'{a}是一个完数!')
else:
    print(f'{a}不是一个完数')



# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/9/16 - 22:35
@file : 3_4.py
@ide : PyCharm
"""


from math import sqrt


def isPrime(x):
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    else:
        return True


print("100~1000之内的所有的素数为：")
count = 0
for i in range(100, 1001):
    if isPrime(i):
        print(i, end=" ")
        count += 1
    if count == 20:
        print()
        count = 0

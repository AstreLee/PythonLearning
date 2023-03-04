# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/9/19 - 10:34
@file : 5_8.py
@ide : PyCharm
"""

from math import sqrt


def isPrime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    else:
        return True


def isGDBH(n):
    list_GDBH = []
    list_prime = []  # 2~100以内的素数
    for i in range(2, 100):
        if isPrime(i):
            list_prime.append(i)
    for j in range(0, len(list_prime)):
        for k in range(j, len(list_prime)):
            if list_prime[j] + list_prime[k] == n:
                list_GDBH.append(f'{n}={list_prime[j]}+{list_prime[k]}')
    return list_GDBH


# 打印6到100的所有偶数的素数之和
for i in range(6, 101, 2):
    print(isGDBH(i))


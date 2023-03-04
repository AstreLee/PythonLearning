# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/9/17 - 20:27
@file : 5_1.py
@ide : PyCharm
"""


def func(n):
    return bin(n)


a = int(input("请输入一个十进制数："))
print(f'{a}十进制数字对应二进制数为:{func(a)}')


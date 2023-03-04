# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/8/4 - 11:07
@file : 10_交换变量的方式.py
@ide : PyCharm
"""


# 设置一个临时变量
c = 0  # 此乃临时变量
a = 1
b = 2
print(a)
print(b)
c = a
a = b
b = c
print(a)
print(b)


# 直接交换  √√√
a, b = 1, 2
print(a)
print(b)
a, b = b, a
print(a)
print(b)

# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/9/16 - 22:48
@file : 3_6.py
@ide : PyCharm
"""


def isShuiXianHuaNumber(x):
    a = x % 10  # 个位
    b = x // 10 % 10  # 十位
    c = x // 100  # 百位
    if a**3 + b**3 + c**3 == c*100 + b*10 + a:
        return True
    else:
        return False


print("所有的水仙花数如下：")
for i in range(100, 1000):
    if isShuiXianHuaNumber(i):
        print(i)

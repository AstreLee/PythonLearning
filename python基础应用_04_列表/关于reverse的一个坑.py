# -*- coding: utf-8 -*-
"""
@Author : xiaoxinxin
@Date : 2021/11/20 - 23:05
@File : 关于reverse的一个坑.py
@IDE : PyCharm
"""

# 注意了, reverse()函数是没有返回值的，只能对列表先用reverse()函数，再打印原列表
L1 = [1, 2, 3, 4]
L2 = L1.reverse()
print(L2)  # None

L3 = [1, 2, 3, 4]
L3.reverse()
print(L3)

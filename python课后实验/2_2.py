# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/9/16 - 21:36
@file : 2_2.py
@ide : PyCharm
"""


from math import sqrt, cos


x = float(input("请输入x:"))
y = float(input("请输入y:"))
z = float(input("请输入z:"))

print("表达式的值为:", (3*x + 4*sqrt(x**2 + 2*y**2)) / (1 + cos(z**3)))

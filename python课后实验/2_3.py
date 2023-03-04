# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/9/16 - 21:43
@file : 2_3.py
@ide : PyCharm
"""

from math import sqrt


a = int(input("请输入二次方项："))
b = int(input("请输入一次方项："))
c = int(input("请输入零次方项："))

# 注意根号下面要是非负的
try:
    x1 = (-b + sqrt(b*b - 4*a*c)) / (2*a)
    x2 = (-b - sqrt(b*b - 4*a*c)) / (2*a)
    print("x1 =", x1, ",x2 =", x2)
except Exception as e:
    print("输入有误:", e)

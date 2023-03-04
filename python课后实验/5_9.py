# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/9/19 - 10:34
@file : 5_9.py
@ide : PyCharm
"""

from math import pi


# 定义装饰器
def deco1(func):
    # 检查func(x, y)中的参数
    def check_call_func(x, y, z):
        if x >= 0 and y >= 0 and z >= 0:
            return func(x, y, z)
        else:
            print("提示：函数参数必须为非负数!")

    return check_call_func


def deco2(func):
    # 检查func(x, y)中的参数
    def check_call_func(x, y):
        if x >= 0 and y >= 0:
            return func(x, y)
        else:
            print("提示：函数参数必须为非负数!")

    return check_call_func


def deco3(func):
    # 检查func(x, y)中的参数
    def check_call_func(x):
        if x >= 0:
            return func(x)
        else:
            print("提示：函数参数必须为非负数!")

    return check_call_func


# 计算三角形的周长
@deco1
def areaOfTriangle(a, b, c):
    return a + b + c


# 计算矩形的周长
@deco2
def areaOfRectangle(a, b):
    return 2 * (a + b)


# 计算圆的周长
@deco3
def areaOfCircle(r):
    return 2 * pi * r



print(areaOfTriangle(1, 2, 3))
print(areaOfRectangle(1, 2))
print(areaOfCircle(5))
# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/9/10 - 16:25
@file : 16_装饰器.py
@ide : PyCharm
"""


# 什么是装饰器：装饰器是Python函数中一个比较特殊的函数，是用来包装函数的函数，装饰器可以使得程序代码更加简洁
# 什么时候使用装饰器：1. 将多个函数中的重复代码拿出来整理成一个装饰器。对每个函数使用装饰器，从而实现代码的重用
# 2. 对多个函数的共同功能进行处理。例如，先单独写一个检查函数参数合法性的装饰器，然后在每个需要检查函数参数合法性的函数处调用即可


# eg1
def deco(function):
    print("I am in deco.")
    function()
    return "deco return value."


# 使用装饰器修饰函数
@deco
def func():
    print("I am in func.")


# print(func)


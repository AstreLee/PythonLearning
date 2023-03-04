# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/7/31 - 11:46
@file : 07_字符串对齐函数.py
@ide : PyCharm
"""

# 1.ljust()：返回一个左对齐的字符串，多余位置用指定的字符（默认空格）填充
myStr = 'Hello'
print(myStr.ljust(10, '.'))

# 2.rjust()；返回一个右对齐的字符串，多余位置用指定的字符(默认空格)填充
print(myStr.rjust(10, '_'))

# 3.center()：返回一个中间对齐的字符串，多余位置用指定的字符(默认空格)填充
print(myStr.center(10, '+'))

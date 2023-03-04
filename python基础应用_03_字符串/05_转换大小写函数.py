# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/7/31 - 11:17
@file : 05_转换大小写函数.py
@ide : PyCharm
"""

# 首字母大写
myStr = 'hello world'
print(myStr.capitalize())

#  字符串中每个单词首字母大写
myStr = 'hello world python'
print(myStr.title())

# 将字符串中大写字母转化为小写
myStr = 'HeLLo WORLD Python'
print(myStr.lower())

# 将字符串中的小写字母转化为大写
myStr = 'hello world PYTHon'
print(myStr.upper())

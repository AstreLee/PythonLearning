# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/7/31 - 20:41
@file : 02_元组数据查找.py
@ide : PyCharm
"""

tuple1 = ('aa', 'bb', 'cc')
print(tuple1[1])

print(tuple1[1:3])
# tuple2 = tuple1.copy()：元组是没有copy函数，所以不能复制的

print(tuple1.index('cc'))

print(tuple1.count('aa'))

print(len(tuple1))

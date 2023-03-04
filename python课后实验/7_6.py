# -*- coding: utf-8 -*-
"""
@Author : xiaoxinxin
@Date : 2021/10/14 - 16:04
@File : 7_6.py
@IDE : PyCharm
"""


import pandas
import numpy


df = pandas.DataFrame(numpy.arange(9).reshape((3, 3)), index=['A', 'B', 'C'], columns=['one', 'two', 'three'])
print(df[1:2])
print(df[['three', 'one']])

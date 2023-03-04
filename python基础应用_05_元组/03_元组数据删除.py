# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/7/31 - 20:47
@file : 03_元组数据删除.py
@ide : PyCharm
"""


# 元组里面嵌套列表的值是可以进行修改的
tuple2 = ('aaa', 'bbb', 'ccc', ['123', '456'], 'ddd')
print(tuple2[3][1])
tuple2[3][1] = '8910'
print(tuple2[3][1])

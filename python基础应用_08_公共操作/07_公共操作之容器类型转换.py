# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/8/1 - 11:42
@file : 07_公共操作之容器类型转换.py
@ide : PyCharm
"""

list1 = [10, 20, 30, 40, 50]
tuple1 = (1, 2, 2, 3, 4, 5)
set1 = {1, 2, 3, 4, 5}
# tuple()函数
print(tuple(list1))
print(tuple(set1))

# list()函数
# 多余的数据会自动去掉
print(list(tuple1))
print(list(set1))

# set()函数
print(set(list1))
print(set(tuple1))

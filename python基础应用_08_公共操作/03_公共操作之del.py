# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/8/1 - 11:17
@file : 03_公共操作之del.py
@ide : PyCharm
"""

str_1 = 'abcdefg'
list_1 = [10, 20, 30, 40, 50]
tuple_1 = (10, 20, 30, 40, 50)
set_1 = {10, 20, 30, 40, 50}
dict_1 = {'name': 'TOM', 'age': 20, 'address': 'HuBei province'}

del str_1
print(str_1)
print(str_1[2])  # 字符串是不可变数据类型嗷~，这样写是不对的

del list_1
print(list_1)
del list_1[2]
print(list_1[2])

del tuple_1
print(tuple_1)

del set_1
print(set_1)

del dict_1
print(dict_1)
del dict_1['name']
print(dict_1)


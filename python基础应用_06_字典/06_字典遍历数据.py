# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/8/1 - 9:54
@file : 06_字典遍历数据.py
@ide : PyCharm
"""

dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
# 1.遍历字典的所有key值
for key in dict1.keys():
    print(key)

# 2.遍历字典序列中所有的键值values
for value in dict1.values():
    print(value)

# 3.遍历字典中所有的键值对
for item in dict1.items():
    print(item)

# 4.遍历字典中所有的键值对，并且进行拆包
for key, value in dict1.items():
    print(f'{key} = {value}')




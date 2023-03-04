# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/7/31 - 21:25
@file : 03_字典删除数据.py
@ide : PyCharm
"""

dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
# del 删除字典或指定的键值对
# del dict1
# print(dict1)

# del 删除指定的键值对
# del dict1['name']  # key存在才可以删除，不存在的话会报错
# print(dict1)

# clear 清空字典  # 清空与删除是有区别的，清空会保留一个空壳，但是删除啥都没有了
dict1.clear()
print(dict1)

# dict.pop(key)：删除关键字为key的元素
dict2 = {'name': 'Tom', 'age': 20, 'gender': '男'}
dict2.pop('name')
print(dict2)

# dict.popitem()：随机删除字典中的元素
dict3 = {'name': 'Tom', 'age': 20, 'gender': '男'}
dict3.popitem()
print(dict3)


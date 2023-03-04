# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/7/31 - 21:38
@file : 05_字典查找数据.py
@ide : PyCharm
"""

dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
# 1.按照key值进行查找 [key] -- key存在，返回键值；key不存在，报错
# print(dict1['name'])
# print(dict1['names'])


# 2.函数查找
# 2.1 get()函数
print(dict1.get('name'))  # TOM
print(dict1.get('names'))  # 不存在,返回None
print(dict1.get('names', 123))  # 不存在，返回默认值123

# 2.2 keys()函数
print(dict1.keys())  # 查找字典中所有的key值，返回可以迭代的对象

# 2.3 values()函数
print(dict1.values())  # 查找字典中所有key对应的键值，返回可以迭代的对象

# 2.4 items()函数  # 查找字典中所有的键值对，返回可迭代对象，里面的数据是元组，元组数据1是字典的key，元组数据2是对应的键值
print(dict1.items())

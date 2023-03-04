# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/8/1 - 15:42
@file : 04_字典推导式.py
@ide : PyCharm
"""

# 1.创建一个字典：字典key是1-5数字,value是这个数字的2次方
# 1.1 for循环实现
dict1 = dict()
for i in range(1, 6):
    dict1[i] = i ** 2
print(dict1)

# 1.2 while循环实现
dict4 = dict()
i = 1
while i <= 5:
    dict4[i] = i * i
    i += 1
print(dict4)

# 1.3 字典推导式实现
dict2 = {i: i ** 2 for i in range(1, 6)}
print(dict2)

# 2.将两个列表快速合并成为一个字典
# 2.1 for循环实现
dict3 = {}
list1 = ['name', 'age', 'address']
list2 = ['Tom', 19, '湖北省黄冈市']
i = 0
for i in range(3):
    dict3[list1[i]] = list2[i]
print(dict3)

# 2.2 while循环实现
dict5 = {}
i = 0
while i < 3:
    dict5[list1[i]] = list2[i]
    i += 1
print(dict5)

# 2.3 字典推导式实现
dict6 = {list1[i]: list2[i] for i in range(len(list1))}
print(dict6)


# 2.4 提取字典中的目标数据
counts = {'MBP': 268, 'HP': 125, 'DELL': 201, 'LENOVO': 199, 'acer': 99}
dict7 = {key: value for key, value in counts.items() if value >= 200}
print(dict7)

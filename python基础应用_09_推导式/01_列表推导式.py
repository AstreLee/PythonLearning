# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/8/1 - 15:20
@file : 01_列表推导式.py
@ide : PyCharm
"""

# 对比以下三种种方式
# 方式一:while循环
list1 = []
i = 0
while i < 10:
    list1.append(i)
    i += 1
print(list1)

# 方式二:for循环实现
list2 = []
for i in range(10):
    list2.append(i)
print(list2)

# 方式三:列表推导式实现
list3 = [i for i in range(10)]  # 这就是一个列表推导式，创建有规律的列表，简化代码很方便
print(list3)

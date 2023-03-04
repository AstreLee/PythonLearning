# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/8/1 - 15:27
@file : 02_列表推导式带if.py
@ide : PyCharm
"""


# 创建0~10的偶数列表（包括10）
# 不带if
list1 = [i for i in range(0, 11, 2)]
print(list1)

# 带if
list2 = [i for i in range(11) if i % 2 == 0]
print(list2)

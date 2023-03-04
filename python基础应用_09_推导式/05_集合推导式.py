# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/8/1 - 19:16
@file : 05_集合推导式.py
@ide : PyCharm
"""

set1 = {1, 2, 3, 1}
set2 = {i ** 2 for i in set1}
print(set2)

# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/9/9 - 22:01
@file : 05_集合运算.py
@ide : PyCharm
"""

# 1. set1.union(set2) 或 set1 | set2 ：并集运算，结果为在set1和set2中所有的元素
set1 = {1, 2, 3}
set2 = {4, 5, 6}
print(set1.union(set2))
print(set1 | set2)

# 2. set1.intersection(set2) 或 set1 & set2：交集运算，结果为set1中和set2中同时出现的元素
set3 = {1, 2, 3, 4, 5, 6}
set4 = {1, 3, 5}
print(set3.intersection(set4))
print(set3 & set4)

# 3. set1.difference(set2) 或 set1 - set2：差集运算，结果为在集合set1中但是不在set2中
set5 = {1, 2, 3, 4, 5, 6}
set6 = {1, 2, 3}
print(set5.difference(set6))
print(set5 - set6)

# 4. set1.issubset(set2) 或 set1 < set2：子集运算，如果集合set1是set2的子集的话，返回True，否则返回False
set7 = {1, 2, 3}
set8 = {1, 2, 3, 4, 5, 6}
print(set7.issubset(set8))
print(set7 < set8)

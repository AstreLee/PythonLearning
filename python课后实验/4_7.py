# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/9/17 - 20:08
@file : 4_7.py
@ide : PyCharm
"""


set1 = {2, 5, 9, 1, 3}
set2 = {3, 6, 8, 2, 5}

# 1. 向set1中添加一个新的元素7
set1.add(7)

# 2. 求set1和set2的并集
print("set1与set2的交集为：", set1.union(set2))

# 3. 求set1与set2的交集
print("set1与set2的交集为：", set1.intersection(set2))

# 4. 求set1与set2的差集
print("set1与set2的差集为：", set1.difference(set2))

# 5. 判断所给关键字key=4是否在set1中或set2中
if 4 in set1 | set2:
    print("4在set1或set2中")
else:
    print("4不在set1或set2中")


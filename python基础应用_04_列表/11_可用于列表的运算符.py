# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/9/9 - 20:27
@file : 11_可用于列表的运算符.py
@ide : PyCharm
"""

# 1. + ：用于连接两个列表
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(list1 + list2)

# 2. * ：用于重复显示列表
print(list1 * 3)

# 3. in & not in ：用于判断里面是否有相应的元素，返回bool值
print(1 in list1)
print(4 not in list1)

# 4. 关系运算符：从列表的第一个元素开始比较，如果有结果的话则返回bool值，没有结果的话就依次往后面比较
print(list1 > list2)

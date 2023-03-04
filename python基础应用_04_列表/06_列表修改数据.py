# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/7/31 - 19:15
@file : 06_列表修改数据.py
@ide : PyCharm
"""

nameList = ['TOM', 'LILY', 'ROSE']

# 1.修改指定下标处的元素
nameList[0] = 'aaa'
print(nameList)

# 2.通过切片修改指定范围的列表的数据
nameList[len(nameList):] = ['Jerry', 'Lily']
nameList[1:4] = ["a", "b", "c"]
print(nameList)

# 2.逆序排列
list1 = [1, 2, 3, 4, 5, 6]
list1.reverse()
print(list1)


# 3.sort()排序
list2 = [1, 3, 2, 6, 4, 8, 4]
list2.sort(reverse=True)  # 降序
list2.sort(reverse=False)  # 升序(默认)
print(list2)

# 4. sorted(列表)：对列表中的元素临时排序，返回一个副本，原有的列表元素次序不变
list3 = [1, 3, 2, 6, 5, 3, 1, 2]
print(sorted(list3))
print(list3)

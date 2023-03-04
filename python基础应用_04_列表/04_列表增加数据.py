# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/7/31 - 18:01
@file : 04_列表增加数据.py
@ide : PyCharm
"""

# 1.append()函数
nameList1 = ['TOM', 'ROSE', 'LILY', 'Jack']
print(nameList1)
nameList1.append([11, 20])
print(nameList1)  # append()函数追加数据的时候如果是一整个序列的话，那么整个序列都会追加到列表的结尾
print(nameList1[4][0])  # 这就相当于一个二维数组了

# 2.extend()函数
nameList2 = ['TOM', 'ROSE', 'LILY']
nameList2.extend('xiaoming')
print(nameList2)
nameList2.extend(['xiaoming', 'xiaojun'])
print(nameList2)  # 这个时候加上去的才是两个人名

# 3.insert()函数
nameList3 = ['TOM', 'ROSE', 'LILY']
nameList3.insert(1, '123')
print(nameList3)

# 4. 使用切片在指定的位置进行添加
list1 = ["January", "February", "March"]
list1[3:] = ["April", "May"]
print(list1)


# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/7/31 - 17:38
@file : 01_列表访问.py
@ide : PyCharm
"""

"""
列表初探：
1. 什么是列表：列表是写在[]里面，用逗号隔开的元素集合，使用频繁，灵活性好
2. 列表里面可以什么都没有，这样的列表我们称为空列表
3. 列表中的元素可以相同可以不同，类型可以一致也可以不一致(里面可以嵌套列表等组合数据类型)
4. 列表和字符串一样支持正向索引和反向索引
"""

# 创建列表的两种方式：1. 使用[]创建；2. 使用list()函数创建(但是这里面的形参只能有一个)
list1 = list(("a", "b", "c"))
list2 = list(['a', 1, (1, 2, 3), "abc"])
list3 = list({1, 2, 3, 3, 4, 5, 6})
list4 = list({"name": "Tom", "age": 19, "sex": "男"})
list5 = list(range(10))
print(list1)
print(list2)
print(list3)
print(list4)  # 这里只会打印key的值
print(list5)

# 1.下标访问，与c系语言类似
nameList = ['Tom', 'Lily', 'Rose']
print(nameList[0])
print(nameList[1])
print(nameList[2])

# 2. 列表切片，和字符串一样

# 2.函数访问统计
# 2.1:index()函数  列表序列.index(要查找的字符串，开始位置对应下标，结束位置对应下标)
print(nameList.index('Tom'))   # 0
# print(nameList.index('TOM'))  # 报错

# 2.2:count()函数 列表序列.count(要查找的字符串，开始位置对应下标，结束位置对应下标)
print(nameList.count('Tom'))  # 1
print(nameList.count('TOM'))  # 0

# 2.3:len()函数 len(序列名)
print(len(nameList))  # 3

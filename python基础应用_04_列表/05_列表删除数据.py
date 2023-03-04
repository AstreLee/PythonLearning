# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/7/31 - 18:58
@file : 05_列表删除数据.py
@ide : PyCharm
"""

nameList = ['TOM', 'Lily', 'Rose']
# 1.del函数
# del nameList  # 不带括号
# del (nameList)  # 带括号
# print(nameList)
# del也可以删除指定下标的字符
# del nameList[0]
# print(nameList)



# 2.pop()函数：-- 删除指定下标处的数据，如果没有指定下标的话，默认删除最后一个数据
# 不论删除的是指定下标处的数据还是最后一个数据，pop()函数都会返回被删除的数据
# del_name = nameList.pop(1)
# print(del_name)
# print(nameList)



# 3.remove()函数
# nameList.remove('TOM')
# print(nameList)


# 4.clear()函数
# nameList.clear()
# print(nameList)


# 5.切片删除
# nameList[1:] = []

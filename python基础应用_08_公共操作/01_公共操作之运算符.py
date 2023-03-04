# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/8/1 - 10:52
@file : 01_公共操作之运算符.py
@ide : PyCharm
"""
str1 = 'aa'
str2 = 'bb'

list1 = [1, 2]
list2 = [3, 4]

tup1 = (1, 2)
tup2 = (3, 4)

dict1 = {'name': 'TOM'}
dict2 = {'age': 20}

set1 = {1, 2}
set2 = {3, 4}


# 1. + (运算符两侧必须是相同的类型)
print(str1 + str2)
print(list2 + list1)
print(tup1 + tup2)
# print(set1 + set2)  # 报错
# print(dict1 + dict2)  # 报错


# 2. *
print(str1 * 5)
print('-' * 10)
print(list1 * 10)
print(tup1 * 10)



# 3. in
print('a' in str1)
print('b' in str1)
print('a' not in str1)
print('b' not in str1)

print(1 in list1)
print(3 in list1)
print(1 not in list1)
print(3 not in list1)

print(1 in tup1)
print(3 not in tup1)
print(1 not in tup1)
print(3 not in tup1)

print('name' in dict1)
print('name' not in dict1)
print('name' in dict1.keys())
print('name' in dict1.values())

print(1 in set1)
print(2 in set1)


# 4. 关系运算符:除了可以使用关系运算符比较两个字符串以外，还可以使用标准库模块Operator中的函数比较

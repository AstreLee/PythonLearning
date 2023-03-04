# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/9/17 - 19:45
@file : 4_4.py
@ide : PyCharm
"""


# 方式一
number = int(input("请输入您想生成的列表中的元素个数："))
print(f'请依次输入这{number}个数：')
list1 = []
for i in range(number):
    a = int(input(f"请输入第{i + 1}个数："))
    for j in list1:
        if j == a:
            break
    else:
        list1.append(a)
print(list1)


# 方式二
number1 = int(input("请输入您想生成的列表中的元素个数："))
print(f'请依次输入这{number1}个数：')
list2 = []
for i in range(number1):
    a = int(input(f"请输入第{i + 1}个数："))
    list2.append(a)
list3 = list(set(list2))
print(list3)


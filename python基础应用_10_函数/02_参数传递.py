# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/8/1 - 19:54
@file : 02_参数传递.py
@ide : PyCharm
"""


# Python中的参数传递有两种情况
# 1. 实参为不可变对象(数字，字符串，元组)：函数调用的时候是将实参的值复制一份传递给形参
# 2. 实参为可变对象(列表，集合，字典)：函数调用的时候是将实参的引用复制一份给形参


def Swap(x, y):
    x, y = y, x


a = 1
b = 2
print("交互前：a =", a, ",b =", b)
Swap(a, b)
print("交换后：a =", a, ",b =", b)



def Swap(myList):
    myList.append(4)


list1 = [1, 2, 3]
print("调用前：", list1)
Swap(list1)
print("调用后：", list1)

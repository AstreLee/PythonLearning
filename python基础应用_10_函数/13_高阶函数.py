# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/8/4 - 19:57
@file : 13_高阶函数.py
@ide : PyCharm
"""


# 所谓高阶函数，就是把函数作为参数进行传递
def sum(a, b, f):
    """对两个数按照指定的方式进行求和"""
    return f(a) + f(b)


print(sum(1.9, 2.4, abs))


# 1.map()函数
def fun1(x):
    return x ** 2


list1 = [1, 2, 3, 4]
result = map(fun1, list1)
print(result)  # 打印的是这个列表的地址
print(list(result))  # 打印列表


# 2.reduce()函数
import functools
list2 = [1, 2, 3, 4, 5]


def fun2(a, b):
    return a + b


result = functools.reduce(fun2, list2)
print(result)


# 3.filter()函数
list3 = [2, 3, 4, 6, 8, 10]
def fun4(x):
    if x % 2 == 0:
        return x


result = filter(fun4, list3)
print(result)
print(list(result))



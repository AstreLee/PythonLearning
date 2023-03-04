# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/8/4 - 10:54
@file : 09_拆包.py
@ide : PyCharm
"""


# 元组拆包
def return_num():
    return 100, 200  # 返回的是一个元组


result = return_num()
print(result)
num1, num2 = return_num()
print(num1)
print(num2)


# 字典拆包
dict1 = {'name': 'Tom', 'age': 19}
a, b = dict1
print(a)
print(b)
# 字典拆包得到的是keys值

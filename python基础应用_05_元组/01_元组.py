# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/7/31 - 20:21
@file : 01_元组.py
@ide : PyCharm
"""

# 创建元组的两个方式
# 1. 使用()运算符
tuple1 = (1, 2, 3)
# 2. 使用tuple()函数
tuple2 = tuple([1, 2, 3])
print(tuple2)
tuple3 = tuple((1, 2, 3))
print(tuple3)
tuple4 = tuple({1, 2, 2, 3, 4, 4, 4, 5, 6})
print(tuple4)
tuple5 = tuple({"name": "Tom", "age": 16, "sex": "男"})
print(tuple5)  # 同样只打印key值

t1 = (10, 20, 30)
print(type(t1))
t2 = (10,)  # 逗号不要忘
print(type(t2))
t3 = ('aaa',)  # 逗号不要忘
print(type(t3))

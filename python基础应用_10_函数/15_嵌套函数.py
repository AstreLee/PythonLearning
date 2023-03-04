# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/9/10 - 16:01
@file : 15_嵌套函数.py
@ide : PyCharm
"""


# 定义外函数
def outerFunc(x):
    # 定义内函数
    def innerFunc(y):
        return x * y
    return innerFunc


print("方法一调用结果：", outerFunc(3)(4))  # 在调用函数的时候传递外函数参数和内函数参数
a = outerFunc(3)  # 调用外函数，传递外函数参数，此时a相当于一个外函数
print("方法二调用结果：", a(4))  # 间接调用内函数，传递内函数参数

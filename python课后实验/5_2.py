# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/9/17 - 20:29
@file : 5_2.py
@ide : PyCharm
"""


# 计算斐波那契数列指定的项数(递归函数实现)
def Fib(n):
    if n < 1:
        print("传入项数有误!")
    elif n == 1 or n == 2:
        return 1
    else:
        return Fib(n - 1) + Fib(n - 2)


# 计算斐波那契数列前十项和
def FibSum(n):
    a = 1
    b = 1
    sumFib = a + b
    for i in range(n - 2):
        b = a + b
        a = b - a
        sumFib += b
    return sumFib


a = int(input("请输入斐波那契数列的项数："))
print(f'斐波那契数列第{a}项为：', Fib(a))
print("斐波那契数列第十项为：", FibSum(10))

# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/8/1 - 20:22
@file : 05_函数嵌套调用实例.py
@ide : PyCharm
"""


# 打印一条横线
def print_line():
    print('-' * 20)


print_line()


# 打印多条横线
def print_lines(num):
    i = 0
    while i < num:
        print_line()
        i += 1


num = int(input('请输入你想打印的横线的条数：'))
print_lines(num)


# 实现三个数求平均值
def sum_three(a, b, c):
    return a + b + c


def aver_three(a, b, c):
    sum = sum_three(a, b, c)
    return sum / 3  # python除法一定得到浮点数


aver = aver_three(1, 2, 3)
print(aver)

# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/9/16 - 22:25
@file : 3_2.py
@ide : PyCharm
"""


a = int(input("请输入一个不多于5位的整数："))
b = a
count = 0
print("倒序输出为：")
while True:
    if b % 10 == 0:
        break
    else:
        print(b % 10, end="")
        b //= 10
        count += 1
print()
print(f'{a}数字共有{count}位数')

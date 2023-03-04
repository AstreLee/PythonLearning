# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/9/16 - 22:59
@file : 3_8.py
@ide : PyCharm
"""


rows = int(input("请输入您想生成的菱形的行数："))
for i in range(rows // 2 + 1):
    print(' ' * ((rows // 2 - i)*2), end="")
    for j in range(2*i + 1):
        print("*", end=" ")
    print()

for i in range(rows // 2):
    print(' ' * (2*i + 2), end="")
    for j in range(2*(rows // 2 - i) - 1):
        print("*", end=" ")
    print()



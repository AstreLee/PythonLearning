# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/9/16 - 22:19
@file : 3_1.py
@ide : PyCharm
"""


a = float(input("请输入a的值："))
b = float(input("请输入b的值："))
c = float(input("请输入c的值："))
if a > b:
    if a < c:
        print(f'{c} > {a} > {b}')
    else:
        if b < c:
            print(f'{a} > {c} > {b}')
        else:
            print(f'{a} > {b} > {c}')
else:
    if c > b:
        print(f'{c} > {b} > {a}')
    else:
        if c < a:
            print(f'{b} > {a} > {c}')
        else:
            print(f'{b} > {c} > {a}')

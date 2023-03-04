# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/8/1 - 11:36
@file : 06_公共操作之enumerate.py
@ide : PyCharm
"""

list1 = [10, 20, 30, 40, 50]
for i in enumerate(list1):  # 没有指定start的初始值，所以默认下标是从0开始的
    print(i, end=' ')
print()
for i in enumerate(list1, start=1):
    print(i, end=' ')

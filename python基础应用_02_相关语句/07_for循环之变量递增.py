# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/7/31 - 9:00
@file : 07_for循环之变量递增.py
@ide : PyCharm
"""

# for 循环中循环变量会自动递增,无需手动添加递增，并且循环控制变量在循环结束后依然存在
str = [10, 20, 30, 40, 50]
for i in str:
    print(i, end=' ')
print()
print(i)  # 50


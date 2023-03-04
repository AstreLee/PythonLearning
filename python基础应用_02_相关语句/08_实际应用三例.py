# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/7/30 - 18:46
@file : 08_实际应用三例.py
@ide : PyCharm
"""

# 打印正方形
j = 0
while j < 5:
    i = 0
    while i < 5:
        print('*', end=' ')
        i += 1
    print()
    # 空的print语句，目的就是想使用print默认的一个换行符
    # 如果是print('\n')的话换的就是两行了
    j += 1


# 打印三角形
j = 0
while j < 6:
    i = 0
    k = j
    while 6 - k > 0:
        print(' ', end='')  # 取消换行的实操
        k += 1
    while i < 2 * j + 1:
        print('*', end=' ')
        i += 1
    print()
    j += 1


# 打印99乘法表
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f'{j}*{i}={i * j} ', end='')  # 取消自动换行
        j += 1
    i += 1
    print()

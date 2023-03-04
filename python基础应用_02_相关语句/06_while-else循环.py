# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/7/31 - 8:37
@file : 06_while-else循环.py
@ide : PyCharm
"""

# while - else循环正常结束
i = 0
while i < 5:
    if i == 3:
        break
    else:
        print('abc')
        i += 1
else:
    print('循环正常结束的时候所执行的代码')

# while - else循环非正常结束 -- break
i = 0
while i < 5:
    print('ABC')
    i += 1
else:
    print('循环正常结束的时候所执行的代码')

# while - else循环之continue
i = 0
while i < 5:
    if i == 2:
        i += 1
        continue
    else:
        print('123')
        i += 1  # 循环控制变量不会自动递增
else:
    print('continue executive')  # 可以正常执行的

# for - else循环正常结束
str = 'itheima'
for i in str:
    print(i, end='')  # 循环控制变量自动递增
else:
    print('循环正常结束时所执行的代码')

# for - else循环非正常结束之break
for j in str:
    if j == 'e':
        break
    else:
        print(j, end='')
else:
    print('程序正常执行的时候执行这条语句')


# while的循环控制变量需要人为进行递增控制
# for的循环控制变量可以自己递增，不需要人为的再来自增一次
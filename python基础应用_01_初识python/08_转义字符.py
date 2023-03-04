# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/7/30 - 10:59
@file : 08_转义字符.py
@ide : PyCharm
"""

print('hello')
print('world')

print('hello, python')

# 换行符号\n的使用
print('hello\nworld')

# 水平制表符号的使用
print('\tabcd')

"""
！！！print会自动换行：print('输出的内容', end="\n")
也可以自己设置如：
print('This is a string', end="\n") --->这是默认的
print('This is a string', end="\t") --->这是自己设置的
print('This is a string', end="...") --->这也是自己设置的
"""

# test:
print('This is a string', end="...")  # 这里最好不要空格
print('This is another string', end='\n')




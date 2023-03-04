# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/7/30 - 10:53
@file : 07_f{ }格式输出.py
@ide : PyCharm
"""

# 我的名字是x，今年x岁了
name = 'TOM'
age = 19
print('我的名字是%s，今年%d岁了' % (name, age))  # 常规
print(f'我的名字是{name}, 今年{age}岁了')  # 语法：f'...{}...'
print(f'我的名字是{name}, 明年{age + 1}岁了')

# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/7/31 - 17:58
@file : 03_判断元素存在实例.py
@ide : PyCharm
"""

nameListSystem = ['Tom', 'Lily', 'Rose', 'Jack', 'Jane']
name = input('请输入您的姓名：')
if name in nameListSystem:
    print(f'您的姓名为{name}，此用户已经注册')
else:
    print('您的姓名为%s，可以进行注册' % name)

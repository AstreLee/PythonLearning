# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/8/5 - 11:19
@file : 07_del()函数.py
@ide : PyCharm
"""


class TestDel:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __del__(self):
        print(f'{self}对象已经删除')


object1 = TestDel(100, 200)
del object1



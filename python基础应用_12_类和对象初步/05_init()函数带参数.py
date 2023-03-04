# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/8/5 - 10:58
@file : 05_init()函数带参数.py
@ide : PyCharm
"""


class TestInit:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def printInfo(self, argument):
        print(f'类成员函数接收一个参数:{argument}')


object1 = TestInit(100, 200, 300)
print(object1.length, object1.width, object1.height)
object1.printInfo(999)


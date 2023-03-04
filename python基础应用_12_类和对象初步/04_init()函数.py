# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/8/5 - 10:45
@file : 04_init()函数.py
@ide : PyCharm
"""


class TestInit:
    def __init__(self):
        self.length = 100
        self.width = 200
        self.height = 300

    def printInfo(self):
        print(f'长:{self.length}, 宽:{self.width},高:{self.height}')


object1 = TestInit()
print(object1.length)
object1.printInfo()
# 这个self不就是c++中隐含的this指针嘛

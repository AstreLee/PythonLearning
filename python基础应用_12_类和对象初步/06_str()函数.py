# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/8/5 - 11:12
@file : 06_str()函数.py
@ide : PyCharm
"""


class TestStr:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def __str__(self):
        return '这是str()函数测试'


object1 = TestStr(100, 200, 300)
print(object1)


class TestStr1:
    def fun1(self):
        print("I'm so handsome!")


object2 = TestStr1()
print(object2)


# 没有定义str()函数的话，打印对象名得到的就是对象的地址
# 定义了str()函数的话，打印对象名得到的就是str()函数的返回信息


# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/8/5 - 14:15
@file : 02_多继承.py
@ide : PyCharm
"""


class A:
    """这是A类的说明"""
    def __init__(self):
        self.name = 'Tom'
        self.age = 19

    def printInfo(self):
        print(f'名字是{self.name}, 年龄是{self.age}')


class B:
    """这是B类的说明"""
    def __init__(self):
        self.name = 'Jack'
        self.age = 20

    def printInfo(self):
        print(f'名字是{self.name}, 年龄是{self.age}')


class C(A, B):
    """这是A和B类的派生类"""
    def __init__(self):
        self.name = 'Rose'
        self.age = 20

    def printInfo(self):
        print(f'名字是{self.name}, 年龄是{self.age}')
# 在子类对父类中的同名属性或方法进行修改，默认调用子类的函数


Ctest = C()
Ctest.printInfo()

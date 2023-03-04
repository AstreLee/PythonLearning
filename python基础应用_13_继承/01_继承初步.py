# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/8/5 - 13:50
@file : 01_继承初步.py
@ide : PyCharm
"""


class A:
    def __init__(self):
        self.name = 'Tom'
        self.age = 19
        self.gender = '男'

    def printInfo(self):
        print(f'name:{self.name}, age:{self.age}, gender:{self.gender}')


class B(A):
    def __init__(self):
        self.name = 'Jack'
        self.age = 21
        self.gender = '男'

    def printInfo(self):
        print(f'name:{self.name}, age:{self.age}, gender:{self.gender}')


Btest = B()
Btest.printInfo()

# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/8/5 - 15:46
@file : 03_mro()函数.py
@ide : PyCharm
"""


class A(object):
    def fun_A(self):
        print('这是父类中的打印语句')


class B(A):
    def fun_B(self):
        print('这是子类中的打印语句')


class C(B):
    def fun_C(self):
        print('这是C类中的打印语句')


print(C.__mro__)
# __mro__用来查看子类与其所有父类之间的关系

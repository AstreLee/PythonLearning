# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/8/1 - 21:14
@file : 06_函数之局部全局变量.py
@ide : PyCharm
"""

a = 100


def testA():
    print(a)


def testB():
    a = 200  # 这里的a是局部的，修改a的值并不会影响全局变量的值
    print(a)


testA()
testB()


def testC():
    global a  # 加关键字global就可以访问全局变量
    a = 200
    print(a)


testC()
print(a)
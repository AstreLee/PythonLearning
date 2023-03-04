# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/8/1 - 20:19
@file : 04_函数嵌套调用.py
@ide : PyCharm
"""


def testB():
    print('------ testB start ------')
    print('Here is testB')
    print('------ testB end ------')


def testA():
    print('------ testA start ------')
    print('Here is testA')
    print('------ testA end ------')
    testB()


testA()

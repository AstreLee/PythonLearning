# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/8/4 - 20:55
@file : 01_类和对象的创建.py
@ide : PyCharm
"""


# 注意类名的创建遵循大驼峰的规则
class Washer:
    def wash(self):
        print('第一个成员函数')


object1 = Washer()
object1.wash()

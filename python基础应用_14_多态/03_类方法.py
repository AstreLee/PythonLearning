# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/8/6 - 10:48
@file : 03_类方法.py
@ide : PyCharm
"""


class A(object):
    __num = 111

    @classmethod  # 定义类方法，一般与类属性配合使用
    def get_num(cls):
        print(cls.__num)
        return cls.__num

    @staticmethod  # 定义静态方法，可以省略self, cls等指针，类和对象都可以进行调用，很方便
    def work():
        print('hahaha')


object1 = A()
print(object1.get_num())
object1.work()  # 对象名进行调用
A.work()  # 类名进行调用


# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/8/5 - 20:24
@file : 06_私有属性.py
@ide : PyCharm
"""


class Master(object):
    def __init__(self):
        self.__word = [1, 2, 3]
        self.__money = 20000
        print('Master初始化调用')

    def get_money(self):
        return self.__money

    def set_money(self):
        self.__money = 10000
        return self.__money


class School(Master):
    def __init__(self):
        super().__init__()
        self.word = [4, 5, 6]
        print('School初始化调用')


# object1 = School()
# object2 = Master()
# print(object2.__word)
# print(object1.__word)
object1 = Master()
print(object1.get_money())
print(object1.set_money())



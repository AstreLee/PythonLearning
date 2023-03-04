# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/8/5 - 12:04
@file : 02_烤土豆实例.py
@ide : PyCharm
"""


class Potato:
    def __init__(self):
        """初始化数据成员函数"""
        self.cook_time = 0
        self.cook_state = 'raw'
        self.cook_condiment = []

    def CookState(self, time):
        """时间控制状态函数"""
        self.cook_time += time
        if 0 <= self.cook_time < 3:
            self.cook_state = 'raw'
        elif 3 <= self.cook_time < 5:
            self.cook_state = 'raw and ripe'
        elif 5 <= self.cook_time < 8:
            self.cook_state = 'ripe'
        else:
            self.cook_state = 'paste'

    def CookCondiment(self, condiment):
        """添加调料函数"""
        self.cook_condiment.append(condiment)

    def __str__(self):
        """显示信息函数"""
        return f'The current baking time is {self.cook_time} minutes\n' \
               f'The current baking state is {self.cook_state}\n' \
               f'The condiment added to the Potato are {self.cook_condiment}'


object1 = Potato()
object1.CookState(2)
print(object1)
object1.CookState(2)
print(object1)
object1.CookCondiment('酱油')
print(object1)
object1.CookState(8)
print(object1)
help(object1.CookCondiment)

# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/8/6 - 9:47
@file : 01_多态初步.py
@ide : PyCharm
"""


class Dog(object):
    def work(self):
        print('这是一只初级狗狗!')


class ArmyDog(Dog):
    def work(self):
        print('这是一只军犬')


class DrugDog(Dog):
    def work(self):
        print('这是一只缉毒犬')


class Police(object):
    def work_for_diff_dog(self, dog):  # 这里的dog是形参，用其它的变量名都是可以的
        print('这里是人民警察，调用具体的犬种')
        dog.work()


police = Police()
police.work_for_diff_dog(ArmyDog())
police.work_for_diff_dog(DrugDog())

# 多态：父类中的方法在不同的派生类中具有不同的表现与行为

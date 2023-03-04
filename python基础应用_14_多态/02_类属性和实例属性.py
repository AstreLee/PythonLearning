# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/8/6 - 10:12
@file : 02_类属性和实例属性.py
@ide : PyCharm
"""


class Dog(object):
    def __init__(self):
        self.num = 111  # 这是实例属性
    teeth = 100  # 这是类属性


# 类属性的访问
object1 = Dog()
object2 = Dog()
print(object1.teeth)  # 通过对象名来访问相应的属性
print(object2.teeth)
print(Dog.teeth)  # 通过类名访问相应的属性，也就是数据成员


# 类属性的修改:注意类属性的修改只能用类名不能用对象名，用对象名的话就是创建一个实例属性了
Dog.teeth = 200
print(Dog.teeth)
print(object1.teeth)
print(object2.teeth)


# 如果用对象名修改会怎么样
object1.teeth = 300
print(Dog.teeth)
print(object1.teeth)
print(object2.teeth)


"""
类属性可以由类名或者对象名进行访问
实例属性只能由对象名进行访问，类名无法访问
"""


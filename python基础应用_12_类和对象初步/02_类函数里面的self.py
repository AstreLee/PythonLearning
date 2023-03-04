# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/8/5 - 9:36
@file : 02_类函数里面的self.py
@ide : PyCharm
"""


# 类里面定义的函数括号里面的self参数就是指代当前调用该函数的对象，类似于c++里面的*this指针
class Test():  # 遵循大驼峰的命名规则
    def testInclass(self):
        print('这是一个类里面的函数')
        print(self)


object1 = Test()
print(object1)
object1.testInclass()
object2 = Test()
print(object2)
object2.testInclass()

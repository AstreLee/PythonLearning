# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/9/14 - 22:34
@file : 04_抽象方法.py
@ide : PyCharm
"""

# Python中一般使用抽象基类来实现抽象类。ABC(abstract base class)主要定义了基本类和最基本的抽象方法，使用抽象基类之前要先导入abc模块
import abc


# 定义抽象类
class People(metaclass=abc.ABCMeta):
    # 定义抽象方法
    @abc.abstractmethod
    def working(self):
        pass


# 定义抽象类People的派生类
class Chinese(People):
    def working(self):
        print("中国人在辛勤的工作!")


c1 = Chinese()
c1.working()

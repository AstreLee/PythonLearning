# -*- coding: utf-8 -*-
"""
@Author : xiaoxinxin
@Date : 2021/9/19 - 13:19
@File : 6_1.py
@IDE : PyCharm
"""


import abc
from math import sqrt, pi


class Shape(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def getArea(self):
        pass

    @abc.abstractmethod
    def getPerimeter(self):
        pass


# 定义Triangle类
class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def getArea(self):
        if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
            halfOfArea = (self.a + self.b + self.c) / 2
            return sqrt(halfOfArea * (halfOfArea - self.a) * (halfOfArea - self.b) * (halfOfArea - self.c))
        else:
            print("该三边无法构成三角形!")

    def getPerimeter(self):
        if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
            return self.a + self.b + self.c
        else:
            print("该三边不能构成三角形!")


class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def getArea(self):
        if self.a >= 0 and self.b >= 0:
            return self.a * self.b
        else:
            print("该三边不能构成三角形!")

    def getPerimeter(self):
        if self.a >= 0 and self.b >= 0:
            return 2*self.a + 2*self.b
        else:
            print("矩形的边长需为非负数!")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def getArea(self):
        if self.radius > 0:
            return pi * self.radius * self.radius
        else:
            print("圆的半径不能小于0!")

    def getPerimeter(self):
        if self.radius > 0:
            return 2 * pi * self.radius
        else:
            print("圆的半径不能为负数!")


# 创建三角形，矩形，圆形的测试类
print("三角形面积：", Triangle(3, 3, 3).getArea())
print("三角形周长：", Triangle(3, 3, 3).getPerimeter())
print("矩形面积：", Rectangle(1, 2).getArea())
print("矩形周长：", Rectangle(1, 2).getPerimeter())
print("圆面积：", Circle(5).getArea())
print("圆周长：", Circle(5).getPerimeter())

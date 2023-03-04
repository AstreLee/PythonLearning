
# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/9/12 - 23:10
@file : 08_类方法.py
@ide : PyCharm
"""

"""
1. 公有方法：名字不以下划线开头，可以在类的外面通过类名或对象名访问(用类名访问的时候注意要传值给self)
2. 私有方法：名字以两个或更多的下划线开头，可以在类的方法中使用self调用，不能再类的外面直接调用(用类名访问的时候注意要传值给self)
3. 静态方法和类方法。静态方法和类方法可以通过类名或者对象名调用，但是不能直接访问属于对象的成员
   ，只能访问属于类的成员，不属于任何对象.相比类方法，静态方法的开销更小，类方法一般以cls作为第一个
   参数表示该类自身，在调用方法的时候不需要为该参数传递值。静态方法用@staticmethod声明，类方法用@classmethod声明
"""


class Test:
    def function_public(self):
        print("在公有方法中调用：", self.__function())
        return "公有方法 'function_public'"

    def __function(self):
        return "私有方法 '__function'"

    @classmethod
    def function_classmethod(cls):
        return "类方法 'function_classmethod'"

    @staticmethod
    def function_staticmethod():
        return "静态方法 'function_staticmethod'"


obj = Test()
print("对象调用：" + obj.function_public())
print("对象调用：" + obj.function_classmethod())
print("对象调用：" + obj.function_staticmethod())
print("类调用：" + Test.function_public(obj))  # 要传递第一个参数self值
print("类调用：" + Test.function_classmethod())
print("类调用：" + Test.function_staticmethod())


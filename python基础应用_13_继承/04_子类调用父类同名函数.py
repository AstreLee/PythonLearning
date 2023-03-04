# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/8/5 - 16:01
@file : 04_子类调用父类同名函数.py
@ide : PyCharm
"""

"""
class A:
    def funA(self):
        print('这是A里面的函数')


class B(A):
    def funB(self):
        A.funA(self)  # 在下一级类中想要调用父类的函数一定要指明类名
        print('这是B里面的函数')


object1 = B()
object1.funB()
"""


# -------------------------------------------

class Master(object):
    def __init__(self):
        self.kongfu = ['九品箭手，天下无双']
        print('master初始化')

    def printInfo(self):
        print(f'Master中的打印信息:{self.kongfu}')


# ------------------------------------------

class School(object):
    def __init__(self):
        self.kongfu = ['华山剑法，天下第一']
        print('school初始化')

    def printInfo(self):
        print(f'School中的打印信息:{self.kongfu}')


# ------------------------------------------

class Practice(Master, School):
    def __init__(self):
        self.kongfu = ['大宗师']
        print('Practice初始化')

    def printInfo(self):
        Practice.__init__(self)  # 如果写成自己调用自己的话就是self.__init__()不需要self参数，因为self前面已经用过了
        print(f'Practice中的打印信息:{self.kongfu}')

    # 想通过子类对象去访问父类中的同名的成员函数，只能和init()函数一起又封装成一个新的函数交给子类对象去调用
    def printInfo_master(self):
        Master.__init__(self)
        Master.printInfo(self)

    def printInfo_school(self):
        School.__init__(self)
        School.printInfo(self)


# ----------------------------------

class Trainee(Practice):
    def __init__(self):
        self.kongfu = ['五竹']
        print('Trainee初始化')

    def printInfo_Trainee(self):
        print(f'Trainee中打印的信息:{self.kongfu}')


# ---------------------------------
object_Pra = Practice()
object_Pra.printInfo()
# now我想通过子类对象访问父类中的同名的成员函数
object_Pra.printInfo_master()
object_Pra.printInfo_school()
object_Pra.printInfo()


object_tudi = Trainee()
object_tudi.printInfo_Trainee()
object_tudi.printInfo()
object_tudi.printInfo_master()
object_tudi.printInfo_school()
object_tudi.printInfo()

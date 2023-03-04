# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/8/7 - 16:20
@file : project_student.py
@ide : PyCharm
"""


class Student(object):
    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel

    def __str__(self):
        return f'name:{self.name}, age:{self.age}, tel:{self.tel}'



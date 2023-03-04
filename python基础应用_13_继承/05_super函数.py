# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/8/5 - 17:10
@file : 05_super函数.py
@ide : PyCharm
"""


# --------------------------------------------

class Master(object):
    def __init__(self):
        self.word = ['九品箭手，天下无双']
        print('Master类体执行初始化')

    def print_123(self):
        print(f'Mater类体返回的信息:{self.word}')


# --------------------------------------------

class School(Master):
    def __init__(self):
        super().__init__()
        self.word = ['华山剑法，天下第一']
        print('School类体执行初始化')

    def print_123(self):
        print(f'School类体返回的信息:{self.word}')
        super().print_123()

    def print_super(self):
        # 方法二
        super().__init__()
        super().print_123()


# --------------------------------------------

class Practice(School):
    def __init__(self):
        super().__init__()
        self.word = ['四大宗师']
        print('Practice类体执行初始化')

    def print_123(self):
        print(f'Practice类体返回的信息:{self.word}')

    def print_Master(self):
        Master.__init__(self)
        Master.print_123(self)

    def print_School(self):
        School.__init__(self)
        School.print_123(self)

    # 访问父类所有同名成员函数
    # 这样做的缺陷：1.如果父类类名变化，则所需要的修改大；2.代码量大，冗余
    def print_Mas_Sch(self):
        Master.__init__(self)
        Master.print_123(self)
        School.__init__(self)
        School.print_123(self)

    def print_super(self):
        # 写法一
        super(Practice, self).__init__()
        super(Practice, self).print_123()


# ------------------------------------

object1 = Practice()
object1.print_Mas_Sch()
object1.print_super()
object2 = School()
object2.print_super()

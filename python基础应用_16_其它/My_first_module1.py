# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/8/7 - 14:28
@file : My_first_module1.py
@ide : PyCharm
"""

from math import sin, pi


def test(a, b):
    print(sin(a) + sin(b))


# 只有在此模块中__name__的值才为__main__，在其他的文件里面的话就是本模块的名字了
if __name__ == '__main__':
    test(pi / 2, pi / 3)


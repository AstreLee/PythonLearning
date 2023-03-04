# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/9/16 - 21:30
@file : 2_1.py
@ide : PyCharm
"""

a = float(input("请输入第一条棱长："))
b = float(input("请输入第二条棱长："))
c = float(input("请输入第三条棱长："))
print(f'长方体的第一条棱长为:{a}，第二条棱长为:{b}，第三条棱长为{c}。')

print("长方体的体积为：%f" % (a * b * c))
print("长方体的面积为：%f" % (2 * a * b + 2 * a * c + 2 * b * c))

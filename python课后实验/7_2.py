# -*- coding: utf-8 -*-
"""
@Author : xiaoxinxin
@Date : 2021/10/14 - 16:00
@File : 7_2.py
@IDE : PyCharm
"""


from datetime import date


d = date.today()
print("今天是第%d年，第%d月，第%d天，第%d周" % (d.year, d.month, d.day, d.day // 7 + 1))
print("今天是周%d" % (d.isoweekday()))

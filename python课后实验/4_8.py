# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/9/17 - 20:14
@file : 4_8.py
@ide : PyCharm
"""


breakfastFee = float(input("请输入小明同学的早餐费用："))
lunchFee = float(input("请输入小明同学中餐的费用："))
dinnerFee = float(input("请输入小明同学的晚餐费用："))
otherFee = float(input("请输入小明同学的其它的费用："))
print(f'小明同学一天的费用为：{breakfastFee + lunchFee + dinnerFee + otherFee}元!')

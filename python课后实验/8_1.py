# -*- coding: utf-8 -*-
"""
@Author : xiaoxinxin
@Date : 2021/11/14 - 20:47
@File : 8_1.py
@IDE : PyCharm
"""

import re
phoneNumber = input("请输入电话号码：")
reg = "^(13\d{9})|(147\d{8})|(15[012356789]\d{8})|(17[0-8]\d{8})|(18[056789]\d{8})$"
pattern = re.compile(reg)
res = pattern.match(phoneNumber)
if res:
    print("这个电话号码合法！")
else:
    print("这个电话号码不合法！")

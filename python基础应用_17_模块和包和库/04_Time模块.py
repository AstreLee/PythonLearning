# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/9/15 - 19:56
@file : 04_Time模块.py
@ide : PyCharm
"""

import time

# 1. time.time()函数：返回至1970-1-1的时间戳(浮点秒数)
print(time.time())

# 2. time.asctime([t])：将一个tuple或者struct_time形式的时间转换成一个表示当地时间的字符串
print(time.asctime())

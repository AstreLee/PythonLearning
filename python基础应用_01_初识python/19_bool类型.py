# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/9/8 - 14:55
@file : 19_bool类型.py
@ide : PyCharm
"""

# 在python中，非0，字符串，列表，元组，集合，字典在进行条件判断的时候都视为真(True)
# 在python中，0，空字符串，空列表，空元组，空集合，空字典在进行条件判断的时候视为假(False)
list1 = [1, 2, 3, 4, 5, 6]
if list1:
    print("list1非空")

# 在python中,bool值如果参与了运算的话，True被当做1，False被当做0
print(True + 1)
print(False + 1)

# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/8/1 - 10:26
@file : 03_集合删除数据.py
@ide : PyCharm
"""

s1 = {10, 20, 30, 40, 50}
# 1.remove()函数
# s1.remove(10)
# print(s1)
# s1.remove(60)  # 60不存在，报错
# print(s1)


# 2.discard()函数
# s1.discard(10)
# print(s1)
# s1.discard(10)  # 删除的数据不存在也不会报错，而是不作为
# print(s1)

# 3.pop()函数
del_num = s1.pop()
print(del_num)

# 4. clear()函数
s1.clear()
print(s1)  # set()

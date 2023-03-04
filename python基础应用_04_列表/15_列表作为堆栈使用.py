# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/9/10 - 14:50
@file : 15_列表作为堆栈使用.py
@ide : PyCharm
"""

# 列表方法可以使得列表很方便的作为堆栈使用，先进来的元素后出栈，后进来的元素先出栈。用append方法
# 可以把一个元素添加到堆栈顶，用pop()方法可以把一个元素从堆栈顶释放出来
list1 = []
list1.append(1)
list1.append(2)
list1.append(3)
print(list1.pop())
print(list1.pop())
print(list1.pop())

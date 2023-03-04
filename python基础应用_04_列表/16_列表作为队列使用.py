# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/9/10 - 15:00
@file : 16_列表作为队列使用.py
@ide : PyCharm
"""

# 列表也可以作为队列使用，先加入的元素先出队列，后加入的元素后出队列。
# 在Python中，要将列表作为队列使用，需要先导入collections模块中的deque类，然后创建deque类的对象
# 并将列表作为参数

from collections import deque


q = deque(["a", "b", "c"])
q.append("d")
q.append("e")
print(q.popleft())
print(q.popleft())
print(q)

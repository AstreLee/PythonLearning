# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/9/15 - 19:29
@file : 03_Random模块.py
@ide : PyCharm
"""


import random


# 1. random.random()函数随机生成一个[0, 1)之间的浮点数
print("**************************************")
for i in range(5):
    print(random.random())
print("**************************************")

# 2. random.uniform(a, b)函数生成一个指定范围内的随机浮点数
# 两个参数a, b一个是上限，一个是下限，若a < b则生成的随机数在[a, b]范围内。如果a > b则生成
# 的随机数在[b, a]之间
print(random.uniform(1, 3))
print(random.uniform(3, 2))
print("*************************************")

# 3. random.randint(a, b)函数生成一个指定范围内的整数，生成的随机整数为[a, b]
for i in range(5):
    print(random.randint(1, 2))
print("*************************************")


# 4. random.randrange(a, b)函数用于生成指定范围，指定步长的随机整数
for i in range(5):
    print(random.randrange(1, 10, 1))
print("************************************")


# 5. random.choice(sequence)函数是从指定的序列中随机获取一个随机元素
print(random.choice([i for i in range(10) if i % 2 != 0]))
print("***********************************")


# 6. random.shuffle(sequence)函数是将一个序列对象中的元素打乱
list1 = [1, 2, 3, 4, 5, 6]
random.shuffle(list1)
print(list1)


# 7. random.sample()
print("**********************************")
print(random.sample([i for i in range(10)], 3))



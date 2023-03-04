# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/9/17 - 19:58
@file : 4_6.py
@ide : PyCharm
"""


grade = (68, 87, 83, 91, 93, 79, 68, 86, 66, 78)
# 1. 输出grade中的第二个元素
print(grade[1])

# 2. 输出grade中的第3~7个元素
print(grade[2:7])

# 3. 使用in查询grade中是否包含成绩87
if 87 in grade:
    print("成绩中有87分!")
else:
    print("成绩中没有87分!")

# 4. 调用index()函数在grade中查找给定成绩为78的学生学号
print("成绩为78分的学生的学号为：", grade.index(78) + 1)

# 5. 调用count()函数在grade中查找成绩68出现的次数
print("成绩68出现的次数为：", grade.count(68))

# 6. 使用len()函数获取grade中的元素的个数
print("grade中的元素个数为：", len(grade))

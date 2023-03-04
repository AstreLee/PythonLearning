# -*- coding: utf-8 -*-
"""
@author : xiaoxinxin
@date : 2021/9/17 - 20:17
@file : 4_9.py
@ide : PyCharm
"""


# 创建一个空字典
dictStu = {1: 99, 2: 98, 3: 88, 4: 89, 5: 90}
# 1. 向字典中添加学生的成绩
dictStu[6] = 100
# 2. 修改字典中的指定学生的成绩
dictStu[1] = 98
# 3. 删除指定学生的数据
del dictStu[1]
# 4. 查询指定学生成绩
print("查询学号为3的同学的成绩为：", dictStu[3])
# 5. 统计学生的成绩，如最高分，最低分，平均分
# 5.1 统计学生的最高分
maxScore = 0
for score in dictStu.values():
    if score > maxScore:
        maxScore = score
print("学生的最高分为：", maxScore)
# 5.2 统计学生的最低分
minScore = 100
for score in dictStu.values():
    if score < minScore:
        minScore = score
print("学生的最低分为：", minScore)
# 5.3 计算学生的平均分
sumScore = 0
count = 0
for score in dictStu.values():
    sumScore += score
    count += 1
print(f'共有{count}个学生')
print("学生的平均分为：", sumScore / count)


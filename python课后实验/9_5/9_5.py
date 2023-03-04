# -*- coding: utf-8 -*-
"""
@Author : xiaoxinxin
@Date : 2021/11/14 - 16:41
@File : 9_5.py
@IDE : PyCharm
"""

import csv


while True:
    print("请依次输入学生的姓名，性别，年龄，语文成绩，数学成绩，英语成绩(中间用空格分隔):")
    name, sex, age, ChineseGrade, MathGrade, EnglishGrade = input().split(" ")
    with open("grade.csv", "a", newline='') as file:
        fw = csv.writer(file)
        list1 = [name, sex, age, ChineseGrade, MathGrade, EnglishGrade]
        fw.writerow(list1)
        print("写入成功!")
    isExit = input("退出请输入-1:")
    if isExit == "-1":
        break
    else:
        continue

with open("grade.csv", "r") as file:
    fr = csv.reader(file)
    infoStu = [row for row in fr]
    listGrade = []
    for stu in infoStu:
        listGrade.append(int(stu[3]) + int(stu[4]) + int(stu[5]))

# 冒泡排序从大到小排列学生的成绩
sumStu = len(listGrade)
for i in range(sumStu - 1):
    for j in range(sumStu - 1 - i):
        if listGrade[j] > listGrade[j + 1]:
            listGrade[j], listGrade[j + 1] = listGrade[j + 1], listGrade[j]

# 将listGrade中的整数转化为字符串形式
for i in range(len(listGrade)):
    listGrade[i] = str(listGrade[i])

# 排序好的总成绩写入statistics.csv中
with open("statistics.csv", "w") as file:
    fw = csv.writer(file)
    fw.writerow(listGrade)

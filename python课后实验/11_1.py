# -*- coding: utf-8 -*-
"""
@Author : xiaoxinxin
@Date : 2021/12/16 - 22:49
@File : 11_1.py
@IDE : PyCharm
"""

import sqlite3


# 定义操作数据库类
class OperateStudentDB:
    # 定义构造方法
    def __init__(self):
        try:
            self.conn = sqlite3.connect('Student.db')  # 创建或链接数据库
            self.cur = self.conn.cursor()
            self.cur.execute('''create table if not exists tb_grade(sno text, sname text, sex text, birthday text, 
            maths text, english text, os text);''')
            self.conn.commit()
            print("数据库和表创建成功!")
        except Exception as e:
            print("创建/链接数据库或创建数据表失败：", e)

    # 增
    def add_record(self, sql):
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            raise e

    # 删
    def delete_record(self, sql):
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            raise e

    # 改
    def update_record(self, sql):
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            raise e

    # 查
    def select_record(self, sql):
        try:
            cur1 = self.cur.execute(sql)
            return cur1
        except Exception as e:
            raise e

    # 定义析构方法
    def __del__(self):
        self.cur.close()
        self.conn.close()


if __name__ == "__main__":
    stuTable = OperateStudentDB()  # 创建对象

    # 提示信息
    print("***************学生成绩管理系统***************")
    print("*********************************************")
    print("----------------1. 添加数据 ------------------")
    print("----------------2. 删除数据 ------------------")
    print("----------------3. 修改数据 ------------------")
    print("----------------4. 查找数据 ------------------")
    print("----------------5. 显示所有 ------------------")
    print("----------------6. 删除所有 ------------------")
    print("----------------7. 退出系统 ------------------")
    # 主菜单开始
    while True:
        fun_num = input("请输入想要操作的功能序号：")
        if fun_num == "1":
            print("请依次输入学生的学号,姓名,性别,出生日期，数学、英语、操作系统的成绩:")
            stu = input().split(' ')
            try:
                sql1 = "select * from tb_grade"
                cur1 = stuTable.select_record(sql1)
            except Exception as e:
                print("查询失败!", e)
            while True:
                for row in cur1:
                    if row[0] == stu[0]:
                        print("学号输入错误,请重新输入:", end='')
                        stu[0] = input()
                        break
                else:
                    print("输入成功!")
                    break
            try:
                sql2 = "insert into tb_grade(sno, sname, sex, birthday, maths, english, os) " \
                       "VALUES ('" + stu[0] + "', '" + stu[1] + "', '" + stu[2] + "', '" + stu[3] + "', '" + stu[
                           4] + "', '" + stu[5] + "', '" + stu[6] + "')"
                # 注意字符串要用单引号+双引号+(+ 字符串 +)
                stuTable.add_record(sql2)
                print("添加记录成功!")
            except Exception as e:
                print("添加记录失败!", e)

        elif fun_num == '2':
            name = input("请输入想删除的学生的姓名：")
            try:
                sql1 = "select * from tb_grade"
                cur1 = stuTable.select_record(sql1)
            except Exception as e:
                print("查询失败!", e)
            for row in cur1:
                if row[1] == name:
                    try:
                        sql2 = "delete from tb_grade where sname='" + name + "'"
                        # 注意字符串的特殊格式，
                        stuTable.delete_record(sql2)
                        print("删除记录成功!")
                        break
                    except Exception as e:
                        print("删除记录失败!", e)
            else:
                print("查无此人!")

        elif fun_num == '3':
            name, math, english, os = input("请依次输入想要修改的学生的姓名,数学,英语,操作系统的成绩:").split(' ')
            try:
                sql1 = "select * from tb_grade"
                cur1 = stuTable.select_record(sql1)
            except Exception as e:
                print("查询失败!", e)
            for row in cur1:
                if row[1] == name:
                    try:
                        sql2 = "update tb_grade set maths='"+math+"', english='"+english+"', os='"+os+"' where sname='"+name+"'"
                        stuTable.update_record(sql2)
                        print("更新记录成功!")
                        break
                    except Exception as e:
                        print("更新记录失败!", e)
            else:
                print("查无此人!")

        elif fun_num == '4':
            name = input("想要查询的学生的姓名:")
            try:
                sql1 = "select * from tb_grade"
                cur1 = stuTable.select_record(sql1)
            except Exception as e:
                print("查询失败!", e)
            for row in cur1:
                if row[1] == name:
                    print("学号：", row[0], ",姓名：", row[1], ",性别：", row[2]
                          , "出生日期：", row[3], "数学：", row[4], ",英语：", row[5], ",操作系统：", row[6])
                    break
            else:
                print("查无此人!")

        elif fun_num == '5':
            try:
                sql1 = "select * from tb_grade"
                cur1 = stuTable.select_record(sql1)
            except Exception as e:
                print("查询失败!", e)
            for row in cur1:
                print("学号：", row[0], ",姓名：", row[1], ",性别：", row[2]
                      , ",出生日期：", row[3], ",数学：", row[4], ",英语：", row[5], ",操作系统：", row[6])

        elif fun_num == '6':
            try:
                sql = "delete from tb_grade"
                stuTable.delete_record(sql)
                print("删除成功!")
            except Exception as e:
                print("删除失败!", e)

        else:
            break


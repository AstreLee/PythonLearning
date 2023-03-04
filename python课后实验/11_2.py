# -*- coding: utf-8 -*-
"""
@Author : xiaoxinxin
@Date : 2021/12/18 - 13:28
@File : 11_2.py
@IDE : PyCharm
"""


import sqlite3


# 定义操作数据库的类
class OperationDatabase:
    def __init__(self):
        try:
            self.conn = sqlite3.connect("staff.db")
            self.cur = self.conn.cursor()
            # 创建第一张表
            self.cur.execute('''create table if not exists tb_emp(eid text, name text, sex text, birthday text, 
            intro text, profession text, dept text);''')
            # 提交
            self.conn.commit()
            # 创建第二张表
            self.cur.execute('''create table if not exists tb_profession(id text, name text);''')
            # 提交
            self.conn.commit()
            # 创建第三张表
            self.cur.execute('''create table if not exists tb_dept(id text, name text);''')
            # 提交
            self.conn.commit()
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


if __name__ == "__main__":
    staffTable = OperationDatabase()  # 创建操作数据库的类

    # 打印提示信息
    # 提示信息
    print("***************员工信息管理系统***************")
    print("*********************************************")
    print("----------------1. 添加数据 ------------------")
    print("----------------2. 删除数据 ------------------")
    print("----------------3. 修改数据 ------------------")
    print("----------------4. 查找数据 ------------------")
    print("----------------5. 显示所有 ------------------")
    print("----------------6. 退出系统 ------------------")

    # 主菜单开始
    while True:
        fun_num = input("请输入选择的功能序号:")
        if fun_num == "1":
            staff = input("依次输入员工id,name,sex,birthday,intro,profession,dept,proName,deptName:").split(' ')
            try:
                sql1 = "select * from tb_emp"
                cur = staffTable.select_record(sql1)
            except Exception as e:
                print("查询失败!", e)
            while True:
                for row in cur:
                    if row[0] == staff[0]:
                        staff[0] = input("员工ID输入错误，请重新输入:")
                        break
                else:
                    print("输入成功!")
                    break
            try:
                sql2 = "insert into tb_emp(eid,name,sex,birthday,intro,profession,dept) Values ('"+staff[0]+"', '"+staff[1]+"', '"+staff[2]+"', '"+staff[3]+"', '"+staff[4]+"', '"+staff[5]+"', '"+staff[6]+"') "
                staffTable.add_record(sql2)
                sql3 = "insert into tb_profession(id,name) Values ('"+staff[0]+"', '"+staff[7]+"')"
                staffTable.add_record(sql3)
                sql4 = "insert into tb_dept(id,name) Values ('"+staff[0]+"', '"+staff[8]+"')"
                staffTable.add_record(sql4)
                print("添加记录成功!")
            except Exception as e:
                print("添加失败!", e)

        elif fun_num == "2":
            staffId = input("输入待删除的员工的ID:")
            try:
                sql1 = "select * from tb_emp"
                cur = staffTable.select_record(sql1)
            except Exception as e:
                print("查询失败", e)
            for row in cur:
                if row[0] == staffId:
                    try:
                        sql2 = "delete from tb_emp where eid='"+row[0]+"'"
                        staffTable.delete_record(sql2)
                        sql3 = "delete from tb_profession where id='"+row[0]+"'"
                        staffTable.delete_record(sql3)
                        sql4 = "delete from tb_dept where id='"+row[0]+"'"
                        staffTable.delete_record(sql4)
                        print("删除成功!")
                        break
                    except Exception as e:
                        print("删除失败!", e)
            else:
                print("查无此人!")

        elif fun_num == '3':
            staffId, self_intro = input("请输入想要修改的员工的ID，个人介绍").split(' ')
            try:
                sql1 = "select * from tb_emp"
                cur = staffTable.select_record(sql1)
            except Exception as e:
                print("查询失败", e)
            for row in cur:
                if row[0] == staffId:
                    try:
                        sql2 = "update tb_emp set intro='"+self_intro+"' where eid='"+staffId+"'"
                        staffTable.update_record(sql2)
                        print("更新成功!")
                        break
                    except Exception as e:
                        print("更新记录失败", e)
            else:
                print("查无此人!")

        elif fun_num == '4':
            staffId = input("请输入想要查询的员工的ID:")
            try:
                sql1 = "select * from tb_emp"
                staffTable.select_record(sql1)
            except Exception as e:
                print("查询失败!", e)
            for row in cur:
                if row[0] == staffId:
                    print("编号:", row[0], " 姓名:", row[1], " 性别:", row[2], " 生日:", row[3], " 自我介绍:", row[4],
                          " 职业:", row[5], " 部门号:", row[6])
                    break
            else:
                print("查无此人!")

        elif fun_num == '5':
            try:
                sql1 = "select * from tb_emp"
                cur = staffTable.select_record(sql1)
            except Exception as e:
                print("查询失败!", e)
            for row in cur:
                print("编号:", row[0], " 姓名:", row[1], " 性别:", row[2], " 生日:", row[3], " 自我介绍:", row[4],
                      " 职业:", row[5], " 部门号:", row[6])
            print("查询完毕!")

        else:
            break

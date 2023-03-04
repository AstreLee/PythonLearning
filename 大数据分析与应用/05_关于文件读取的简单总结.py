# -*- coding: utf-8 -*-
"""
@Author : xiaoxinxin
@Date : 2022/3/7 - 15:39
@File : 05_关于文件读取的简单总结.py
@IDE : PyCharm
"""


"""
一、读取txt文件
使用pandas.read_table函数
参数有：
    1. file(表示要打开的txt文件)
    2. names=[列名1, 列名2, ...]，如果不设置的话默认就是第一行作为列名
    3. sep表示分隔符，默认是\t
    
二、读取csv文件
使用pandas.read_csv函数
参数有：
    1. file(表示要打开的csv文件)
    2. names=[列名1, 列名2, ...]，如果不设置的话默认就是第一行作为列名
    3. sep表示分隔符，默认是,
    
三、读取excel文件
使用pandas.read_excel函数
参数有：
    1. file(表示要打开的excel文件)
    2. sheet_name
        2.1 =['列名1', '列名2', ...]，这个列名要用引号
        2.2 =[a, b]：表示从工作簿中从0开始，读取a~b的工作表，再以字典的形式返回
                     其中key是a~b，value就是对应的工作表中的内容
        2.3 ="工作表名"：这种就是直接指定工作表了，比较容易
        2.4 =None：选定所有的工作表，以字典的形式返回，其中key是工作表的名称，value
                   是与之对应的工作表的名字
    3. header：表示从第几行开始选取，header=0表示第一行作为表头加入进来
                header=1表示去掉第一行
                
四、导出csv文件(导出txt文件也和这个差不多)
使用pandas.to_csv()函数
参数有：
    1. file：指定生成的csv表的名称以及存放的路径
    2. sep表示分隔符，默认是逗号(txt文件默认\t?)，当然也可以指定像是\t或者是空格都行
    3. index表示行号，有True和False两种值，默认是True表示显示行号，指定为False表示不显示行号
    4. header表示是否显示列名，有True和False两种，默认是True显示列名，指定为False则不显示表头

五、导出为excel文件
使用pandas.to_excel()函数
参数有：
    1. file：和to_csv()一样
    2. index和header都是与to_csv()一样的
    
补充如何向excel文件追加新的工作表
使用pandas.ExcelWriter
    步骤：1. 创建ExcelWriter文件流对象(r'[指定的文件名]', mode='a')
             eg: fileopen = ExcelWriter(r'text.xlsx', mode='a')
                1.1 参数mode='a'表示模式为append添加，r表示以规格化的形式打开
         2. obj.to_excel(fileopen, sheet_name='要添加的工作表的名称', [index=], [header=])
         3. fileopen.save()   # 这个是一定要保存的，不然添加的是不会有结果的
"""
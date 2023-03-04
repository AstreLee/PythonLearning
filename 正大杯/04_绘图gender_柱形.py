# -*- coding: utf-8 -*-
"""
@Author : xiaoxinxin
@Date : 2022/2/19 - 14:52
@File : 04_绘图gender_柱形.py
@IDE : PyCharm
"""


import pandas as pd
from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.globals import ThemeType
# 这次我们用饼状图来展示一下性别

# 1. 获取数据
# 首先获取所有的省份数据
df = pd.read_excel('all.xlsx')
# 再创建一个列表保存性别
genders = []
# 获取性别一列的数据也就是第一列
for item in df.iloc[:, 0]:
    if item == '男':
        genders.append(1)
    else:
        genders.append(2)
gx = ['男', '女']
gy = [
    genders.count(1),
    genders.count(2),
]

(
    Bar(init_opts=opts.InitOpts(theme=ThemeType.CHALK, width='700px', height='400px'))
    .add_xaxis(gx)
    .add_yaxis("", gy)
    .set_global_opts(title_opts=opts.TitleOpts(title='性别柱状图', subtitle='数据来源：问卷网', pos_left='center'))
).render('C:\\A_code\\pycharm\\study\\正大杯\\性别柱图.html')

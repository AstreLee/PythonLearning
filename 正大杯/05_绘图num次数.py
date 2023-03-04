# -*- coding: utf-8 -*-
"""
@Author : xiaoxinxin
@Date : 2022/2/19 - 15:46
@File : 05_绘图num次数.py
@IDE : PyCharm
"""

import pandas as pd
from pyecharts.charts import Line
from pyecharts import options as opts
from pyecharts.globals import ThemeType

# 这次我们用饼状图来展示一下性别

# 1. 获取数据
# 首先获取所有的省份数据
df = pd.read_excel('all.xlsx')
# 创建次数列表
nums = []
# 创建x轴列表
gx = ['0次', '1~5次', '6~15次', '15次以上']
# 创建y轴列表
gy = []

countA = 0
countB = 0
countC = 0
countD = 0
for item in df.iloc[:, 5]:
    if item == '0次':
        countA += 1
    elif item == '1-5次':
        countB += 1
    elif item == '6-15次':
        countC += 1
    else:
        countD += 1
gy = [countA, countB, countC, countD]
(
    Line(init_opts=opts.InitOpts(theme=ThemeType.DARK, width='700px', height='400px'))
    .add_xaxis(gx)
    .add_yaxis("", gy, areastyle_opts=opts.AreaStyleOpts(opacity=0.5))
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title='次数统计', subtitle='数据来源：问卷网', pos_left='center')
    )
).render('C:\\A_code\\pycharm\\study\\正大杯\\次数折线图.html')
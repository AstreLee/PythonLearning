# -*- coding: utf-8 -*-
"""
@Author : xiaoxinxin
@Date : 2022/2/19 - 14:26
@File : 03_绘图gender_饼状.py
@IDE : PyCharm
"""


import pandas as pd
from pyecharts.charts import Pie
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
"""
或者是:
count_1 = 0
count_2 = 0
for item in genders:
    if item == 1:
        count_1 += 1
    else:
        count_2 += 1
gy.append(count_1)
gy.append(count_2)
"""
(
    Pie(init_opts=opts.InitOpts(theme=ThemeType.CHALK, width='700px', height='400px'))
    .add("", list(zip(gx, gy)))
    .set_global_opts(title_opts=opts.TitleOpts(title='性别比例', subtitle='数据来源：问卷网', pos_left='pos_left'))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{d}%", font_size=12))
).render('C:\\A_code\\pycharm\\study\\正大杯\\性别饼图.html')


"""

其中变量a、b、c在不同图表类型下代表数据含义为：

折线（区域）图、柱状（条形）图: a（系列名称），b（类目值），c（数值）, d（无）
散点图（气泡）图 : a（系列名称），b（数据名称），c（数值数组）, d（无）
饼图、雷达图 : a（系列名称），b（数据项名称），c（数值）, d（百分比）
弦图 : a（系列名称），b（项1名称），c（项1-项2值），d（项2名称)， e(项2-项1值)
力导向图 :
节点 : a（类目名称），b（节点名称），c（节点值）
边 : a（系列名称），b（源名称-目标名称），c（边权重）， d（如果为true的话则数据来源是边）
"""
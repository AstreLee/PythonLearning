# -*- coding: utf-8 -*-
"""
@Author : xiaoxinxin
@Date : 2022/5/16 - 14:46
@File : 可视化.py
@IDE : PyCharm
"""

from pandas import read_excel
from pyecharts.charts import Pie, Line, Bar, Scatter
from pyecharts import options as opts
from pyecharts.globals import ThemeType

# # 首先绘制饼图
# 1. 获取数据
# 首先获取所有的省份数据
df = read_excel('可视化.xlsx')
count_1 = 0
count_2 = 0
for item in df.iloc[:, 3]:
    if item == '男':
        count_1 += 1
    else:
        count_2 += 1
gy = [count_1, count_2]
gx = ['男', '女']
(
    Pie(init_opts=opts.InitOpts(theme=ThemeType.DARK, width='700px', height='400px'))
        .add("", list(zip(gx, gy)))
        .set_global_opts(title_opts=opts.TitleOpts(title='性别比例', subtitle='数据来源：成绩统计', pos_left='pos_left'))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{d}%", font_size=12))
).render('.\饼图.html')

# 绘制折线图
gx = []
gy = []
for i in range(len(df)):
    gx.append(str(df.iloc[i, 0])[-3:])
gx.sort()
# 创建y轴列表
for num in gx:
    for count in range(len(df)):
        if str(df.iloc[count, 0])[-3:] == num:
            gy.append(str(df.iloc[count, 10]))
            break
(
    Line(init_opts=opts.InitOpts(theme=ThemeType.LIGHT, width='1000px', height='400px'))
        .add_xaxis(gx)
        .add_yaxis("", gy)
        .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
        .set_global_opts(
        title_opts=opts.TitleOpts(title='分数折线图', subtitle='数据来源：已知数据', pos_left='center'),
        yaxis_opts=opts.AxisOpts(min_=300)
    )
).render('.\折线图.html')

# 绘制柱图
gx = []
gy = []
for num in range(len(df)):
    gx.append(str(df.iloc[num, 0]))
    gy.append(str(df.iloc[num, 10]))
(
    Bar(init_opts=opts.InitOpts(theme=ThemeType.CHALK, width='1000px', height='500px'))
        .add_xaxis(gx)
        .add_yaxis("", gy)
        .set_global_opts(
        title_opts=opts.TitleOpts(title='分数柱状图', subtitle='数据来源：已知数据', pos_left='center'),
        xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-90)),
        yaxis_opts=opts.AxisOpts(min_=300)
    )
).render('.\柱状图.html')

# 绘制散点图
gx = []
gy = []
for num in range(len(df)):
    gx.append(str(df.iloc[num, 0]))
    gy.append(int(df.iloc[num, 10]))
(
    Scatter(init_opts=opts.InitOpts(theme=ThemeType.LIGHT, width='1000px', height='500px'))
        .add_xaxis(gx)
        .add_yaxis('', y_axis=gy)
        .set_global_opts(
        title_opts=opts.TitleOpts(title='分数散点图', subtitle='数据来源：已知数据', pos_left='center'),
        xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-90)),
        visualmap_opts=opts.VisualMapOpts(
            type_='color',  # 颜色设置
            max_=500,  # 图标数值大小
            min_=300
        ),
        yaxis_opts=opts.AxisOpts(min_=300)
    )
).render('.\散点图.html')

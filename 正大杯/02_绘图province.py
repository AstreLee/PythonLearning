# -*- coding: utf-8 -*-
"""
@Author : xiaoxinxin
@Date : 2022/2/19 - 10:32
@File : 02_绘图province.py
@IDE : PyCharm
"""


from collections import Counter
import pandas as pd
from pyecharts.charts import Geo
from pyecharts import options as opts
from pyecharts.globals import ThemeType

# 首先获取所有的省份数据
df = pd.read_excel('all.xlsx')
# 创建城市列表保存城市
cities = []
# 再对第二十六列的数据遍历添加到列表当中
for city in df.iloc[:, 26]:
    if city != '':
        cities.append(city)
c = Counter(cities)
data = c.most_common(101)

# 现在我们去掉第一个无用的nan数据
list1 = []
for i in range(1, len(data)):
    list1.append(data[i])
data = list1

gx1 = []
gy1 = []
for item in data:
    gx1.append(item[0])
    gy1.append(item[1])
geo = Geo(init_opts=opts.InitOpts(width="800px", height='500px', theme=ThemeType.DARK, bg_color="#404a59"))
(
    geo.add_schema(maptype='china', itemstyle_opts=opts.ItemStyleOpts(color='#323c48', border_color='#111'))
    .add("数据源城市", list(zip(gx1, gy1)))
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        toolbox_opts=opts.ToolboxOpts,
        title_opts=opts.TitleOpts(title='位置分布地理坐标', pos_left='left'),
        visualmap_opts=opts.VisualMapOpts(max_=120, is_piecewise=True)
    )
).render('C:\\A_code\\pycharm\\study\\正大杯\\省份点状图.html')

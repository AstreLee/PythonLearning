# -*- coding: utf-8 -*-
"""
@Author : xiaoxinxin
@Date : 2021/11/18 - 16:09
@File : 8_3.py
@IDE : PyCharm
"""

import re
import urllib.request

with urllib.request.urlopen('https://baike.baidu.com/item/%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0/217599?fr=aladdin') as file:
    print("网页状态：", file.status, file.reason)
    data = file.read().decode('utf-8')
    reg = "<title>(.*?)</title>"   # 获取网页的标题
    title = re.findall(reg, data, re.S | re.M)
    print("网页标题：", title)
    reg = '<div class="hotnews" alog-group="focustop-hotNews">(.*?)</div>'
    news = re.findall(reg, data, re.S | re.M)
    hotnews_list = []
    for item in news:
        hotnews_list = re.findall("<a .*?>(.*?)</a>", item)
    print("热点要闻：")
    for hotnews in hotnews_list:
        print(hotnews)

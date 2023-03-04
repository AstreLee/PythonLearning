# -*- coding: utf-8 -*-
"""
@Author : xiaoxinxin
@Date : 2022/1/27 - 19:31
@File : 05_requests模块发送带参数的请求.py
@IDE : PyCharm
"""


import requests


headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/97.0.4692.71 Safari/537.36"}
# 直接对含有参数的url发起请求
# 我们在使用百度搜索的时候经常发现url地址中会有一个 ?，那么该问号后边的就是请求参数，又叫做查询字符串
url = "https://www.baidu.com/s?wd=python"
# 获取响应对象
response = requests.get(url, headers=headers)
# 打印响应的对象
print(response.content.decode())

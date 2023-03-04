# -*- coding: utf-8 -*-
"""
@Author : xiaoxinxin
@Date : 2022/1/27 - 19:08
@File : 04_requests模块发送带headers的请求.py
@IDE : PyCharm
"""

"""
请求头中有很多字段，其中User-Agent字段必不可少，表示客户端的操作系统以及浏览器的信息
requests.get(url, headers=headers)

- headers参数接收字典形式的请求头
- 请求头字段名作为key，字段对应的值作为value

"""
import requests

url = "https://www.baidu.com"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/97.0.4692.71 Safari/537.36"}
# 在请求头中带上User-Agent，模拟浏览器发送请求
response = requests.get(url, headers=headers)
print(response.content.decode())
print(response.request.headers)


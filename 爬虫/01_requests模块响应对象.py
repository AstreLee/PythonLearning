# -*- coding: utf-8 -*-
"""
@Author : xiaoxinxin
@Date : 2022/1/27 - 18:40
@File : 01_requests模块响应对象.py
@IDE : PyCharm
"""



import requests


# 目标url
url = "https://www.baidu.com"


# 向目标url发送get请求
response = requests.get(url)


# 打印响应的内容
print(response.content.decode())
# 默认是UTF-8编码字符集
# decode()函数中也可以指定编码的字符集，比如说GBK,GB2312等

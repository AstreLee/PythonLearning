# -*- coding: utf-8 -*-
"""
@Author : xiaoxinxin
@Date : 2022/1/28 - 11:13
@File : 10_超时参数timeout的使用.py
@IDE : PyCharm
"""


import requests


url = "https://www.baidu.com"
response = requests.get(url, timeout=3)
print(response.content.decode())


"""
为什么要使用timeout超时参数
在平时网上冲浪的过程中，我们经常会遇到网络波动，这个时候，一个请求等了很久可能任然没有结果。
在爬虫中，一个请求很久没有结果，就会让整个项目的效率变得非常低，这个时候我们就需要对请求进行强制要求，让他必须在特定的时间内返回结果，否则就报错

"""
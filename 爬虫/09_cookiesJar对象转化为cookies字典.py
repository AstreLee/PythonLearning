# -*- coding: utf-8 -*-
"""
@Author : xiaoxinxin
@Date : 2022/1/28 - 11:06
@File : 09_cookiesJar对象转化为cookies字典.py
@IDE : PyCharm
"""


import requests

# 要访问的url
url = "https://www.baidu.com"

# 构造请求头字典
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/97.0.4692.71 Safari/537.36"}

# 带有header参数获取响应体
response = requests.get(url, headers=headers)

# 打印响应体的内容
# print(response.content.decode())

# 打印响应体的cookies内容
print(response.cookies)

# 将cookiesJar类型的对象转化为cookies类型的对象
cookies_dict = requests.utils.dict_from_cookiejar(response.cookies)

# 打印从cookieJar转为cookies字典
print(cookies_dict)

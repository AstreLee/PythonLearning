# -*- coding: utf-8 -*-
"""
@Author : xiaoxinxin
@Date : 2022/1/27 - 19:39
@File : 06_通过params携带参数字典.py
@IDE : PyCharm
"""

import requests

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/97.0.4692.71 Safari/537.36"}
# 这是目标url
# url = "https://www.baidu.com/s?wd=python"

# 最后有没有问号都一样
url = "https://www.baidu.com/s?"

# 请求参数是一个字典
kw = {'wd': 'python'}

# 带上请求参数发起请求，获取响应
response = requests.get(url, headers=headers, params=kw)

# 打印响应体的内容
# print(response.content.decode())

# 打印请求体的内容
# print(response.request.headers)

# 打印响应体的内容
# print(response.headers)

# 写入文件
with open("baidu.html", "wb") as f:
    f.write(response.content)

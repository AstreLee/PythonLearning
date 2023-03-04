# -*- coding: utf-8 -*-
"""
@Author : xiaoxinxin
@Date : 2022/1/28 - 10:04
@File : 07_在headers参数中携带cookie.py
@IDE : PyCharm
"""


import requests

# 访问的url
url = "https://github.com/USER_NAME"

# headers头部参数
headers = {
    # 从浏览器复制过来的User-Agent
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 "
                  "Safari/537.36",
    # 从浏览器复制过来的cookie
    "Cookie": "从cookie复制过来的字符串，注意要先通过;分隔再通过=分隔构成字典(实际上用带cookies参数的方法更好使用)"
}
# 请求头参数字典中携带cookie字符串
response = requests.get(url, headers=headers)

# 打印响应体的内容
print(response.content.decode())

# -*- coding: utf-8 -*-
"""
@Author : xiaoxinxin
@Date : 2022/1/27 - 18:49
@File : 02_response响应对象常用属性.py
@IDE : PyCharm
"""


import requests


# 请求的url地址
url = "https://www.baidu.com"

# 获取url的相应的内容
response = requests.get(url)

# - response.url响应的url；有时候响应的url和请求的url并不一致
# - response.status_code 响应状态码
# - response.request.headers 响应对应的请求头
# - response.headers 响应头
# - response.request._cookies 响应对应请求的cookie；返回cookieJar类型
# - response.cookies 响应的cookie（经过了set-cookie动作；返回cookieJar类型
# - response.json()自动将json字符串类型的响应内容转换为python对象（dict or list）

print(response.url)  # 这里是相应的url，不是请求的url，一定要注意区分
print(response.status_code)  # 打印响应的状态码
print(response.request.headers)  # 打印响应对应的请求头
print(response.headers)  # 响应头
# print(response.request._cookies)   # 打印对应请求的cookie；返回cookieJar类型
# print(response.cookies)  # 打印响应了的cookie
# print(response.json())  # 自动将json字符串响应的内容转化为python对象(dict or list)


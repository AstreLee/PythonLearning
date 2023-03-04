# -*- coding: utf-8 -*-
"""
@Author : xiaoxinxin
@Date : 2022/1/28 - 11:54
@File : 12_verify参数忽略CA证书.py
@IDE : PyCharm
"""

import requests

url = "https://www.baidu.com"
response = requests.get(url, verify=False)
# 为了在代码中能够正常的请求，我们使用verify=False参数，此时requests模块发送请求将不做CA证书的验证：verify参数能够忽略CA证书的认证

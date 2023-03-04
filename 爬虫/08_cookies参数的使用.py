# -*- coding: utf-8 -*-
"""
@Author : xiaoxinxin
@Date : 2022/1/28 - 10:42
@File : 08_cookies参数的使用.py
@IDE : PyCharm
"""

import requests

# 要访问的url
url = "https://gitee.com/USER_NAME"

# 构造请求头字典
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/97.0.4692.71 Safari/537.36"}

# 构造cookies字典
# 首先接收来自cookies的字符串
cookies_str = "user_locale=zh-CN; oschina_new_user=false; remote_way=http; close_wechat_tour=true; " \
              "yp_riddler_id=6ffcadd5-558a-4841-b4bb-15cbe37d618b; " \
              "sensorsdata2015jssdkchannel=%7B%22prop%22%3A%7B%22_sa_channel_landing_url%22%3A%22%22%7D%7D; " \
              "visit-gitee--2021-12-06%2018%3A23%3A21%20%2B0800=1; " \
              "Hm_lvt_dbba4dc235af9a121ecb9ae949529239=1640184092; " \
              "visit-gitee--2021-12-22%2016%3A15%3A17%20%2B0800=1; slide_id=9; tz=Asia%2FShanghai; " \
              "sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%228956827%22%2C%22first_id%22%3A%22178c03b80d03f7" \
              "-08ecc0f8d120ad-31614c0c-921600-178c03b80d13d9%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type" \
              "%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A" \
              "%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com" \
              "%2Flink%22%2C%22%24latest_utm_source%22%3A%22baidu%22%2C%22%24latest_utm_medium%22%3A%22sem%22%2C%22" \
              "%24latest_utm_campaign%22%3A%22enterprise%22%2C%22%24latest_utm_content%22%3A%22competition%22%2C%22" \
              "%24latest_utm_term%22%3A%22codinggitee%22%7D%2C%22%24device_id%22%3A%22178c03b80d03f7-08ecc0f8d120ad" \
              "-31614c0c-921600-178c03b80d13d9%22%7D; Hm_lvt_24f17767262929947cc3631f99bfd274=1642689691,1643030767," \
              "1643096138,1643337579; gitee_user=true; Hm_lpvt_24f17767262929947cc3631f99bfd274=1643337619; " \
              "gitee-session-n" \
              "=b056TjA4Zi9RcXFmRzF6VEZMbEx5dDI0b2JUNVlEOXdvdDRzTnpPbThtcnpCcmJSSWdxaUV2c2JPSHZPR1dqNmw5Y2lwVEhwa3BC" \
              "SlJLYjdvWXNGUzhydC8vamxVVElqYlY0eGkvS0pJZm5WS3hGdzNpZzMxSnBqcGJSb3pOTjE2cTNMaUtHZ204QXlHbytmWDM3UGg0N1" \
              "ViUXdJMytBODc2cHgwQ3hHTU5tT0hsOXQzVnhXQXlZWm80OEdPOVpQWU5TL1dLV2s1bUx2c2tzK1FvdFpmZVY3bWV1bjl1aHJ5VER" \
              "TUjhpTkN5c3pXZ0l6WGFCbS9ZSVA4S1Rtejk5a1Y2L0VvdmJIVWI0TXJmU1k1dXIveVFiTGVDcVdlTlJmeEM4YitWMGxOU081Vkdte" \
              "i8rUWJieTljK2ZnaFN4MmVVTDY3RmtENmZGZmpkUGZZYTdleEdrdFBneVJJcFJXekhqS1M4eEhrSHlFPS0tTGt0L0ZkLzhlbkQ4Ri9" \
              "UM0JvVm5Ldz09--8f50348a4a633b011c3235908696fb74e32a7f3a "

# 构造cookies参数字典
cookies_dict = {cookie.split("=")[0]: cookie.split("=")[-1] for cookie in cookies_str.split(";")}

# 请求头参数字典中携带cookies字符串
response = requests.get(url, headers=headers, cookies=cookies_dict)

# 打印响应体的内容
# rint(response.content.decode())

# 写入文件
with open("User.html", "wb") as f:
    f.write(response.content)


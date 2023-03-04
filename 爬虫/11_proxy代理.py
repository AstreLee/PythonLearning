# -*- coding: utf-8 -*-
"""
@Author : xiaoxinxin
@Date : 2022/1/28 - 11:40
@File : 11_proxy代理.py
@IDE : PyCharm
"""


import requests


url = "https://www.baidu.com"
proxy = {
    'http': 'http://101.231.104.82:80',
    'https': 'https://101.231.104.82:80',
    # 'https': 'https://1.192.246.63:9999',
}
response = requests.get(url, proxies=proxy)

"""
代理的相关知识点:
正向代理和反向代理的区别

前边提到proxy参数指定的代理ip指向的是正向的代理服务器，那么相应的就有反向服务器；现在来了解一下正向代理服务器和反向代理服务器的区别

1. 从发送请求的一方的角度，来区分正向或反向代理
2. 为浏览器或客户端（发送请求的一方）转发请求的，叫做正向代理
   - 浏览器知道最终处理请求的服务器的真实ip地址，例如VPN
3. 不为浏览器或客户端（发送请求的一方）转发请求、而是为最终处理请求的服务器转发请求的，叫做反向代理
   - 浏览器不知道服务器的真实地址，例如nginx

3.7.3 代理ip（代理服务器）的分类

1. 根据代理ip的匿名程度，代理IP可以分为下面三类：
   - 透明代理(Transparent Proxy)：透明代理虽然可以直接“隐藏”你的IP地址，但是还是可以查到你是谁。目标服务器接收到的请求头如下：
         REMOTE_ADDR = Proxy IP
         HTTP_VIA = Proxy IP
         HTTP_X_FORWARDED_FOR = Your IP
   - 匿名代理(Anonymous Proxy)：使用匿名代理，别人只能知道你用了代理，无法知道你是谁。目标服务器接收到的请求头如下：
         REMOTE_ADDR = proxy IP
         HTTP_VIA = proxy IP
         HTTP_X_FORWARDED_FOR = proxy IP
   - 高匿代理(Elite proxy或High Anonymity Proxy)：高匿代理让别人根本无法发现你是在用代理，所以是最好的选择。毫无疑问使用高匿代理效果最好。目标服务器接收到的请求头如下：
         REMOTE_ADDR = Proxy IP
         HTTP_VIA = not determined
         HTTP_X_FORWARDED_FOR = not determined
2. 根据网站所使用的协议不同，需要使用相应协议的代理服务。从代理服务请求使用的协议可以分为：
   - http代理：目标url为http协议
   - https代理：目标url为https协议
   - socks隧道代理（例如socks5代理）等：
     1. socks 代理只是简单地传递数据包，不关心是何种应用协议（FTP、HTTP和HTTPS等）。
     2. socks 代理比http、https代理耗时少。
     3. socks 代理可以转发http和https的请求

3.7.4 proxies代理参数的使用

为了让服务器以为不是同一个客户端在请求；为了防止频繁向一个域名发送请求被封ip，所以我们需要使用代理ip；那么我们接下来要学习requests模块是如何使用代理ip的



总的来说，所谓的代理就是防止请求频繁被封号
"""
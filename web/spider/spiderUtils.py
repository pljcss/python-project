# -*- coding:utf-8 -*-
import requests
import json
import time
from bs4 import BeautifulSoup
import random

"""
封装 requests 模块
"""
def requests_utils(url):

    # 动态加载 user_agent
    user_agent = [
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36",
        "Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"
    ]

    # 动态设置代理 IP
    proxies = {'http': 'http://127.0.0.1:1087',
               'https': 'http://127.0.0.1:1087'}

    # 封装请求头
    headers = dict()
    headers['User-Agent'] = random.choice(user_agent)
    # headers["Connection"] = "keep-alive"
    headers["Connection"] = "close"
    headers["Accept"] = "text/plain, */*; q=0.01"
    headers["Accept-Encoding"] = "gzip, deflate, br"
    headers["Accept-Language"] = "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7"
    headers["HOST"] = "www.dianping.com"
    headers["Cookie"] = "xxx"


    # 该url可以测试 header 是否生效
    # print(requests.get("https://www.whatismybrowser.com/detect/what-http-headers-is-my-browser-sending", headers=headers).text)


    response = requests.get(url, headers=headers)

    return response
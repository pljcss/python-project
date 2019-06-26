# -*- coding:utf-8 -*-
import requests
import json
import time
from bs4 import BeautifulSoup
import random
import time

import logging
import logging.config
logging.config.fileConfig('log.ini')


def requests_utils(url):
    """
    封装 requests 模块
    :param url:
    :return:
    """
    # 动态加载 user_agent
    user_agent = [
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36",
        "Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"
    ]

    # 封装请求头
    headers = dict()
    headers['User-Agent'] = random.choice(user_agent)
    # headers["Connection"] = "keep-alive"
    headers["Connection"] = "close"
    headers["Accept"] = "text/plain, */*; q=0.01"
    headers["Accept-Encoding"] = "gzip, deflate, br"
    headers["Accept-Language"] = "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7"
    # headers["HOST"] = "www.dianping.com"
    # headers["Cookie"] = "xxx"


    # 该url可以测试 header 是否生效
    # print(requests.get("https://www.whatismybrowser.com/detect/what-http-headers-is-my-browser-sending", headers=headers).text)

    # response = requests.get(url, headers=headers, proxies=proxies, timeout=3)

    retry_times = 0
    while retry_times < 3:
        proxies = [{'http': 'http://106.12.39.147:8899','https': 'http://106.12.39.147:8899'}]

        # proxies = [{'http': 'http://106.12.39.147:8899','https': 'http://106.12.39.147:8899'},
        #            {'http': 'http://125.114.174.50:8888','https': 'http://125.114.174.50:8888'}]

        # 动态设置代理 IP
        # proxies = {'http': 'http://125.114.174.50:8888',
        #            'https': 'http://125.114.174.50:8888'}

        print(retry_times)
        proxy_ip = random.choice(proxies)
        print(proxy_ip)
        try:
            response = requests.get(url, headers=headers, proxies=proxy_ip, timeout=1)
            return response
        except requests.exceptions.ConnectionError as e:
            retry_times = retry_times + 1
            print("重试第%d"%retry_times,"报错了", e)
        except requests.exceptions.ReadTimeout as e:
            retry_times = retry_times + 1
            print("重试第%d"%retry_times,"报错了", e)

    return None

    # # 休眠
    # sleep_time = random.uniform(0, 3)
    # # print("休眠", sleep_time)
    # time.sleep(sleep_time)




def get_lng(dd):
    if dd == "0":
        return dd
    else:
        return dd.get("lng","0")


def get_lat(dd):
    if dd == "0":
        return dd
    else:
        return dd.get("lat","0")


if __name__ == '__main__':
    result = requests_utils("http://icanhazip.com")
    if result is None:
        print(result)
    else:
        print(result.text)
    # print(result.text)


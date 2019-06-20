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

    # 动态设置代理 IP
    proxies = {'http': 'http://115.217.46.53:8888',
               'https': 'http://115.217.46.53:8888'}

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


    response = requests.get(url, headers=headers, proxies=proxies)
    sleep_time = random.uniform(0, 3)
    print("休眠", sleep_time)
    time.sleep(sleep_time)
    return response

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
    # result = requests_utils("http://icanhazip.com")
    # print(result.text)

    json_str = "{'name': '浙江大学医学院附属第一医院', 'location': {'lat': 30.26161, 'lng': 120.184319}, 'address': '杭州市上城区庆春路79号', 'province': '浙江省', 'city': '杭州市', 'area': '上城区', 'street_id': 'bf688e06cd186c9edeee8b8d', 'telephone': '(0571)87236114', 'detail': 1, 'uid': '43b7e8891c14be7359f6bea8'}"

    jjj = json_str.replace("'", '"')



    # 输出日志到控制台,获取的是root对应的logger
    console_logger = logging.getLogger()

    # 输出日志到单个文件
    file_logger = logging.getLogger(name="fileLogger")

    file_logger.error("sdfsfdsf")


    with open('/Users/caosai/Desktop/无标题.txt') as f:
        ff = f.readlines()
        str1 = ""
        for i in ff:
            str1 = str1 + i.strip('\n') + ","


        print(str1)
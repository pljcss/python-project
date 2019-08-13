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
    # user_agent = [
    #     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36",
    #     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
    #     "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36",
    #     "Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"
    # ]

    user_agent = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1 Safari/605.1.15"]

    # 封装请求头
    headers = dict()
    headers['User-Agent'] = random.choice(user_agent)
    headers["Connection"] = "keep-alive"
    # headers["Connection"] = "close"
    # headers["Accept"] = "text/plain, */*; q=0.01"
    headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
    headers["Accept-Encoding"] = "gzip, deflate, br"
    headers["Accept-Language"] = "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7"
    headers["Host"] = "www.dianping.com"

    # headers["Referer"] = "http://www.dianping.com/shop/98440846"
    # headers["X-Requested-With"] = "XMLHttpRequest"

    # headers["Origin"] = "http://www.dianping.com"

    # headers["Cookie"] = "s_ViewType=10; _lxsdk_cuid=16c8497049fc8-06b5f179e16f2a-38617706-fa000-16c8497049f7c; _lxsdk=16c8497049fc8-06b5f179e16f2a-38617706-fa000-16c8497049f7c; _hc.v=73305ac3-2ce0-dd8b-4f94-0abcc3c130cd.1565592585; _lxsdk_s=16c849704a2-56a-f51-096%7C%7C19"

    # headers["Cookie"] = "_lxsdk_cuid=16aa0e13385c8-09565305c22591-37607604-232800-16aa0e13385c8; _lxsdk=16aa0e13385c8-09565305c22591-37607604-232800-16aa0e13385c8; _hc.v=2c408a18-4187-b4d2-0016-76ee91ea5b15.1557477275; Hm_lvt_e6f449471d3527d58c46e24efb4c343e=1557477275; cy=1; cye=shanghai; s_ViewType=10; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_s=16c849faad8-d0a-305-56d%7C%7C512"

    # headers["Cookie"] = "_lxsdk_cuid=16c8524c06dc8-0fbfa373eef812-38617706-fa000-16c8524c06ec8;" \
    #                     "_lxsdk=16c8524c06dc8-0fbfa373eef812-38617706-fa000-16c8524c06ec8;" \
    #                     "_lxsdk_s=16c8524c071-661-79f-9eb%7C%7C1;" \
    #                     "_hc.v=4f73dde6-e19c-aa5f-664d-293fffc68ba6.1565601874"


    # headers["Cookie"] = "cityid=1; cy=1; cye=shanghai; _lxsdk_s=16c85c4a76a-7cc-56-e61%7C%7C124; _hc.v=7509c902-6550-1fbc-56e7-1622d5263ab3.1565612353; _lxsdk=16c85c4a768c8-0ffb41473819238-3f616c4d-fa000-16c85c4a768c8; _lxsdk_cuid=16c85c4a768c8-0ffb41473819238-3f616c4d-fa000-16c85c4a768c8"


    # cookies = {"cityid=1; cy=1; cye=shanghai; _lxsdk_s=16c85c4a76a-7cc-56-e61%7C%7C124;
    # _hc.v=7509c902-6550-1fbc-56e7-1622d5263ab3.1565612353; _lxsdk=16c85c4a768c8-0ffb41473819238-3f616c4d-fa000-16c85c4a768c8;
    # _lxsdk_cuid=16c85c4a768c8-0ffb41473819238-3f616c4d-fa000-16c85c4a768c8"}

    cookies = {
        'cityid': '1',
        'cy': '1',
        'cye': 'shanghai',
        '_lxsdk_s': '16c88af9df2-b88-5cb-b11%7C%7C116',
        's_ViewType': '10',
        '_hc.v': '7509c902-6550-1fbc-56e7-1622d5263ab3.1565612353',
        '_lxsdk': '16c85c4a768c8-0ffb41473819238-3f616c4d-fa000-16c85c4a768c8',
        '_lxsdk_cuid': '16c85c4a768c8-0ffb41473819238-3f616c4d-fa000-16c85c4a768c8'
    }

    # 该url可以测试 header 是否生效
    # print(requests.get("https://www.whatismybrowser.com/detect/what-http-headers-is-my-browser-sending", headers=headers).text)

    # response = requests.get(url, headers=headers, proxies=proxies, timeout=3)

    retry_times = 0
    while retry_times < 3:
        # proxies = [{'http': 'http://106.12.39.147:8899','https': 'http://106.12.39.147:8899'}]

        # 122.245.158.18 | 60.179.66.187 | 60.179.64.87 | 122.245.251.216 | 183.135.2.80 | 220.189.2.246
        # 122.245.110.163 | 115.217.44.148 | 122.245.157.228 | 183.135.2.12
        proxies = [{'http': 'http://183.135.2.12:32982','https': 'http://183.135.2.12:32982'}]

        # proxies = [{'http': 'http://106.12.39.147:8899','https': 'http://106.12.39.147:8899'},
        #            {'http': 'http://125.114.174.50:8888','https': 'http://125.114.174.50:8888'}]

        # 动态设置代理 IP
        # proxies = {'http': 'http://125.114.174.50:8888',
        #            'https': 'http://125.114.174.50:8888'}

        # print(retry_times)
        proxy_ip = random.choice(proxies)
        # print(proxy_ip)

        try:
            response = requests.get(url, headers=headers, proxies=proxy_ip, timeout=5, cookies=cookies)

            # print(response.cookies)
            print("-"*20)
            print(response.headers)
            print(response.request.headers)
            print("-"*20)
            # response = requests.get(url, headers=headers, timeout=100)
            return response
        except requests.exceptions.ConnectionError as e:
            retry_times = retry_times + 1
            # print("重试第%d"%retry_times,"报错了", e)
        except requests.exceptions.ReadTimeout as e:
            retry_times = retry_times + 1
            # print("重试第%d"%retry_times,"报错了", e)

    return None

    # # 休眠
    # sleep_time = random.uniform(0, 3)
    # # print("休眠", sleep_time)
    # time.sleep(sleep_time)

def requests_dianping(url):
    """
    封装 requests 模块
    :param url:
    :return:
    """
    # 动态加载 user_agent
    # user_agent = [
    #     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36",
    #     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
    #     "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36",
    #     "Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"
    # ]

    user_agent = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1 Safari/605.1.15"]

    # 封装请求头
    headers = dict()
    headers['User-Agent'] = random.choice(user_agent)
    headers["Connection"] = "keep-alive"
    # headers["Connection"] = "close"
    # headers["Accept"] = "text/plain, */*; q=0.01"
    headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
    headers["Accept-Encoding"] = "gzip, deflate, br"
    headers["Accept-Language"] = "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7"
    headers["Host"] = "www.dianping.com"

    # headers["Referer"] = "http://www.dianping.com/shop/98440846"
    # headers["X-Requested-With"] = "XMLHttpRequest"

    # headers["Origin"] = "http://www.dianping.com"

    # headers["Cookie"] = "s_ViewType=10; _lxsdk_cuid=16c8497049fc8-06b5f179e16f2a-38617706-fa000-16c8497049f7c; _lxsdk=16c8497049fc8-06b5f179e16f2a-38617706-fa000-16c8497049f7c; _hc.v=73305ac3-2ce0-dd8b-4f94-0abcc3c130cd.1565592585; _lxsdk_s=16c849704a2-56a-f51-096%7C%7C19"

    # headers["Cookie"] = "_lxsdk_cuid=16aa0e13385c8-09565305c22591-37607604-232800-16aa0e13385c8; _lxsdk=16aa0e13385c8-09565305c22591-37607604-232800-16aa0e13385c8; _hc.v=2c408a18-4187-b4d2-0016-76ee91ea5b15.1557477275; Hm_lvt_e6f449471d3527d58c46e24efb4c343e=1557477275; cy=1; cye=shanghai; s_ViewType=10; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_s=16c849faad8-d0a-305-56d%7C%7C512"

    # headers["Cookie"] = "_lxsdk_cuid=16c8524c06dc8-0fbfa373eef812-38617706-fa000-16c8524c06ec8;" \
    #                     "_lxsdk=16c8524c06dc8-0fbfa373eef812-38617706-fa000-16c8524c06ec8;" \
    #                     "_lxsdk_s=16c8524c071-661-79f-9eb%7C%7C1;" \
    #                     "_hc.v=4f73dde6-e19c-aa5f-664d-293fffc68ba6.1565601874"


    # headers["Cookie"] = "cityid=1; cy=1; cye=shanghai; _lxsdk_s=16c85c4a76a-7cc-56-e61%7C%7C124; _hc.v=7509c902-6550-1fbc-56e7-1622d5263ab3.1565612353; _lxsdk=16c85c4a768c8-0ffb41473819238-3f616c4d-fa000-16c85c4a768c8; _lxsdk_cuid=16c85c4a768c8-0ffb41473819238-3f616c4d-fa000-16c85c4a768c8"


    # cookies = {"cityid=1; cy=1; cye=shanghai; _lxsdk_s=16c85c4a76a-7cc-56-e61%7C%7C124;
    # _hc.v=7509c902-6550-1fbc-56e7-1622d5263ab3.1565612353; _lxsdk=16c85c4a768c8-0ffb41473819238-3f616c4d-fa000-16c85c4a768c8;
    # _lxsdk_cuid=16c85c4a768c8-0ffb41473819238-3f616c4d-fa000-16c85c4a768c8"}


    with open('incre_cookid') as f1:
        incre_value = f1.read()
    with open('incre_cookid', 'w') as f:
        f.write(str(int(incre_value) + 3))

    # print(incre_value)
    cookies = {
        'cityid': '1',
        'cy': '1',
        'cye': 'shanghai',
        '_lxsdk_s': '16c88af9df2-b88-5cb-b11%7C%7C' + incre_value,
        's_ViewType': '10',
        '_hc.v': '7509c902-6550-1fbc-56e7-1622d5263ab3.1565612353',
        '_lxsdk': '16c85c4a768c8-0ffb41473819238-3f616c4d-fa000-16c85c4a768c8',
        '_lxsdk_cuid': '16c85c4a768c8-0ffb41473819238-3f616c4d-fa000-16c85c4a768c8'
    }

    # print(cookies)
    # 该url可以测试 header 是否生效
    # print(requests.get("https://www.whatismybrowser.com/detect/what-http-headers-is-my-browser-sending", headers=headers).text)

    # response = requests.get(url, headers=headers, proxies=proxies, timeout=3)

    retry_times = 0
    while retry_times < 3:
        # proxies = [{'http': 'http://106.12.39.147:8899','https': 'http://106.12.39.147:8899'}]

        # 122.245.158.18 | 60.179.66.187 | 60.179.64.87 | 122.245.251.216 | 183.135.2.80 | 220.189.2.246
        # 122.245.110.163 | 115.217.44.148 | 122.245.157.228 | 183.135.2.12 | 115.213.25.214 | 122.246.251.0
        proxies = [{'http': 'http://122.246.251.0:32982','https': 'http://122.246.251.0:32982'}]



        # proxies = [{'http': 'http://106.12.39.147:8899','https': 'http://106.12.39.147:8899'},
        #            {'http': 'http://125.114.174.50:8888','https': 'http://125.114.174.50:8888'}]

        # 动态设置代理 IP
        # proxies = {'http': 'http://125.114.174.50:8888',
        #            'https': 'http://125.114.174.50:8888'}

        # print(retry_times)
        proxy_ip = random.choice(proxies)
        # print(proxy_ip)

        try:
            # # 休眠
            sleep_time = random.uniform(2, 4)
            print("休眠", sleep_time)
            time.sleep(sleep_time)


            response = requests.get(url, headers=headers, proxies=proxy_ip, timeout=5, cookies=cookies)

            # print(response.cookies)
            # print("-"*20)
            # print(response.headers)
            # print(response.request.headers)
            # print("-"*20)
            # response = requests.get(url, headers=headers, timeout=100)
            return response
        except requests.exceptions.ConnectionError as e:
            retry_times = retry_times + 1
            # print("重试第%d"%retry_times,"报错了", e)
        except requests.exceptions.ReadTimeout as e:
            retry_times = retry_times + 1
            # print("重试第%d"%retry_times,"报错了", e)

    return None

def requests_dianping2(url):
    """
    封装 requests 模块
    :param url:
    :return:
    """
    # 动态加载 user_agent
    user_agent = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1 Safari/605.1.15"]

    # 封装请求头
    headers = dict()
    headers['User-Agent'] = random.choice(user_agent)
    headers["Connection"] = "keep-alive"
    headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
    headers["Accept-Encoding"] = "gzip, deflate"
    headers["Accept-Language"] = "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7"
    headers["Host"] = "www.dianping.com"

    headers["Accept-Language"] = "zh-cn"
    headers["Upgrade-Insecure-Requests"] = "1"

    headers["Cache-Control"] = "max-age=0"

    with open('incre_cookid_detail') as f1:
        incre_value2 = f1.read()
    with open('incre_cookid_detail', 'w') as f:
        f.write(str(int(incre_value2) + 2))

    cookies = {
        'cityid': '1',
        'cy': '1',
        'cye': 'shanghai',
        '_lxsdk_s': '16c8a77a039-155-fc2-94e%7C%7C' + incre_value2,
        's_ViewType': '10',
        '_hc.v': 'a31cc9e4-e038-f8fb-686f-00f08c972906.1565680731',
        '_lxsdk': '16c89d80035c8-00633b53efe6478-3f616c4d-fa000-16c89d80036c8',
        '_lxsdk_cuid': '16c8524c06dc8-0fbfa373eef812-38617706-fa000-16c8524c06ec8',
        # '_lxsdk_cuid': '16c8526c06dc8-0fbfa373eef812-38617706-fa000-16c8524c06ec8',
        '_lx_utm': 'utm_source%3DBaidu%26utm_medium%3Dorganic',
        'cy': '1',
        'cye': 'shanghai',
        # 'aburl': '1'
    }

    # _lxsdk_cuid=; _lxsdk=16c8524c06dc8-0fbfa373eef812-38617706-fa000-16c8524c06ec8; _hc.v=4f73dde6-e19c-aa5f-664d-293fffc68ba6.1565601874; cy=1; cye=shanghai; s_ViewType=10; aburl=1; _lxsdk_s=16c8a97ac85-faa-9b0-72%7C%7C6

    retry_times = 0
    while retry_times < 3:
        # proxies = [{'http': 'http://106.12.39.147:8899','https': 'http://106.12.39.147:8899'}]

        # 122.245.158.18 | 60.179.66.187 | 60.179.64.87 | 122.245.251.216 | 183.135.2.80 | 220.189.2.246
        # 122.245.110.163 | 115.217.44.148 | 122.245.157.228 | 183.135.2.12 | 115.213.25.214 | 122.246.251.0
        # 122.245.156.30 | 60.178.217.81 | 60.178.216.118 | 122.245.111.242 | 122.245.250.225 | 122.245.250.225
        # 115.217.47.91 | 60.179.66.26 | 122.246.250.171 | 183.135.84.208 | 125.116.191.69 | 183.135.4.74
        # 60.178.216.40 | 122.245.152.122 | 60.178.91.225 | 60.178.216.158 | 122.245.154.22 | 183.135.7.185
        proxies = [{'http': 'http://115.213.57.162:32982','https': 'http://115.213.57.162:32982'}]

        proxy_ip = random.choice(proxies)

        try:
            # 休眠
            # sleep_time = random.uniform(3, 9)
            # print("休眠", sleep_time)
            # time.sleep(sleep_time)

            # sleep_time = random.uniform(3, 5)
            # print("休眠", sleep_time)
            # time.sleep(sleep_time)


            response = requests.get(url, headers=headers, proxies=proxy_ip, timeout=10, cookies=cookies)

            # response = requests.get(url, headers=headers,  timeout=10, cookies=cookies)

            # print(response.cookies)
            print("-"*20)
            print(response.headers)
            print(response.request.headers)
            print("-"*20)
            return response
        except requests.exceptions.ConnectionError as e:
            retry_times = retry_times + 1
            # print("重试第%d"%retry_times,"报错了", e)
        except requests.exceptions.ReadTimeout as e:
            retry_times = retry_times + 1
            # print("重试第%d"%retry_times,"报错了", e)

    return None

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


def sub_rect_baidu():

    geo_list = list()

    # 切分行列数
    # split_x = 5
    # split_y = 5

    split_x = 7
    split_y = 7


    # start_rect_geo = {'left_bottom':{'x':0,'y':0}, 'right_top':{'x':6,'y':6}}
    # start_rect_geo = {'left_bottom':{'x':119.58962425017401,'y':29.02371358317696},
    #                   'right_top':{'x':119.787499394624553,'y':29.149153586357146}}

    start_rect_geo = {'left_bottom':{'x':119.999705,'y':30.083411},
                      'right_top':{'x':120.15292,'y':30.3649}}

    start_left_x = start_rect_geo['left_bottom']['x']
    start_left_y = start_rect_geo['left_bottom']['y']

    width = abs(start_rect_geo['left_bottom']['x'] - start_rect_geo['right_top']['x'])
    height = abs(start_rect_geo['left_bottom']['y'] - start_rect_geo['right_top']['y'])

    width_step = width / (split_x + 1)
    height_step = height / (split_y + 1)


    # print(width,height)
    # print(a['left']['x'])

    each_y = start_left_y
    sub_y_bottom = each_y # 初始y坐标

    for y in range(split_y + 1):
        sub_x_bottom = start_left_x
        # each_y = start_left_y


        for x in range(split_x + 1):
            # geo_x = sub_x_bottom + width_step

            sub_x_top = sub_x_bottom + width_step
            sub_y_top = sub_y_bottom + height_step
            # print((sub_x_bottom, sub_y_bottom), (sub_x_top, sub_y_top))

            str_geo = '%s,%s,%s,%s'%(round(sub_y_bottom,6),round(sub_x_bottom,6),round(sub_y_top,6),round(sub_x_top,6))
            # print('%s,%s,%s,%s'%(round(sub_y_bottom,6),round(sub_x_bottom,6),round(sub_y_top,6),round(sub_x_top,6)))

            geo_list.append(str_geo)
            sub_x_bottom += width_step

        # print("-"*20)

        sub_y_bottom += height_step


    return geo_list



if __name__ == '__main__':
    # result = requests_dianping("http://icanhazip.com")
    # # # result = requests_utils("http://www.baidu.com")
    # if result is None:
    #     print(result)
    # else:
    #     print(result.text)
    # print(result.text)

    # ll = sub_rect_baidu()
    #
    # print(len(ll))

    # url = "http://www.dianping.com/search/keyword/1/0_美容医院"
    # url = "http://www.dianping.com/shanghai/ch50/g183"
    # url = "http://www.dianping.com/shop/98440846"

    # url = "http://m.dianping.com/beauty/book/bookphoneno/show?attachtype=0"

    url = "http://www.dianping.com/shop/126746440"
    res = requests_dianping2(url)

    print(res.text)

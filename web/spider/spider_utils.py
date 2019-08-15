# -*- coding:utf-8 -*-
import requests
import json
import time
from bs4 import BeautifulSoup
import random
import time
import datetime
import os
import socket
from spider import selenium_utils

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
        if incre_value2.isdigit():
            f.write(str(int(incre_value2) + 3))
        else:
            f.write(str(5))

    # cookies = {
    #     'cityid': '1',
    #     'cy': '1',
    #     'cye': 'shanghai',
    #     # '_lxsdk_s': '16c8ee18d0b-af3-e43-aec%7C%7C' + incre_value2,
    #     '_lxsdk_s': '16c8f9683e2-3ad-e9c-532%7C%7C' + incre_value2,
    #     # 16c8f52a0be-3-89d-f61%7C%7C10
    #     's_ViewType': '10',
    #     '_hc.v': 'ccf4c4c1-f8b1-1084-e507-91fd9af023d3.1565777109',
    #     # 25635510-2672-561a-5658-3dd380ba2dbd.1565772653
    #     '_lxsdk': '16c8f96a0e4c8-00042c829b81f28-3f616c4d-fa000-16c8f96a0e484',
    #     # 16c8f52a0bbb-0d9a27cc52c9c5-3f616c4d-fa000-16c8f52a0bcc8
    #     '_lxsdk_cuid': '16c8f96a0e4c8-00042c829b81f28-3f616c4d-fa000-16c8f96a0e484',
    #     '_lx_utm': 'utm_source%3DBaidu%26utm_medium%3Dorganic',
    #     # utm_source%3DBaidu%26utm_medium%3Dorganic
    #     'cy': '1',
    #     'cye': 'shanghai',
    #     # 'aburl': '1'
    # }

    # cookies = {'_lxsdk_s': '16c92f80f4a-de8-0ec-d09%7C%7C1', '_hc.v': '8d075aa4-9b5c-9731-6aa6-a14a4fcb663b.1565833827', '_lxsdk_cuid': '16c92f80f48c8-07bc01b67895d4-38617706-fa000-16c92f80f48c8', '_lxsdk': '16c92f80f48c8-07bc01b67895d4-38617706-fa000-16c92f80f48c8', 'cye': 'shanghai', 'cityid': '1', 'cy': '1'}


    # 获取最新的IP地址
    with open("ip_proxy") as f:

        all_ip = ""
        try:
            all_ip = f.readlines()
        except Exception as e:
            print(e)

        new_ip = all_ip[-1].strip()

        if new_ip.find("重复IP") == 0:
            new_ip = change_ip()

        ip_res = test_ip(new_ip)
        cookies = eval(str(all_ip[1]).strip("\n"))
        cookies['_lxsdk_s'] = str(cookies['_lxsdk_s'])[:-1] + str(incre_value2)
        print("cookies-----", cookies)
        print(cookies['_lxsdk_s'])

        if ip_res !=0:
            print("该IP无效重试 ", new_ip)
            change_ip()
            requests_dianping2(url)
        else:
            print("该IP有效 ", new_ip)
            retry_times = 0
            while retry_times < 3:
                # proxies = [{'http': 'http://106.12.39.147:8899','https': 'http://106.12.39.147:8899'}]

                ip_dict = {
                    'http': 'http://%s:32982'% new_ip,
                    'https': 'http://%s:32982'% new_ip
                }
                # proxies = [{'http': 'http://115.217.47.39:32982','https': 'http://115.217.47.39:32982'}]
                proxies = [ip_dict]
                proxy_ip = random.choice(proxies)

                print(proxy_ip)
                try:
                    # 休眠
                    # sleep_time = random.uniform(3, 9)
                    # print("休眠", sleep_time)
                    # time.sleep(sleep_time)

                    # sleep_time = random.uniform(2, 4)
                    # print("休眠", sleep_time)
                    # time.sleep(sleep_time)

                    print("---335555---", cookies)
                    response = requests.get(url, headers=headers, proxies=proxy_ip, timeout=10, cookies=cookies)
                    # response = requests.get(url, headers=headers, proxies=proxy_ip, timeout=10, cookies={"a1":"11"})
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

def change_ip():
    start_time = datetime.datetime.now()
    command_linux = "ssh root@122.227.184.61 -p20073 'sh restart_pp.sh'"
    str1 = os.popen(command_linux)
    res_ip = str1.read()
    end_time = datetime.datetime.now()

    cost_time = end_time - start_time

    with open("ip_proxy") as f_r:
        # ip_gen = "60.178.91.229"
        all_ip = f_r.read()
        #
        if all_ip.find(res_ip) == -1:
            with open("ip_proxy", "a+") as f_w:
                f_w.write(res_ip)
                print("更换IP,耗时", cost_time, res_ip)
                return res_ip
        else:
            with open("ip_proxy", "a+") as f_w:
                f_w.write("重复IP: " + res_ip)
            change_ip()

def change_ip_cookies(url_t):
    start_time = datetime.datetime.now()

    # 切换IP并解析
    command_linux = "ssh root@122.227.184.61 -p20073 'sh restart_pp.sh'"
    str1 = os.popen(command_linux)
    res_ip = str1.read()

    # 耗时
    end_time = datetime.datetime.now()
    cost_time = end_time - start_time

    # 生成cookies
    cookies = selenium_utils.no_delay_cookies(url_t)

    # 新生成的IP和Cookie写入文件
    with open("ip_proxy", "r+") as f_r:
        # ip_gen = "60.178.91.229"
        all_content = f_r.read()
        #
        if all_content.find(res_ip) == -1:
            f_r.seek(0, 0) # get to the first position
            f_r.write(str(cookies).rstrip("\r\n") + "\n" + all_content + str(res_ip))
            print("更换IP Cookie,耗时", cost_time, res_ip, cookies)
            return res_ip
        else:
            f_r.write("\n" + "重复IP: " + res_ip)
            change_ip()

def test_ip(ip_address):
    """
    测试该 IP + Port 是否有效
    :return: 0代表有效
    """
    print("490,测试IP", ip_address)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(3)
    try:
        ip_result = sock.connect_ex((ip_address, 32982))
    except Exception as e:
        ip_result = -1
        print(e)
    # if ip_result == 0:
    #     print("Port is open")
    # else:
    #     print("Port is not open")

    return ip_result


if __name__ == '__main__':
    # change_ip()
    # result = requests_dianping2("http://icanhazip.com")
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

    # url = "http://www.dianping.com/shop/126746440"
    # url = "http://www.dianping.com/shop/93764773"
    # res = requests_dianping2(url)
    # print(res.text)

    print(test_ip("115.217.45.0"))

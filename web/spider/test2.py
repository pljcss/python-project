import requests
from urllib import request
from http import cookiejar
import random
import os
import datetime
import socket


def get_cookies():
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

    headers["Referer"] = "http://www.dianping.com/shop/98440846"
    headers["X-Requested-With"] = "XMLHttpRequest"

    headers["Origin"] = "http://www.dianping.com"



    # 声明一个CookieJar对象实例来保存cookie
    cookie = cookiejar.CookieJar()
    #利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器,也就CookieHandler
    cookie_support = request.HTTPCookieProcessor(cookie)
    #通过CookieHandler创建opener
    opener = request.build_opener(cookie_support)
    #创建Request对象


    # http://www.dianping.com/shop/1705777
    # http://www.dianping.com/shop/98440846
    req1 = request.Request(url='http://www.dianping.com/shop/98440846', headers=headers)
    response1 = opener.open(req1)
    html = response1.read().decode('utf-8')
    return html

def test(ip_dynamic):
    ip_dict = {
        'http': 'http://%s:32982'%ip_dynamic,
        'https': 'http://%s:32982'%ip_dynamic
    }

    print(ip_dict)
if __name__ == '__main__':
    # str1 = os.system('ls')
    # start_time = datetime.datetime.now()
    # command_linux = "ssh root@122.227.184.61 -p20073 'sh restart_pp.sh'"
    # str1 = os.popen(command_linux)
    # change_ip = str1.read()
    # end_time = datetime.datetime.now()
    #
    # cost_time = end_time - start_time
    # print("耗时", cost_time, change_ip)

    pass

    url = 'http://www.dianping.com/'
    # headers = {'Upgrade-Insecure-Requests':'1',
    #            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    #            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    #            'Accept-Encoding':'gzip, deflate, sdch, br',
    #            'Accept-Language':'zh-CN,zh;q=0.8',
    #            }


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

    headers["Referer"] = "http://www.dianping.com/shop/98440846"
    headers["X-Requested-With"] = "XMLHttpRequest"

    headers["Origin"] = "http://www.dianping.com"
    s = requests.Session()
    req = s.get(url=url,headers=headers)
    print(s.cookies)


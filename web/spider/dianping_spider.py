# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
from spider import spider_utils, selenium_utils
import logging.config
import re
import requests
from selenium import webdriver
import os

logging.config.fileConfig('log.ini')
file_logger = logging.getLogger(name="fileLogger")

def get_dianping_url(url):
    """
    获取大众点评数据 url
    :return:
    """
    # url = "http://www.dianping.com/search/keyword/1/0_美容医院"

    # url = "http://www.dianping.com/shanghai/ch50/g183"
    # response = spider_utils.requests_dianping(url)
    # # print(response.text)
    #
    # soup = BeautifulSoup(response.text, features="lxml")
    #
    # # 存储获取到的url
    # url_set = set([])
    # for link in soup.find_all("a"):
    #     ll =  link.get("href")
    #
    #     # 获取满足条件的url
    #     if isinstance(ll, str):
    #         # print(ll)
    #         # print(ll.find("http://www.dianping.com/shop"))
    #         if ll.find("http://www.dianping.com/shop") == 0 and ll.find("#")==-1:
    #             # print(ll)
    #             if ll.find("review") == -1:
    #                 url_set.add(ll)
    #
    # return url_set

    # url = "http://www.dianping.com/shanghai/ch50/g183"

    response = spider_utils.requests_dianping2(url)
    # print(response.text)

    soup = BeautifulSoup(response.text, features="lxml")

    # 存储获取到的url
    url_set = set([])
    for link in soup.find_all("a"):
        ll =  link.get("href")

        # 获取满足条件的url
        if isinstance(ll, str):
            # print(ll)
            # print(ll.find("http://www.dianping.com/shop"))
            if ll.find("http://www.dianping.com/shop") == 0 and ll.find("#")==-1:
                # print(ll)
                if ll.find("review") == -1:
                    url_set.add(ll)

    return url_set

def parse_dianping_url():
    """
    解析大众点评 url
    :return:
    """
    # url_set = get_dazhong_url()

    url_set = {'http://www.dianping.com/shop/98440846', 'http://www.dianping.com/shop/68960534',
               'http://www.dianping.com/shop/20816759', 'http://www.dianping.com/shop/92726325',
               'http://www.dianping.com/shop/77220510', 'http://www.dianping.com/shop/72448927',
               'http://www.dianping.com/shop/58387941', 'http://www.dianping.com/shop/23510196',
               'http://www.dianping.com/shop/98632891', 'http://www.dianping.com/shop/23123189',
               'http://www.dianping.com/shop/90058481', 'http://www.dianping.com/shop/14894422',
               'http://www.dianping.com/shop/92197169', 'http://www.dianping.com/shop/22799131',
               'http://www.dianping.com/shop/8984185'}


    all_page_links = get_all_page_links()

    for url in all_page_links:
        every_page_links_set = get_dianping_url(url)

        for url_detail in every_page_links_set:

            # response = spider_utils.requests_dianping("http://www.dianping.com/shop/98440846")

            response = spider_utils.requests_dianping(url_detail)
            soup = BeautifulSoup(response.text, features="lxml")

            # print(response.text)
            # 医院名
            hospital_name, b = soup.find("h1").stripped_strings
            print(hospital_name)

            # 地址
            address = ""
            for i in soup.find("div", attrs={"class":"expand-info address"}).find_all("span"):
                address += (str(i.get_text()).strip())
            print(address)

            # 电话
            tel = str(soup.find("p", attrs={"class":"expand-info tel"}).find("span", "item").get_text()).strip()
            print(tel)

            # 星级
            stars_str = soup.find("div", attrs={"class":"brief-info"}).find_all("span")[0]

            print(stars_str)
            score = re.findall(r"\d+\.?\d*",str(stars_str).strip())[0]
            print(score)
            #
            # print(hospital_name, address, tel, score)




    # with open("/Users/caosai/Desktop/test.html") as f:
    #     html = f.read()
    #     soup = BeautifulSoup(html, features="lxml")
    #
    #     # print(soup.select("h1"))
    #
    #     # print(soup.find_all("h1", attrs={"class":"shop-name"}))
    #     #
    #     # print(soup.find_all("h1", "shop-name"))
    #
    #     # for ll in soup.find_all("h1", "shop-name"):
    #     #     print(type(ll))
    #     #     a, b = ll.stripped_strings
    #     #     print(a)
    #
    #     # 医院名
    #     hospital_name, b = soup.find("h1").stripped_strings
    #     print(hospital_name)
    #
    #     # 地址
    #     address = ""
    #     for i in soup.find("div", attrs={"class":"expand-info address"}).find_all("span"):
    #         address += (str(i.get_text()).strip())
    #     print(address)
    #
    #     # 电话
    #     tel = str(soup.find("p", attrs={"class":"expand-info tel"}).find("span", "item").get_text()).strip()
    #     print(tel)
    #
    #     print(hospital_name, address, tel)

def parse_dianping_url2(url2):
    """
    解析大众点评 url
    :return:
    """
    response = spider_utils.requests_dianping2(url2)

    # print(response.text)
    # if response is not None and response.text.find("地址不对") == -1:
    #     print('---161----')
    #     soup = BeautifulSoup(response.text, features="lxml")
    #     # print(response.text)
    #
    #     # 如果counter_none 值为4,则说明IP被封,需更换IP
    #     counter_none = 0
    #
    #     # 医院名
    #     hospital_name = ""
    #     try:
    #         hospital_name, b = soup.find("h1").stripped_strings
    #         # print(hospital_name)
    #     except Exception as e:
    #         counter_none += 1
    #         print(e)
    #
    #     # 地址
    #     address = ""
    #     try:
    #         for i in soup.find("div", attrs={"class":"expand-info address"}).find_all("span"):
    #             address += (str(i.get_text()).strip())
    #         # print(address)
    #     except Exception as e:
    #         counter_none += 1
    #         print(e)
    #
    #     # 电话
    #     tel = ""
    #     try:
    #         tel = str(soup.find("p", attrs={"class":"expand-info tel"}).find("span", "item").get_text()).strip()
    #         # print(tel)
    #     except Exception as e:
    #         counter_none += 1
    #         print(e)
    #
    #     # 星级
    #     score = ""
    #     try:
    #         stars_str = soup.find("div", attrs={"class":"brief-info"}).find_all("span")[0]
    #         score = re.findall(r"\d+\.?\d*",str(stars_str).strip())[0]
    #     except Exception as e:
    #         counter_none += 1
    #         print(e)
    #
    #     # 检测IP是否被封
    #     if counter_none == 4:
    #         print("IP-Cookie失效, 更换....")
    #         # selenium
    #         # cookies = selenium_utils.no_delay_cookies(url)
    #         # print(cookies)
    #
    #         spider_utils.change_ip_cookies(url2)
    #         # spider_utils.change_ip()
    #         print("重新执行该方法")
    #         return parse_dianping_url2(url2)
    #     else:
    #         print('---217----')
    #         str2 = url2 + "^" + hospital_name + "^" + address + "^" + tel + "^" + score
    #         print(hospital_name, address, tel, score)
    #
    #         return str2
    #         # with open("dianping_data_huangpu_spa.txt", "a+") as f:
    #         #     f.write(str2 + "\n")

    # print(response.text)
    # 不能这样使用地址不对,因为本中可能存在这种值
    # if response is not None and response.text.find("地址不对") == -1:
    if response is not None:
        soup = BeautifulSoup(response.text, features="lxml")
        # print(response.text)

        # 如果counter_none 值为4,则说明IP被封,需更换IP
        counter_none = 0

        # 医院名
        hospital_name = ""
        try:
            hospital_name, b = soup.find("h1").stripped_strings
            # print(hospital_name)
        except Exception as e:
            counter_none += 1
            print(e)

        # 地址
        address = ""
        try:
            for i in soup.find("div", attrs={"class":"expand-info address"}).find_all("span"):
                address += (str(i.get_text()).strip())
                # print(address)
        except Exception as e:
            counter_none += 1
            print(e)

        # 电话
        tel = ""
        try:
            tel = str(soup.find("p", attrs={"class":"expand-info tel"}).find("span", "item").get_text()).strip()
            # print(tel)
        except Exception as e:
            counter_none += 1
            print(e)

        # 星级
        score = ""
        try:
            stars_str = soup.find("div", attrs={"class":"brief-info"}).find_all("span")[0]
            score = re.findall(r"\d+\.?\d*",str(stars_str).strip())[0]
        except Exception as e:
            counter_none += 1
            print(e)

        # 检测IP是否被封
        if counter_none == 4:
            print("IP-Cookie失效, 更换....")
            # selenium
            # cookies = selenium_utils.no_delay_cookies(url)
            # print(cookies)

            spider_utils.change_ip_cookies(url2)
            # spider_utils.change_ip()
            print("重新执行该方法")
            return parse_dianping_url2(url2)
        else:
            print('---217----')
            str2 = url2 + "^" + hospital_name + "^" + address + "^" + tel + "^" + score
            print(hospital_name, address, tel, score)

            return str2
            # with open("dianping_data_huangpu_spa.txt", "a+") as f:
            #     f.write(str2 + "\n")
    else:
        print('#'*20)
        return parse_dianping_url2(url2)

def get_all_page_links():

    url_start = "http://www.dianping.com/hangzhou/ch50/g158r8845"
    url_list = list()
    url_list.append(url_start)

    for i in range(50):
        if i > 0:
            # url_former = "http://www.dianping.com/beijing/ch50/g158r5950p" + str(i+1) + "?cpt=5220127%2C19813864"
            url_former = url_start + "p" + str(i+1)
            url_list.append(url_former)

    return url_list

def get_all_detail_page_links():
    ########### 1、将url写入文件 ###############
    province = '浙江省'
    city = '杭州市'
    region = '余杭区'

    str1 = ""
    for i in get_all_page_links():
        print(i)
        url_sets = get_dianping_url(i)

        for res in url_sets:
            print(res)
            str1 = str1 + province + '^' + city + '^' + region + '^' + res + "\n"

    with open("url_all.txt", "a+") as f:
        f.write(str1)
    ########### 1、将url写入文件 ###############

if __name__ == '__main__':
    # get_all_detail_page_links()
    # print(get_dianping_url("http://www.dianping.com/shanghai/ch50/g183"))

    # 获取所有页面主链接
    # print(get_all_page_links())

    get_all_detail_page_links()

    # with open("url_all.txt") as f:
    #     file_path = "dianping_hangzhou_data_spa.txt"
    #
    #     counter = 1
    #     flag = False
    #     last_one_url = ""
    #     if os.path.exists(file_path):
    #         with open(file_path) as f2:
    #             last_one_url = f2.readlines()[-1].split('^')[3]
    #     else:
    #         flag = True
    #
    #     for line in f.readlines():
    #         province = line.strip().split('^')[0]
    #         city = line.strip().split('^')[1]
    #         region = line.strip().split('^')[2]
    #         url = line.strip().split('^')[3]
    #
    #         if last_one_url == url:
    #             flag = True
    #             continue
    #
    #         if flag is True:
    #             print("开始解析第%d行, %s"%(counter, url))
    #             str2 = province + '^' + city + '^' + region + '^' + parse_dianping_url2(url)
    #
    #             with open(file_path, "a+") as f2:
    #                 f2.write(str2 + "\n")
    #             # print(url)
    #             # if counter%150 == 0:
    #             #     print("切换")
    #             #     spider_utils.change_ip()
    #             print("结束解析----------" + '\n')
    #
    #             counter +=1
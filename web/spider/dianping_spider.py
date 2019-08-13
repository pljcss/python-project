# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
from spider import spider_utils
import logging.config
import re
import requests

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
            str_digtial = re.findall(r"\d+\.?\d*",str(stars_str).strip())[0]
            print(str_digtial)
            #
            # print(hospital_name, address, tel, str_digtial)




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
    soup = BeautifulSoup(response.text, features="lxml")

    # print(response.text)

    # 医院名
    hospital_name = ""
    try:
        hospital_name, b = soup.find("h1").stripped_strings
        # print(hospital_name)
    except Exception as e:
        print(e)


    # 地址
    address = ""
    try:
        for i in soup.find("div", attrs={"class":"expand-info address"}).find_all("span"):
            address += (str(i.get_text()).strip())
        # print(address)
    except Exception as e:
        print(e)

    # 电话
    tel = ""
    try:
        tel = str(soup.find("p", attrs={"class":"expand-info tel"}).find("span", "item").get_text()).strip()
        # print(tel)
    except Exception as e:
        print(e)

    # 星级
    str_digtial = ""
    try:
        stars_str = soup.find("div", attrs={"class":"brief-info"}).find_all("span")[0]
        str_digtial = re.findall(r"\d+\.?\d*",str(stars_str).strip())[0]
    except Exception as e:
        print(e)


    str2 = url2 + "^" + hospital_name + "^" + address + "^" + tel + "^" + str_digtial
    print(hospital_name, address, tel, str_digtial)

    with open("dianping_data_changning_spa.txt", "a+") as f:
        f.write(str2 + "\n")

def get_all_page_links():

    # http://www.dianping.com/shanghai/ch50/g158r4
    # http://www.dianping.com/shanghai/ch50/g158r4p2
    # http://www.dianping.com/shanghai/ch50/g158r4p50

    url_start = "http://www.dianping.com/shanghai/ch50/g158r4"
    url_list = list()
    url_list.append(url_start)

    for i in range(50):
        if i > 0:
            url_former = "http://www.dianping.com/shanghai/ch50/g158r4p" + str(i+1)
            url_list.append(url_former)

    return url_list

if __name__ == '__main__':
    # print(get_dianping_url("http://www.dianping.com/shanghai/ch50/g183"))

    ########### 1、将url写入文件 ###############
    # str1 = ""
    # for i in get_all_page_links():
    #     print(i)
    #     url_sets = get_dianping_url(i)
    #
    #     for res in url_sets:
    #         print(res)
    #         str1 = str1 + res + "\n"
    #
    # with open("url_all.txt", "a+") as f:
    #     f.write(str1)
    ########### 1、将url写入文件 ###############


    with open("url_all.txt") as f:
        for line in f.readlines():
            url = line.strip()

            print("开始解析:::", url)
            parse_dianping_url2(url)
            # print(url)
            print("结束解析----------" + '\n')



    # print(get_all_page_links())
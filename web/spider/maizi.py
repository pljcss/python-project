# -*- coding:utf-8 -*-
import requests
import json
import time
from bs4 import BeautifulSoup
import random
from spider import spiderUtils


def get_content_from_baidu(page_size=20, page_num=0):
    """
    百度地图接口
    :param page_size:
    :param page_num:
    :return:
    """

    ak = "HSpG2oGjxfDeFyLamp89ENfQ3gXckMzG"
    url = "http://api.map.baidu.com/place/v2/search?query=医院&region=浦东新区&output=json&ak=%s&page_size=%d&page_num=%d" %(ak, page_size, page_num)

    # 返回结果
    res = requests.get(url)
    # print(res.text)

    # 转成json
    json_res = json.loads(res.text)

    # 查询到的总数
    total_results = json_res["total"]

    page_num = total_results / page_size

    for i in range(int(page_num)):
        page_num = i
        url = "http://api.map.baidu.com/place/v2/search?query=医院&region=浦东新区&output=json&ak=%s&page_size=%d&page_num=%d" %(ak, page_size, page_num)
        # time.sleep(5)
        res = requests.get(url)
        json_res = json.loads(res.text)

        print(json_res)

        # print(i)
        # print(url)
        try:
            for i in json_res["results"]:
                # print(type(i))
                print(i["name"], i["location"], i["address"], i["telephone"])
        except Exception as e:
            print(e)


def get_content_from_gaode():
    """
    高德地图接口
    :return:
    """

    ak = "610479fef7daa6a9a1291889c357a0e0"
    keyword = "医院"
    city = "浦东新区"
    url = "https://restapi.amap.com/v3/place/text?key=%s&keywords=%s&city=%s" % (ak, keyword, city)

    response = requests.get(url)

    print(response.text)


def get_dazhong_url():
    """
    获取大众点评数据 url
    :return:
    """
    url = "http://www.dianping.com/search/keyword/1/0_美容医院"

    response = spiderUtils.requests_utils(url)
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
                url_set.add(ll)


    return url_set



def parse_dazhong_url():
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

    for url in url_set:
        pass


    # response = spiderUtils.requests_utils("http://www.dianping.com/shop/98440846")

    with open("/Users/caosai/Desktop/test.html") as f:
        html = f.read()
        soup = BeautifulSoup(html, features="lxml")

        # print(soup.select("h1"))

        # print(soup.find_all("h1", attrs={"class":"shop-name"}))
        #
        # print(soup.find_all("h1", "shop-name"))

        # for ll in soup.find_all("h1", "shop-name"):
        #     print(type(ll))
        #     a, b = ll.stripped_strings
        #     print(a)

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

        print(hospital_name, address, tel)


if __name__ == '__main__':
    parse_dazhong_url()
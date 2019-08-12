# -*- coding:utf-8 -*-
import requests
import json
import time
from bs4 import BeautifulSoup
import random
from spider import spider_utils
import logging
import logging.config
import csv

logging.config.fileConfig('log.ini')
file_logger = logging.getLogger(name="fileLogger")

def get_data_by_bounds(keywords, bounds, page_size=20, page_num=0):
    # ak = "HSpG2oGjxfDeFyLamp89ENfQ3gXckMzG" # self
    ak = "dASz7ubuSpHidP1oQWKuAK3q" # 链家ak
    url = "http://api.map.baidu.com/place/v2/search?" \
          "query=%s&" \
          "bounds=%s&" \
          "output=json&" \
          "scope=2&&ak=%s&" \
          "page_size=%d&" \
          "page_num=%d&" \
          "city_limit=true" \
          %(keywords, bounds, ak, page_size, page_num)

    res = None
    try:
        # 返回结果
        res = requests.get(url)
        # print(res.text)
    except Exception as e:
        file_logger.error("解析出错::: ", e)

    if res is not None:
        # 转成json
        json_res = json.loads(res.text)

        # 总页数
        total_results = json_res.get("total", 0)
        # print("总页数", total_results)
        file_logger.info("当前解析%s:%s, 共%d页"%(bounds, keywords, total_results))


        print(total_results)

        # 先查询出总页数, 然后分页查询
        page_num = total_results / page_size


        # 按页查询
        str2 = ""
        for i in range(int(page_num)):
            page_num = i
            # print("第一页, ", page_num)
            file_logger.info("爬取第%s页"%(page_num+1))

            url = "http://api.map.baidu.com/place/v2/search?" \
                  "query=%s&bounds=%s&output=json&scope=2&ak=%s&page_size=%d&page_num=%d&city_limit=true" \
                  %(keywords, bounds, ak, page_size, page_num)

            res = spider_utils.requests_utils(url)

            if res is not None:
                json_res = json.loads(res.text)
                # print(json_res)
                try:
                    for i in json_res["results"]:
                        str2 = str2 + str(i) + "\n"
                except Exception as e:
                    file_logger.error("报错了", e)

        # 将结果保存到文件
        with open("/Users/caosai/Desktop/lbs_all_杭州_split.txt", "a+") as f:
            f.write(str2)

def get_all_content_from_baidu(keywords, region, page_size=20, page_num=0):
    """
    百度地图接口
    :param keywords:
    :param region:
    :param page_size:
    :param page_num:
    :return:
    """
    # ak = "HSpG2oGjxfDeFyLamp89ENfQ3gXckMzG" # self
    ak = "dASz7ubuSpHidP1oQWKuAK3q" # 链家ak
    url = "http://api.map.baidu.com/place/v2/search?" \
          "query=%s&" \
          "region=%s&" \
          "output=json&" \
          "scope=2&&ak=%s&" \
          "page_size=%d&" \
          "page_num=%d&" \
          "city_limit=true" \
          %(keywords, region, ak, page_size, page_num)

    res = None
    try:
        # 返回结果
        res = requests.get(url)
        # print(res.text)
    except Exception as e:
        file_logger.error("解析出错::: ", e)

    if res is not None:
        # 转成json
        json_res = json.loads(res.text)

        # 总页数
        total_results = json_res.get("total", 0)
        # print("总页数", total_results)
        file_logger.info("当前解析%s:%s, 共%d页"%(region, keywords, total_results))

        # 先查询出总页数, 然后分页查询
        page_num = total_results / page_size


        # 按页查询
        str2 = ""
        for i in range(int(page_num)):
            page_num = i
            # print("第一页, ", page_num)
            file_logger.info("爬取第%s页"%(page_num+1))

            url = "http://api.map.baidu.com/place/v2/search?" \
                  "query=%s&region=%s&output=json&scope=2&ak=%s&page_size=%d&page_num=%d&city_limit=true" \
                  %(keywords, region, ak, page_size, page_num)

            res = spider_utils.requests_utils(url)

            if res is not None:


                try:
                    json_res = json.loads(res.text)
                    # print(json_res)
                    for i in json_res["results"]:
                        str2 = str2 + str(i) + "\n"
                except Exception as e:
                    file_logger.error("报错了", e)

        # 将结果保存到文件
        with open("/Users/caosai/Desktop/lbs_all_data.txt", "a+") as f:
            f.write(str2)


def write_csv(keywords, region, page_size=20, page_num=0):
    ak = "dASz7ubuSpHidP1oQWKuAK3q" # 链家ak
    url = "http://api.map.baidu.com/place/v2/search?" \
          "query=%s&region=%s&output=json&scope=2&&ak=%s&page_size=%d&page_num=%d" \
          %(keywords, region, ak, page_size, page_num)

    res = None
    try:
        # 返回结果
        res = requests.get(url)
        # print(res.text)
    except Exception as e:
        file_logger.error("解析出错::: ", e)

    if res is not None:
        # 转成json
        json_res = json.loads(res.text)

        # 总页数
        total_results = json_res.get("total", 0)
        # print("总页数", total_results)
        file_logger.info("当前解析%s:%s, 共%d页"%(region, keywords, total_results))

        # 先查询出总页数, 然后分页查询
        page_num = total_results / page_size

        # 按页查询
        str2 = ""
        res_list = list()
        for i in range(int(page_num)):
            page_num = i
            # print("第一页, ", page_num)
            file_logger.info("爬取第%s页"%(page_num+1))

            url = "http://api.map.baidu.com/place/v2/search?" \
                  "query=%s&region=%s&output=json&scope=2&ak=%s&page_size=%d&page_num=%d&city_limit=true" \
                  %(keywords, region, ak, page_size, page_num)

            res = spider_utils.requests_utils(url)

            if res is not None:
                json_res = json.loads(res.text)
                print(json_res)
                try:
                    for i in json_res["results"]:
                        str1 = i.get("name","0") + "^" + "null^" + i.get("telephone","0") + "^" + i.get("address","0") + "^" + i.get("province","0") + "^" \
                               + i.get("city","0") + "^" + i.get("area","0") + "^" + str(spider_utils.get_lng(i.get("location", "0"))) + "^" + str(spider_utils.get_lat(i.get("location", "0"))) + "^" \
                               + "null^" + "null^" + "null"

                        str2 = str2 + str1 + "\n"

                        res_dict = {"name":i.get("name","0"), "address":i.get("address","0"), "contact":i.get("telephone","0")}
                        res_list.append(res_dict)
                except Exception as e:
                    file_logger.error("报错了", e)

        # 将结果保存到文件
        with open("/Users/caosai/Desktop/lbs.csv", "a+") as f:
            headers = ['name', 'address', 'contact']
            f_csv = csv.DictWriter(f, headers)
            f_csv.writerows(res_list)
            # f.write(str2)

def get_content_from_baidu(keywords, region, page_size=20, page_num=0):
    """
    百度地图接口
    :param page_size:
    :param page_num:
    :return:
    """
    # ak = "HSpG2oGjxfDeFyLamp89ENfQ3gXckMzG"
    ak = "dASz7ubuSpHidP1oQWKuAK3q" # 链家ak
    # url = "http://api.map.baidu.com/place/v2/search?query=%s&region=%s&output=json&ak=%s&page_size=%d&page_num=%d" %(keywords, region, ak, page_size, page_num)
    url = "http://api.map.baidu.com/place/v2/search?query=%s&region=%s&output=json&scope=2&&ak=%s&page_size=%d&page_num=%d" %(keywords, region, ak, page_size, page_num)

    # 返回结果
    res = requests.get(url)
    # print(res.text)

    # 转成json
    json_res = json.loads(res.text)

    # 查询到的总数
    total_results = json_res.get("total", 0)
    # print("总页数", total_results)

    page_num = total_results / page_size

    str2 = ""
    for i in range(int(page_num)):
        page_num = i
        print("第一页, ", page_num)
        file_logger.info("爬取第%s页"%(page_num+1))

        url = "http://api.map.baidu.com/place/v2/search?query=%s&region=%s&output=json&ak=%s&page_size=%d&page_num=%d" %(keywords, region, ak, page_size, page_num)

        print("当前url%s"%url)
        # time.sleep(5)
        res = spider_utils.requests_utils(url)
        # res = requests.get(url)

        if res is not None:
            json_res = json.loads(res.text)

            # print(json_res)
            # print(i)
            # print(url)
            try:
                for i in json_res["results"]:
                    # print(i)
                    # print(type(i))
                    # str1 = i["name"] + "," + "null," + i["telephone"] + "," + i["address"] + "," + i["province"] + "," \
                    # + i["city"] + "," + i["area"] + "," + str(i["location"]["lng"]) + "," + str(i["location"]["lat"]) + "," \
                    # + "null," + "null," + "null"
                    # print(i["name"], i["location"], i["address"], i["telephone"],i["province"],i["city"],i["area"])

                    # str1 = i.get("name","0") + "," + "null," + i.get("telephone","0") + "," + i.get("address","0") + "," + i.get("province","0") + "," \
                    #        + i.get("city","0") + "," + i.get("area","0") + "," + str(spiderUtils.get_lng(i.get("location","0"))) + "," + str(spiderUtils.get_lat(i.get("location","0"))) + "," \
                    #        + "null," + "null," + "null"


                    str1 = i.get("name","0") + "^" + "null^" + i.get("telephone","0") + "^" + i.get("address","0") + "^" + i.get("province","0") + "^" \
                           + i.get("city","0") + "^" + i.get("area","0") + "^" + str(spider_utils.get_lng(i.get("location", "0"))) + "^" + str(spider_utils.get_lat(i.get("location", "0"))) + "^" \
                           + "null^" + "null^" + "null"

                    # print(str1)

                    str2 = str2 + str1 + "\n"
            except Exception as e:
                # print("报错了", e)
                file_logger.error("报错了", e)


    # print(str2)
    with open("/Users/caosai/Desktop/lbs_test1.txt", "a+") as f:
        f.write(str2)

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



def baidu_data(keywords, region, page_size=20, page_num=0):
    """
    百度地图接口
    :param keywords:
    :param region:
    :param page_size:
    :param page_num:
    :return:
    """
    # ak = "HSpG2oGjxfDeFyLamp89ENfQ3gXckMzG" # self
    ak = "dASz7ubuSpHidP1oQWKuAK3q" # 链家ak
    url = "http://api.map.baidu.com/place/v2/search?" \
          "query=%s&" \
          "region=%s&" \
          "output=json&" \
          "scope=2&&ak=%s&" \
          "page_size=%d&" \
          "page_num=%d&" \
          "city_limit=true" \
          %(keywords, region, ak, page_size, page_num)

    res = None
    try:
        # 返回结果
        res = requests.get(url)
        # print(res.text)
    except Exception as e:
        file_logger.error("解析出错::: ", e)

    if res is not None:
        # 转成json
        json_res = json.loads(res.text)

        # 总页数
        total_results = json_res.get("total", 0)
        # print("总页数", total_results)
        file_logger.info("当前解析%s:%s, 共%d页"%(region, keywords, total_results))

        # 先查询出总页数, 然后分页查询
        page_num = total_results / page_size


        # 按页查询
        str2 = ""
        res_list = list()
        for i in range(int(page_num)):
            page_num = i
            # print("第一页, ", page_num)
            file_logger.info("爬取第%s页"%(page_num+1))

            url = "http://api.map.baidu.com/place/v2/search?" \
                  "query=%s&region=%s&output=json&scope=2&ak=%s&page_size=%d&page_num=%d&city_limit=true" \
                  %(keywords, region, ak, page_size, page_num)

            res = spider_utils.requests_utils(url)

            if res is not None:
                json_res = json.loads(res.text)
                print(json_res)
                try:
                    for i in json_res["results"]:
                        print(i)
                        str1 = i.get("name","0") + "^" + "null^" + i.get("telephone","0") + "^" + i.get("address","0") + "^" + i.get("province","0") + "^" \
                               + i.get("city","0") + "^" + i.get("area","0") + "^" + str(spider_utils.get_lng(i.get("location", "0"))) + "^" + str(spider_utils.get_lat(i.get("location", "0"))) + "^" \
                               + "null^" + "null^" + "null"
                        # 省市区、详细地址、

                        # str11 = i.get("name","0") + "^" + i.get("telephone","0") + "^" + i.get("address","0") + "^" \
                        #         + i.get("province","0") + "^" + i.get("city","0") + "^" + i.get("area","0") + "^"

                        str2 = str2 + str1 + "\n"

                except Exception as e:
                    file_logger.error("报错了", e)
            print(str2)
        # 将结果保存到文件
        # with open("/Users/caosai/Desktop/lbs_all_data.txt", "a+") as f:
        #     f.write(str2)

if __name__ == '__main__':
    # keywords = ["门诊","急诊","诊所","医院","医疗","口腔","眼病","眼科","皮肤","骨科",
    #             "中医","手足健康","康复","祛痘","皮肤管理","脱毛","水光","抗衰","埋线",
    #             "瘦身","整容","整形","医美","美胸","美体","美白","美颜","美肤","医学美容"]
    #
    # region_all = [
    #               '海口市秀英区','海口市龙华区','海口市琼山区','海口市美兰区',
    #               '扬州市广陵区','扬州市邗江区','扬州市江都区']
    #
    # for region in region_all:
    #     for keyword in keywords:
    #         print(region,keyword)
    #         file_logger.info("begin: 爬取城市%s关键字%s"%(region, keyword))
    #         # print(keyword)
    #         get_all_content_from_baidu(keyword, region)


    # for region in hangzhou:
    #     for keyword in keywords_test:
    #         file_logger.info("begin: 爬取城市%s关键字%s"%(region, keyword))
    #         # print(keyword)
    #         geo_list = spider_utils.sub_rect_baidu()
    #
    #         for bounds in geo_list:
    #             get_data_by_bounds(keyword, bounds)

    print()
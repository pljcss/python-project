# -*- coding:utf-8 -*-
import requests
import json
import time
from bs4 import BeautifulSoup
import random
from spider import spider_utils
import logging
import logging.config


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
        file_logger.info("当前解析%s:%s, 共%d页"%(region, keyword, total_results))


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
        file_logger.info("当前解析%s:%s, 共%d页"%(region, keyword, total_results))

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
                json_res = json.loads(res.text)
                print(json_res)
                try:
                    for i in json_res["results"]:
                        str2 = str2 + str(i) + "\n"
                except Exception as e:
                    file_logger.error("报错了", e)

        # 将结果保存到文件
        with open("/Users/caosai/Desktop/lbs_all_杭州.txt", "a+") as f:
            f.write(str2)




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

def get_dazhong_url():
    """
    获取大众点评数据 url
    :return:
    """
    url = "http://www.dianping.com/search/keyword/1/0_美容医院"

    response = spider_utils.requests_utils(url)
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
    keywords = ["医美医疗","医美","整容","整形","美体美肤"]

    # 北京、上海、广州、深圳、杭州、宁波
    regions = ['北京市东城区', '北京市西城区', '北京市朝阳区', '北京市崇文区', '北京市海淀区', '北京市宣武区',
               '北京市石景山区', '北京市门头沟区', '北京市丰台区', '北京市房山区',
               '北京市大兴区', '北京市通州区', '北京市顺义区', '北京市平谷区',
               '北京市昌平区', '北京市怀柔区和延庆县', '北京市密云县',
               '上海市松江区', '上海市青浦区', '上海市奉贤区', '上海市黄浦区',
               '上海市徐汇区', '上海市长宁区',
               '上海市静安区', '上海市普陀区', '上海市虹口区', '上海市杨浦区', '上海市闵行区', '上海市宝山区',
               '上海市嘉定区', '上海市浦东新区', '上海市金山区', '广州市荔湾区', '广州市越秀区', '广州市海珠区',
               '广州市天河区', '广州市白云区', '广州市黄埔区', '广州市番禺区', '广州市花都区', '广州市南沙区',
               '广州市从化区', '广州市增城区', '深圳市罗湖区', '深圳市福田区', '深圳市南山区', '深圳市宝安区',
               '深圳市龙岗区', '深圳市盐田区', '杭州市临安区', '杭州市上城区', '杭州市下城区', '杭州市江干区',
               '杭州市拱墅区', '杭州市西湖区', '杭州市滨江区', '杭州市萧山区', '杭州市余杭区', '杭州市富阳区',
               '宁波市海曙区', '宁波市江东区', '宁波市江北区', '宁波市北仑区', '宁波市镇海区', '宁波市鄞州区']

    # 杭州、广州、厦门、深圳
    hgxs_regions = ['广州市荔湾区', '广州市越秀区', '广州市海珠区',
                   '广州市天河区', '广州市白云区', '广州市黄埔区', '广州市番禺区', '广州市花都区', '广州市南沙区',
                   '广州市从化区', '广州市增城区', '深圳市罗湖区', '深圳市福田区', '深圳市南山区', '深圳市宝安区',
                   '深圳市龙岗区', '深圳市盐田区', '杭州市临安区', '杭州市上城区', '杭州市下城区', '杭州市江干区',
                   '杭州市拱墅区', '杭州市西湖区', '杭州市滨江区', '杭州市萧山区', '杭州市余杭区', '杭州市富阳区',
                   '厦门市思明区','厦门市海沧区','厦门市湖里区','厦门市集美区','厦门市同安区','厦门市翔安区']

    hangzhou = ['杭州市西湖区']
    keywords_test = ['美容']

    # for region in hangzhou:
    #     for keyword in keywords_test:
    #         file_logger.info("begin: 爬取城市%s关键字%s"%(region, keyword))
    #         # print(keyword)
    #         get_all_content_from_baidu(keyword, region)



    for region in hangzhou:
        for keyword in keywords_test:
            file_logger.info("begin: 爬取城市%s关键字%s"%(region, keyword))
            # print(keyword)
            geo_list = spider_utils.sub_rect_baidu()

            for bounds in geo_list:
                get_data_by_bounds(keyword, bounds)
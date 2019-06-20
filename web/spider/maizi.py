# -*- coding:utf-8 -*-
import requests
import json
import time
from bs4 import BeautifulSoup
import random
from spider import spiderUtils
import logging
import logging.config
logging.config.fileConfig('log.ini')
file_logger = logging.getLogger(name="fileLogger")


def get_content_from_baidu(keywords, region, page_size=20, page_num=0):
    """
    百度地图接口
    :param page_size:
    :param page_num:
    :return:
    """

    # ak = "HSpG2oGjxfDeFyLamp89ENfQ3gXckMzG"
    ak = "dASz7ubuSpHidP1oQWKuAK3q"
    url = "http://api.map.baidu.com/place/v2/search?query=%s&region=%s&output=json&ak=%s&page_size=%d&page_num=%d" %(keywords, region, ak, page_size, page_num)

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
        # print("第一页, ", page_num)
        file_logger.info("爬取第%s页"%(page_num+1))

        url = "http://api.map.baidu.com/place/v2/search?query=%s&region=%s&output=json&ak=%s&page_size=%d&page_num=%d" %(keywords, region, ak, page_size, page_num)

        # print(url)
        # time.sleep(5)
        res = spiderUtils.requests_utils(url)
        # res = requests.get(url)
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

                str1 = i.get("name","0") + "," + "null," + i.get("telephone","0") + "," + i.get("address","0") + "," + i.get("province","0") + "," \
                       + i.get("city","0") + "," + i.get("area","0") + "," + str(spiderUtils.get_lng(i.get("location","0"))) + "," + str(spiderUtils.get_lat(i.get("location","0"))) + "," \
                       + "null," + "null," + "null"

                # print(str1)

                str2 = str2 + str1 + "\n"
        except Exception as e:
            # print("报错了", e)
            file_logger.error("报错了", e)


    # print(str2)
    with open("/Users/caosai/Desktop/lbs.txt", "a+") as f:
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
    keywords = ["门诊","急诊","诊所","医院","医疗","口腔","眼病","眼科","皮肤","骨科",
               "中医","手足健康","康复","祛痘","皮肤管理","脱毛","水光","抗衰","埋线",
               "瘦身","整容","整形","医美","美胸","美体","美白","美颜","美肤"]

    regions = ["平度市","黄岛区","市北区","即墨区","李沧区","莱西市","胶州市","嘉定区","静安区",
              "普陀区","松江区","金山区","奉贤区","浦东新区","宝山区","长宁区","杨浦区","黄浦区",
              "徐汇区","闵行区","虹口区","青浦区","海珠区","从化区","增城区","南沙区","番禺区",
              "荔湾区","黄埔区","天河区","越秀区","花都区","白云区","东莞市","南山区","龙华区",
              "宝安区","福田区","罗湖区","龙岗区","碑林区","莲湖区","新城区","未央区","雁塔区",
              "灞桥区","禄劝彝族苗族自治县","东川区","寻甸回族彝族自治县","盘龙区","嵩明县","安宁市",
              "晋宁区","石林彝族自治县","宜良县","西山区","官渡区","五华区","呈贡区","富民县","中原区",
              "金水区","上街区","管城回族区","二七区","惠济区","坪山区","宁乡市","浏阳市","芙蓉区","长沙县",
              "雨花区","市南区","天心区","康平县","城阳区","开福区","昆山市","北仑区","望城区","宁海县",
              "象山县","奉化区","海曙区","江北区","余姚市","慈溪市","富阳区","江干区","余杭区","上城区",
              "下城区","淳安县","滨江区","鄞州区","镇海区","临安区","建德市","桐庐县","江宁区","鼓楼区",
              "建邺区","六合区","浦口区","高淳区","溧水区","栖霞区","玄武区","秦淮区","雨花台区","常熟市",
              "太仓市","吴中区","苏州工业园区","吴江区","虎丘区","姑苏区","相城区","张家港市","拱墅区",
              "西湖区","萧山区","荥阳市","光明区","中牟县","崂山区","巩义市","新密市","新郑市","登封市",
              "和平区","于洪区","皇姑区","浑南区","沈北新区","沈河区","铁西区","新民市","大东区","法库县",
              "辽中区","苏家屯区","都江堰市","崇州市","大邑县","蒲江县","新都区","岳麓区","高陵区","鄠邑区",
              "蓝田县","临潼区","阎良区","长安区","周至县","蔡甸区","东西湖区","汉南区","汉阳区","洪山区",
              "黄陂区","江岸区","江汉区","江夏区","硚口区","青山区","武昌区","新洲区","武侯区","崇明区",
              "盐田区","简阳市","双流区","成华区","青白江区","金堂县","新津县","彭州市","锦江区","金牛区",
              "郫都区","青羊区","邛崃市","温江区","奉贤区","浦东新区","金山区","宝山区","崇明区","龙泉驿区"]

    for region in regions:
        for keyword in keywords:
            get_content_from_baidu(keyword, region)

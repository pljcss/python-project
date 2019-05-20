# -*- coding:utf-8 -*-
import requests
import json
import time
def get_content(page_size=20, page_num=0):
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
        time.sleep(5)
        res = requests.get(url)
        json_res = json.loads(res.text)

        # print(i)
        # print(url)
        try:
            for i in json_res["results"]:
                # print(type(i))
                print(i["name"])
        except Exception as e:
            print(e)


if __name__ == '__main__':
    get_content()
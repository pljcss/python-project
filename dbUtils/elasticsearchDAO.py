# -*- coding: utf-8 -*
from elasticsearch import Elasticsearch
from elasticsearch import helpers
import json

def search_es(es_con:Elasticsearch):
    """
    search 方法
    :param es_con:
    :return:
    """

    body = {
        "query":{
            "match_all":{}
        },
        "sort":{
            "id":{                 # 根据id字段升序排序
                "order":"desc"       # asc升序，desc降序
            }
        }
    }

    search_result = es_con.search(index="shop_face", doc_type="info", body=body)

    return search_result["hits"]["hits"]





def get_es(es_con:Elasticsearch, index_id):
    res = es_con.get(index="shop_face", doc_type="info", id=index_id)

    return res


def delete_es(es_con):
    """

    :param es_con:
    :return:
    """
    pass

def insert_es(es_con:Elasticsearch, index_id, body):
    """
    insert 数据
    :param es_con:
    :param index_id:
    :param body:
    :return:
    """
    # res = es.index(index="shop_face", doc_type="info", id=12345, body={"id":12345, "name":"测试数据1"})

    res = es_con.index(index="shop_face", doc_type="info", id=index_id, body=body)
    return res

def bulk_load():
    pass


def get_lng(dd):
    if dd == "0" or dd == 0:
        return dd
    else:
        return dd.get("lon","0")


def get_lat(dd):
    if dd == "0" or dd == 0:
        return dd
    else:
        return dd.get("lat","0")

if __name__ == '__main__':
    # 建立连接 es version: 5.5.1
    host = [{"host": "172.16.2.159", "port": 9200}] # 需要使用列表的形式
    es = Elasticsearch(hosts=host)
    # print(es.info()) # 需要加括号,否则不输出

    new_id = 1

    element_list = []
    location_distinct_list = []
    with open('/Users/caosai/Desktop/lbs_all_distinct.txt') as f:
        files = f.readlines()
        i = 0

        for file in files:
            # file_json = json.loads(file.replace("'", '"').strip()) # 出错
            file_dict = eval(file)
            body = dict()

            id_es = new_id + i

            name = str(file_dict.get("name", "无"))

            if "理发" not in name and "美发" not in name and "汽修" not in name and "汽车" not in name:
                location = file_dict.get("location", "0") # 经纬度
                address = file_dict.get("address", "无")
                province = file_dict.get("province", "无")
                city = file_dict.get("city", "无")
                region = file_dict.get("area", "无")
                telephone = file_dict.get("telephone", "无")



                if location not in location_distinct_list:
                    location_distinct_list.append(location)

                    ######
                    body["id"] = id_es
                    body["name"] = name
                    body["status"] = 0
                    body["tel"] = telephone
                    body["address"] = address
                    body["shop_latitude"] = str(get_lat(location))
                    body["shop_longitude"] = str(get_lng(location))
                    body["province"] = province
                    body["city"] = city
                    body["region"] = region
                    body["disabled"] = 0



                    # print(telephone)
                    # 如果是字典类型,则插入数据
                    if isinstance(location, dict):
                        location["lat"] = str(location.get("lat", "0"))
                        location["lon"] = str(location.get("lon", "0"))

                        body["location"] = location


                    element = {
                        "_index": "shop_face",
                        "_type": "info",
                        "_id": id_es,
                        "_source": body
                    }


                    # print(element)
                    # print(element)
                    element_list.append(element)

                    i = i + 1

        helpers.bulk(es, element_list)
        # print(element_list)

            ######## 单条插入 ########
            # insert_es(es_con=es, index_id=new_id, body=body)
            # print("插入第 %d 条"%i)

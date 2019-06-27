# -*- coding: utf-8 -*
from elasticsearch import Elasticsearch

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

if __name__ == '__main__':
    # 建立连接 es version: 5.5.1
    host = [{"host": "172.16.2.159", "port": 9200}] # 需要使用列表的形式
    es = Elasticsearch(hosts=host)
    # print(es.info()) # 需要加括号,否则不输出

    """
          "id" : 1625,
          "name" : "崔召镇医院凤凰山卫生所",
          "status" : 0,
          "tel" : "0",
          "address" : "凤凰山村附近",
          "shop_latitude" : "36.801368",
          "shop_longitude" : "120.050985",
          "province" : "山东省",
          "city" : "青岛市",
          "region" : "平度市",
          "disabled" : 0,
          "location" : {
            "lon" : "120.050985",
            "lat" : "36.801368"
          }
    """
    new_id = 504488

    body = dict
    body["id"] = new_id
    body["name"] = "test name"

    print(body)

    # insert_es(es, index_id=new_id, body={"id":new_id, "name":"测试数据2","ddddddd":"没有这个"})
    #
    # result = get_es(es, index_id=new_id)
    # print(result)
    # print(result["_source"])

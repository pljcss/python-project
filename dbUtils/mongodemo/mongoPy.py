import pymongo

def mongo_demo():
    # 连接mongo
    client = pymongo.MongoClient(host="localhost", port=27017)

    # 指定数据库
    db = client["test_mongo"]

    # 指定集合(类似关系型数据库中的表)
    collection = db["test_mongo"]

    # 插入数据
    student = {
        'id': '20190303',
        'name': 'Leo',
        'age': 26,
        'gender': 'female'
    }

    # result= collection.insert_one(student)
    #
    # print(result)


    # 查询数据
    search_result = collection.find_one({"name":"Bob"})
    # print(type(search_result))
    # print(search_result)
    #
    # print(search_result['age'])
    # print(search_result['_id'])

    # 查询多条数据
    search_result_multi = collection.find({"age":26}) # 年龄用字符串则搜不出来结果
    # print(type(search_result_multi))
    # print(search_result_multi)
    print(search_result_multi)
    for result in search_result_multi:
        print(result)


    # 查询年龄大于20岁的人
    search_result_gt20 = collection.find({"age":{"$gt":20}}).count()
    print(search_result_gt20)

    # for result in search_result_gt20:
    #     print(result)


if __name__ == '__main__':
    mongo_demo()



if __name__ == '__main__':

    list_1 = []
    for i in range(100):
        dict_1 = dict() # 此种方式定义dict, 需要带括号
        dict_1["name"] = "Bob"+ str(i)
        dict_1["score"] = i

        list_1.append(dict_1)

    print(list_1)
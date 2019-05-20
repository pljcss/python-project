# -*- coding:utf-8 -*-
import pandas as pd
import json
def json_deal():
    # res = pd.read_json("/Users/saicao/Desktop/j1.json")
    # print(res)


    with open("/Users/saicao/Desktop/j1.json") as f:
        line = f.readlines()
        for i in line:
            ll = json.loads(i)
            print(ll)

            # print(ll.get("phone"))

            for key, value in ll.items():
                print(key, value)

    # json.loads()

    return None

if __name__ == '__main__':
    json_deal()
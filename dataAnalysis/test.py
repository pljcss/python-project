# -*- coding:utf-8 -*-
import pandas as pd

def deal_data():
    with open("/Users/saicao/Desktop/副本.csv") as f:
        str = ""
        index = 0
        for line in f.readlines():
            index += 1
            ll = line.split(",")

            res = ll[1][ll[1].index("(")+3:ll[1].index(")")-2].strip() + "," + ll[2][1:-2].strip()

            if res in str:
                pass
            else:
                str = str + res + "\n"

            print(index)

        with open("/Users/saicao/Desktop/写副本.csv", "w") as f1:
            f1.write(str)

    return None


def search_data():

    activity = pd.read_csv("/Users/saicao/Desktop/activity.csv")
    activity_name = pd.read_csv("/Users/saicao/Desktop/activity_name.csv")
    customer_info = pd.read_csv("/Users/saicao/Desktop/customer_info.csv")

    _res = pd.merge(activity, activity_name, on="activityId", how="left")

    res = pd.merge(_res, customer_info, on="userId", how="left")


    # print(res.head(5))
    # print(res.info())
    # res.to_csv("/Users/saicao/Desktop/ddd.csv")


    print(activity_name)


    return None

if __name__ == '__main__':
    search_data()
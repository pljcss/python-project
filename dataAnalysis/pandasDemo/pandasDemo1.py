# -*- coding:utf-8 -*-
import pandas as pd

def main():
    # pandas读取csv中的文件
    df = pd.read_csv("/Users/saicao/Desktop/dogNames2.csv")
    # print(df.describe())
    #
    # # DataFrame中排序的方法
    # df = df.sort_values(by="Count_AnimalName", ascending=False)
    # # 取前5行
    # print(df.head(5))
    #
    # # pandas取行或者列的注意事项
    # '''
    # 1、方括号内写数值, 表示取行
    # 2、方括号内写字符串, 表示取列
    # '''
    # print(df[:20])
    # print(df["Count_AnimalName"])

    # DataFrame 布尔索引
    print(df[df["Count_AnimalName"]>1000]) # 单条件
    print(df[(df["Count_AnimalName"]>800) & (df["Count_AnimalName"]<1000)]) # 多条件写法

if __name__ == '__main__':
    main()
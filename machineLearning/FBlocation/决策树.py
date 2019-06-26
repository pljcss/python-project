# -*- coding:utf-8 -*-
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_graphviz # 决策树
import pandas as pd

def decision():
    """
    决策树对泰坦尼克号生死预测
    :return:
    """
    # 获取数据
    # titanic = pd.read_csv("http://biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/titanic.txt") # 可以直接读取网络数据
    titanic = pd.read_csv("/Users/saicao/Desktop/stu_data/data/titanic.txt")

    # 处理数据, 找出特征值和目标值
    x = titanic[['pclass', 'age', 'sex']]
    y = titanic['survived']

    # print(x)
    # print(y)

    # 缺失值处理
    x['age'].fillna(x['age'].mean(), inplace=True ) # inplace为True代表替换

    # 分割数据, 训练集、测试集
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

    # 进行处理 (特征工程) 特征如果是类别 -> one_hot编码
    dict = DictVectorizer(sparse=False)
    x_train = dict.fit_transform(x_train.to_dict(orient="records")) # orient="records"代表转换为行

    print(dict.get_feature_names())
    x_test = dict.transform(x_test.to_dict(orient="records"))

    print(x_train)

    # 用决策树进行预测
    dec =  DecisionTreeClassifier(max_depth=5)
    dec.fit(x_train, y_train)

    # 预测准确率
    print("预测的准确率: ", dec.score(x_test, y_test))

    # 导出决策树的结构
    export_graphviz(dec, out_file='/Users/saicao/Desktop/tree.dot', feature_names=['age', 'pclass=1st', 'pclass=2nd', 'pclass=3rd', 'sex=female', 'sex=male'])

    return None

if __name__ == '__main__':
    decision()
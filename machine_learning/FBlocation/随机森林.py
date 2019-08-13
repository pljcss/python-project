# -*- coding:utf-8 -*-
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeClassifier, export_graphviz # 决策树
from sklearn.ensemble import RandomForestClassifier
import pandas as pd


def decision():
    """
    随机森林对泰坦尼克号生死预测
    使用网格搜索
    :return:
    """
    # 获取数据
    # titanic = pd.read_csv("http://biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/titanic.txt") # 可以直接读取网络数据
    titanic = pd.read_csv("/Users/saicao/Desktop/data/titanic.txt")

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

    x_test = dict.transform(x_test.to_dict(orient="records"))

    # 随机森林进行预测(超参数调优)
    rf = RandomForestClassifier()

    #
    param = {"n_estimators": [120,200,300,500,800,1200], "max_depth": [5,8,15,25,30]}

    # 网格搜索与交叉验证
    gc = GridSearchCV(rf, param_grid=param, cv=2)

    gc.fit(x_train, y_train)

    print("准确率: ", gc.score(x_test, y_test))
    print("查看选择参数模型: ", gc.best_params_)



    return None

if __name__ == '__main__':
    decision()
# -*- coding:utf-8 -*-
from sklearn.datasets import load_iris, fetch_20newsgroups, load_boston
from sklearn.model_selection import train_test_split


def main():

    li = load_iris() # 加载数据集
    # print(li.data) # 获取特征值
    # print(li.target) # 获取目标值
    # print(li.DESCR) # 获取描述信息

    """
    注意返回值: 训练集 train + 测试集 test
    训练集train中又分为特征值和目标值, x_train和y_train;
    测试集test分为 特征值和目标, x_test和 y_test;
    """
    x_train, x_test, y_train, y_test = train_test_split(li.data, li.target, test_size=0.25)

    # print(x_train, y_train)
    # print(x_test, y_test)

    new = fetch_20newsgroups(subset='all')
    # print(new.data)
    # print(new.target)


    lb = load_boston()
    print(lb.data)
    print(lb.target)
    print(lb.DESCR)


    return None

if __name__ == '__main__':
    main()

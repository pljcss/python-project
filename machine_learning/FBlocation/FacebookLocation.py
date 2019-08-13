# -*- coding:utf-8 -*-
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
import pandas as pd


def knncls():
    """
    K-近邻预测用户签到位置
    :return:
    """
    # 读取数据
    data = pd.read_csv("/Users/saicao/Desktop/data/facebook_location/train.csv")

    # print(data.head(10))

    # 处理数据
    # 1、缩小数据, 筛选数据
    data = data.query(" x > 1.0 & x < 1.25 & y > 2.5 & y < 2.75")

    # 2、转换时间戳
    time_value = pd.to_datetime(data['time'], unit='s')

    # 把日期格式转换成字典格式
    time_value = pd.DatetimeIndex(time_value)

    # 构造一些特征
    data['day'] = time_value.day
    data['hour'] = time_value.hour
    data['weekday'] = time_value.weekday

    # 删除原先的时间戳
    data = data.drop(['time'], axis=1)
    print(data)

    # 3、将签到位置小于n个用户的数据删除
    place_count = data.groupby('place_id').count()
    tf = place_count[place_count.row_id > 3].reset_index()
    data = data[data['place_id'].isin(tf.place_id)]

    # 取出数据中的特征值和目标值
    y = data['place_id']
    x = data.drop(['place_id'], axis=1)

    # 将数据分割为训练集和测试集
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

    # print(time_value)

    # 特征工程 (标准化)
    # 1、先不做标准化测试准确率

    # 2、对测试集和训练集的特征值进行标准化
    std = StandardScaler()
    x_train = std.fit_transform(x_train)
    x_test = std.transform(x_test)

    # 进行算法流程
    knn = KNeighborsClassifier(n_neighbors=5)

    # fit、predict、score
    knn.fit(x_train, y_train)

    # 得出预测结果
    y_predict = knn.predict(x_test)

    print("预测的目标签到位置为: ", y_predict)

    # 得出准确率
    print("预测的准确率: ", knn.score(x_test, y_test))



    return None

if __name__ == '__main__':
    knncls()

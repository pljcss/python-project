# -*- coding:utf-8 -*-
import random
from matplotlib import pyplot as plt
from matplotlib import font_manager


def movie_time_distribute():
    """
    使用直方图
    统计电影时长分布
    :return:
    """
    # 生成模拟数据: 电影时长
    a = [random.randint(120,150) for i in range(120)]
    print(a)

    # 计算组数
    d = 5
    num_bins = (max(a) - min(a))//d

    # 设置图形大小
    plt.figure(figsize=(20,8), dpi=80)

    # 传入数据和分成的组数
    plt.hist(a, num_bins)

    # 设置x轴刻度
    plt.xticks(range(min(a), max(a)+d, d))

    # 设置网格
    plt.grid(alpha=0.3)

    plt.show()

def deal_data():
    """
    处理原始数据
    :return:
    """
    ss = []
    with open("/Users/saicao/Desktop/zy.txt") as f:
        file = f.readlines()

        for i in file:
            i2 = i.strip()
            ss.append(int(i2))

    return ss

def zhiye_visit_time():
    """
    置业绿城预约用户访问时间分布图
    :return:
    """
    # 生成模拟数据: 电影时长
    a = deal_data()
    print(a)

    # 计算组数
    d = 20
    num_bins = (max(a) - min(a))//d

    print(num_bins)

    # 设置图形大小
    plt.figure(figsize=(20,8), dpi=80)

    # 传入数据和分成的组数
    plt.hist(a, num_bins)

    # 设置x轴刻度
    plt.xticks(range(min(a), max(a)+d, d))
    # plt.xticks(range(min(a), (max(a)+d)/2, d))

    # 设置网格
    plt.grid(alpha=0.3)

    plt.show()


    return None

if __name__ == '__main__':
    zhiye_visit_time()
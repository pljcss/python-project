# -*- coding:utf-8 -*-
import random
from matplotlib import pyplot as plt
from matplotlib import font_manager

'''
使用直方图
统计电影时长分布
'''
def main():

    # 生成模拟数据: 电影时长
    a = [random.randint(120,150) for i in range(120)]
    print(a)

    # 计算组数
    d = 5
    num_bins = (max(a) - min(a))//d

    # 设置图形大小
    plt.figure(figsize=(20,8), dpi=80)

    # 传入数据和分成的组数
    plt.hist(a, 20)

    # 设置x轴刻度
    plt.xticks(range(min(a), max(a)+d, d))

    # 设置网格
    plt.grid(alpha=0.3)

    plt.show()


if __name__ == '__main__':
    main()
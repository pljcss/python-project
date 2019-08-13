# -*- coding:utf-8 -*-
import numpy as np


def main():

    # 加载数据
    gb = np.loadtxt("/Users/saicao/Desktop/gb.csv", delimiter=",", dtype="int", skiprows=1)
    us = np.loadtxt("/Users/saicao/Desktop/us.csv", delimiter=",", dtype="int", skiprows=1)

    # 添加国家信息
    zero_data = np.zeros((gb.shape[0], 1)).astype(int) # 构造全为0的数据
    one_data = np.ones((us.shape[0], 1)).astype(int) # 构造全为1的数据

    # 分别添加一列全为0、1的数组
    gb_data = np.hstack((gb, zero_data))
    us_data = np.hstack((us, one_data))

    # 拼接两组数据
    final_data = np.vstack((gb_data, us_data))
    
    print(final_data)


if __name__ == '__main__':
    main()
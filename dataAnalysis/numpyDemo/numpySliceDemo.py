# -*- coding:utf-8 -*-
import numpy as np

'''
numpy切片
'''
def main():
    gb = np.loadtxt("/Users/saicao/Desktop/gb.csv", delimiter=",", dtype="int", skiprows=1)
    us = np.loadtxt("/Users/saicao/Desktop/us.csv", delimiter=",", dtype="int", skiprows=1)
    # print(gb)
    print(us)

    # 1、取行操作
    print(us[2]) # 取第三行数据
    print(us[2:]) # 取第三行之后的所有数据
    print(us[[2, 4, 5]]) # 取第三行、第五行、第六行数据

    # 2、通用操作,可取行列(逗号前表示行,逗号后表示列,逗号后的冒号表示所有列都取)
    print(us[2,:]) # 取指定行
    print(us[2:,:]) # 取连续多行
    print(us[[2,4,6],:]) # 取非连续多行

    # 3、取列操作
    print(us[:,0]) # 取指定列
    print(us[:,2:]) # 取连续多列
    print(us[:,[0,2]]) # 取非连续多列

    # 4、取指定行列
    print(us[2,3]) # 取第三行,第四列的数

    # 5、取多行多列
    print(us[0:3,0:2]) # 取第一行到第三行,第一列到第二列数据

    # 6、取多个不相邻的点
    print(us[[0,1],[0,2]]) # 两个列表按顺序匹配取点

if __name__ == '__main__':
    main()
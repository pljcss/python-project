# -*- coding:utf-8 -*-
from matplotlib import pyplot as plt

def main():
    # 数据在x轴的位置,是一个可迭代对象
    x = range(2, 26, 2)

    # 数据在y轴的位置,是一个可迭代对象
    y = [12, 22, 23.5, 16, 26, 28, 18, 10, 23, 22, 23, 12]

    # x和y轴一起组成了要绘制的图标,分别是(2,12),(4,22)...
    # 传入x和y,通过plot绘制出折线图
    plt.plot(x, y)
    # 在执行程序的时候展示图形
    plt.show()

    print x

if __name__ == '__main__':
    main()
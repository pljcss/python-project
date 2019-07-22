# -*- coding:utf-8 -*-
from matplotlib import pyplot as plt

'''展示一天中24小时的气温'''
def main():
    # 数据在x轴的位置,是一个可迭代对象
    x = range(2, 26, 2)

    # 数据在y轴的位置,是一个可迭代对象
    y = [12, 22, 23.5, 16, 26, 28, 18, 10, 23, 22, 23, 12]

    # 设置图片大小
    '''figsize设置图像大小, dpi设置图像清晰度'''
    fig = plt.figure(figsize=(20, 8), dpi=80)

    # x和y轴一起组成了要绘制的图标,分别是(2,12),(4,22)...
    # 传入x和y,通过plot绘制出折线图
    plt.plot(x, y)

    # 设置自定义的x,y轴刻度
    # plt.xticks(x)
    # plt.xticks(range(2, 25)) # 将x轴变的密集
    # 将x轴的步长设置为0.5
    _xtick_labels = [i/2.0 for i in range(4, 49)]
    plt.xticks(_xtick_labels[::3]) # 每隔3取一个
    plt.yticks(range(min(y), max(y) + 1))

    # 保存图片
    '''
    可以保存为svg这种矢量图格式, 放大不会有锯齿
    '''
    # plt.savefig('/Users/saicao/Desktop/t1.png')

    # 在执行程序的时候展示图形
    plt.show()

    print(x)

if __name__ == '__main__':
    main()
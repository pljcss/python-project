# -*- coding:utf-8 -*-
from matplotlib import pyplot as plt
import random
from matplotlib import font_manager

# 解决python2 matplotlib中文显示报错问题
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

'''
设置中文显示
添加描述信息
格式化输出坐标轴的信息,如果 1-> 10点1分
'''
def main():
    # 设置中文字体
    my_font = font_manager.FontProperties(fname='/System/Library/Fonts/PingFang.ttc')

    # 准备x, y轴数据
    y_temperature = [random.randint(20, 35) for i in range(0, 120)]
    x_time = range(0, 120)

    # 设置图片大小
    fig = plt.figure(figsize=(20, 8), dpi=80)

    # 设置x,y轴
    plt.plot(x_time, y_temperature)

    # 设置 x 轴刻度
    _x = list(x_time) # 取步长10
    _xtick_labels = ['10:{}'.format(i) for i in range(60)]
    _xtick_labels += ['11:{}'.format(i) for i in range(60)]

    # 将刻度数字与字符串一一对应
    # rotation表示将x轴刻度旋转的度数,fontproperties设置显示中文
    plt.xticks(_x[::10], _xtick_labels[::10], rotation=60, fontproperties=my_font)

    # 设置描述信息
    plt.xlabel('时间', fontproperties=my_font)
    plt.ylabel('温度 单位(摄氏度)', fontproperties=my_font)
    plt.title('10点到12点每分钟的气温变化情况', fontproperties=my_font)
    # 如果不显示需要在方法中也传入font参数
    # plt.title('10点到12点每分钟的气温变化情况', fontproperties=my_font)

    # 展示图标
    plt.show()

if __name__ == '__main__':
    main()
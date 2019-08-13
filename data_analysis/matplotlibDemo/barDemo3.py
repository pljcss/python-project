# -*- coding:utf-8 -*-
from matplotlib import pyplot as plt
from matplotlib import font_manager
import sys

# 解决python2 matplotlib中文显示报错问题
# reload(sys)
# sys.setdefaultencoding('utf-8')

'''
绘制条形图
横着的
'''
def main():
    # 设置中文字体
    my_font = font_manager.FontProperties(fname='/System/Library/Fonts/PingFang.ttc')

    # 如果名字太长,可以使用\n进行换行
    a = ['猩球崛起', '敦刻尔克', '蜘蛛侠', '战狼2']
    b_14 = [2358, 399, 2212, 262]
    b_15 = [12357, 156, 2045, 168]
    b_16 = [15746, 312, 4497, 319]

    bar_width = 0.2
    x_14 = list(range(len(b_14)))
    x_15 = [i+bar_width for i in x_14]
    x_16 = [i+bar_width*2 for i in x_14]

    # 设置图形大小
    plt.figure(figsize=(20,8), dpi=80)

    plt.bar(range(len(a)), b_14, width=bar_width, label='9月14日')
    plt.bar(x_15, b_15, width=bar_width, label='9月15日')
    plt.bar(x_16, b_16, width=bar_width, label='9月16日')

    # 设置x轴刻度
    plt.xticks(x_15, a, fontproperties=my_font)

    # 设置图例
    plt.legend(prop=my_font)

    # 设置网格
    plt.grid(alpha=0.3)

    plt.show()

if __name__ == '__main__':
    main()
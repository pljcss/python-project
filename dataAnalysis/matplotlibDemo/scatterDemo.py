# -*- coding:utf-8 -*-
from matplotlib import pyplot as plt
from matplotlib import font_manager
import sys

# 解决python2 matplotlib中文显示报错问题
# reload(sys)
# sys.setdefaultencoding('utf-8')

'''
绘制散点图
'''
def main():
    # 设置中文字体
    my_font = font_manager.FontProperties(fname='/System/Library/Fonts/PingFang.ttc')

    # 3月份与10月份气温
    y_3 = [13,16,18,12,22,24,19,20,21,14,13,16,18,20,18,19,23,24,25,20,22,21,19,22,23,26,28,24,26,25,26]
    y_10 = [22,24,23,28,29,31,19,18,17,15,12,18,19,22,24,26,19,20,22,16,15,19,20,22,19,20,22,18,16,15,14]

    # 月份
    x_3 = range(1, 32)
    x_10 = range(51, 82)

    # 设置图形大小
    plt.figure(figsize=(20,8), dpi=80)

    '''
    使用scatter方法绘制散点图
    '''
    plt.scatter(x_3, y_3, label='3月份')
    plt.scatter(x_10, y_10, label='10月份')

    # 调整x轴刻度
    _x = list(x_3) + list(x_10)
    _xtick_labels = ["3月{}日".format(i) for i in x_3]
    _xtick_labels += ["10月{}日".format(i-50) for i in x_10]
    plt.xticks(_x[::3], _xtick_labels[::3], fontproperties=my_font, rotation=60)

    # 添加图例
    plt.legend(prop=my_font, loc=0)

    # 添加描述信息
    plt.xlabel('时间', fontproperties=my_font)
    plt.ylabel('温度', fontproperties=my_font)
    plt.title('标题', fontproperties=my_font)

    # 展示
    plt.show()

if __name__ == '__main__':
    main()
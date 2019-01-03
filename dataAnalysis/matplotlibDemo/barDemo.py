# -*- coding:utf-8 -*-
import random
from matplotlib import pyplot as plt
from matplotlib import font_manager
import sys

# 解决python2 matplotlib中文显示报错问题
# reload(sys)
# sys.setdefaultencoding('utf-8')

'''
绘制条形图
竖着的
'''
def main():
    # 设置中文字体
    my_font = font_manager.FontProperties(fname='/System/Library/Fonts/PingFang.ttc')

    # 如果名字太长,可以使用\n进行换行
    x = ['海王','中国合伙人2','印度合伙人','网络谜踪','无名之辈','狗十三','绿毛怪格林奇','毒液','午夜整容室','照相师','淡蓝琥珀']
    y = [1075.18,94.74,138.38,65.89,53.71,47.45,26.54,15.79,3.01,9.93,2.16]

    # 设置图形大小
    plt.figure(figsize=(20,8), dpi=80)

    # plt.bar(range(len(x)), y, width=0.3, color='yellow')
    plt.bar(range(len(x)), y, width=0.3)
    plt.xticks(range(len(x)), x, fontproperties=my_font, rotation=90)
    plt.show()


if __name__ == '__main__':
    main()
# -*- coding:utf-8 -*-
import random
from matplotlib import pyplot as plt
from matplotlib import font_manager
import sys

# 解决python2 matplotlib中文显示报错问题
# reload(sys)
# sys.setdefaultencoding('utf-8')

'''
添加多个曲线图
添加不同曲线的描述信息
绘制网格
'''
def main():

    # 设置中文字体
    my_font = font_manager.FontProperties(fname='/System/Library/Fonts/PingFang.ttc')

    # 年龄
    x = range(11, 31)

    # 数量
    y_leo = [random.randint(0, 5) + 1 for i in x]
    y_tom = [random.randint(0, 5) + 1 for i in x]

    # 设置图片大小
    fig = plt.figure(figsize=(20, 8), dpi=80)

    plt.plot(x, y_leo, label='Leo', color='orange', linestyle=':')
    plt.plot(x, y_tom, label='Tom', color='cyan', linestyle='--')

    x_str = ["{}岁".format(i) for i in x]
    plt.xticks(x, x_str)
    plt.yticks(range(min(min(y_leo)-1, min(y_tom)-1), max(max(y_leo), max(y_tom))+5))

    # 设置描述信息
    plt.xlabel('年龄')
    plt.ylabel('数量/个')
    plt.title('Tom和Leo在11岁～30岁所交女朋友的数量变化图')

    # 绘制网格,alpha设置透明度
    plt.grid(alpha=0.4, linestyle='--')

    # 添加图例
    '''
    两步,1:在plot中设置label; 2:调用plt.legend()
    注意,此处设置显示中文需要使用prop参数,而其他地方设置中文都是 fontproperties 参数
    loc参数可以设置图例的位置
    '''
    # plt.legend()
    plt.legend(prop=my_font, loc=0)

    plt.show()

if __name__ == '__main__':
    main()
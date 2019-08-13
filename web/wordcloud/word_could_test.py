# -*- coding:utf-8 -*-
import jieba
import os
from os import path
#导入wordcloud模块和matplotlib模块
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from scipy.misc import imread


# 读取一个txt文件
comment_text = open('/Users/saicao/Desktop/file1.txt','r').read()
comment_text=unicode(comment_text,'utf-8')

# 结巴分词, 生成字符串, 如果不通过分词无法直接生成正确的中文词云
cut_text = " ".join(jieba.cut(comment_text))

# 当前文件文件夹所在目录
d = path.dirname(__file__)

# 读取背景图片
color_mask = imread("/Users/saicao/Desktop/1.png")

cloud = WordCloud(
    #设置字体,不指定就会出现乱码,注意mac下的字体路径
    font_path="/Library/Fonts/Songti.ttc",
    #font_path=path.join(d,'simsun.ttc'),
    #设置背景色
    background_color='white',
    #词云形状
    mask=color_mask,
    #允许最大词汇
    max_words=2000,
    #最大号字体
    max_font_size=40
)

# 产生词云
word_cloud = cloud.generate(cut_text)
# 保存图片
word_cloud.to_file("/Users/saicao/Desktop/2.jpg")

# 显示词云图片
plt.imshow(word_cloud)
plt.axis('off')
plt.show()
# -*- coding:utf-8 -*-
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer # 文本
from sklearn.feature_extraction import DictVectorizer # 字典
from sklearn.preprocessing import MinMaxScaler, StandardScaler, Imputer # 归一化, 标准化, 缺失值处理
import jieba
import numpy as np

def textVector():
    """
    对文本数据进行特征抽取
    :return:
    """
    # 实例化 CountVectorizer
    cv = CountVectorizer()

    # 调用fit_transform输入并转换数据; 列表中的数据分别代表第一篇文章和第二篇文章
    data = cv.fit_transform(["life is is short, i like python", "life is too long, i dislike python"])

    # 如果使用空格切割,则会有不同的分词方式;对于中文,应该先分词
    data_cn = cv.fit_transform(["人生苦短,我用python", "人生 漫长,我用java"])

    # 打印结果
    print(cv.get_feature_names())
    print(data.toarray()) # 将sparse矩阵 转换为数组形式
    print(data) # sparse矩阵


def cutWord():
    """
    分词
    :return:
    """
    con1 = jieba.cut("今天很残酷，明天更残酷，后天很美好，但绝大部分是死在明天晚上，所以每个人不要放弃今天。")
    con2 = jieba.cut("我们看到的从很遥远的星系来的光是几百万年前发出的，这样当我们看到宇宙时，我们是看到它的过去。")
    con3 = jieba.cut("如果只有一种方式了解某样事物，你就不会真正了解它。了解事物真正含义的秘密取决于如何将其与我们所了解的事物相联系。")

    # 转换成列表
    content1 = list(con1)
    content2 = list(con2)
    content3 = list(con3)

    # 把列表转换成字符串
    c1 = ' '.join(content1)
    c2 = ' '.join(content2)
    c3 = ' '.join(content3)

    return c1, c2, c3


def cnTextVector():
    """
    方式一：CountVectorizer
    中文特征值化
    :return:
    """

    c1, c2, c3 = cutWord()

    cv = CountVectorizer()
    data = cv.fit_transform([c1, c2, c3])

    print(cv.get_feature_names())
    print(data.toarray())

    return None

def tfIdfVec():
    """
    方式二：TfidfVectorizer
    中文特征值化
    :return:
    """

    c1, c2, c3 = cutWord()

    cv = TfidfVectorizer()
    data = cv.fit_transform([c1, c2, c3])

    print(cv.get_feature_names())
    print(data.toarray())
    return None

def dictVector():
    """
    对字典数据进行特征抽取
    :return:
    """
    # 实例化
    # 默认为True,返回sparse矩阵; 设为False,则返回数组
    dict = DictVectorizer(sparse=False)

    list_dict = [{'city':'上海','temperature':22}, {'city':'北京','temperature':18}, {'city':'南京','temperature':30}]

    data = dict.fit_transform(list_dict)

    print(dict.get_feature_names())
    print(data)

    return None

def mm():
    """
    归一化处理
    :return:
    """
    mm = MinMaxScaler(feature_range=(0,1))
    data = mm.fit_transform([[90,2,10,40], [60,4,15,45], [75,3,13,46]])

    print(data)

    return None

def stand():
    """
    标准化缩放
    :return:
    """
    std = StandardScaler()
    data = std.fit_transform([[1., -1., 3.], [2., 4., 2.], [4., 6., -1.]])

    print(data)

    return None


def im():
    """
    缺失值处理
    :return:
    """
    # nan, NaN
    im = Imputer(missing_values='NaN', strategy='mean', axis=0)

    data = im.fit_transform([[1, 2], [np.nan, 3], [7, 6]])

    print(data)

    return None

if __name__ == '__main__':
    im()
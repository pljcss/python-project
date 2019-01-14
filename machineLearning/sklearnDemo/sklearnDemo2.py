# -*- coding:utf-8 -*-
from sklearn.feature_selection import VarianceThreshold
from sklearn.decomposition import PCA


def var():
    """
    特征选择 - 删除低方差的特征
    :return:
    """
    # 默认是0, 把所有值相同的特征删除掉
    var = VarianceThreshold(threshold=0.0)
    data = var.fit_transform([[0, 2, 0, 3], [0, 1, 4, 3], [0, 1, 1, 3]])

    print(data)

    return None

def pca():
    """
    主成分分析进行特征降维
    :return:
    """
    pca = PCA(n_components=0.9)
    data = pca.fit_transform([[2, 8, 4, 5], [6, 3, 0, 8], [5, 4, 9, 1]])

    print(data)

    return None

if __name__ == '__main__':
    var()
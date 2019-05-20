import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

def logistic():
    """
    逻辑回归做二分类进行癌症预测 (根据细胞的属性特征)
    :return:
    """
    # 构造列标签名字
    column = ['Sample code number','Clump Thickness','Uniformity of Cell Size','Uniformity of Cell Shape',
              'Marginal Adhesion','Single Epithelial Cell Size','Bare Nuclei',
              'Bland Chromatin','Normal Nucleoli','Mitoses','Class']

    # 1、读取数据
    data = pd.read_csv("/Users/saicao/Desktop/data/breast-cancer-wisconsin.data", names=column)

    print(data)

    # 2、缺失值处理
    data = data.replace("?", value=np.nan)
    data = data.dropna() # 删除缺失值数据

    # 3、进行数据分割
    x_train, x_test, y_train, y_test = train_test_split(data[column[1:10]], data[column[10]], test_size=0.25)

    # 4、进行标准化处理
    std = StandardScaler()
    x_train = std.fit_transform(x_train)
    x_test = std.fit_transform(x_test)

    # 5、逻辑回归预测
    lg = LogisticRegression(C=1.0)

    lg.fit(x_train, y_train)

    print(lg.coef_)

    y_predict = lg.predict(x_test)

    print("准确率: ", lg.score(x_test, y_test))

    print("召回率: ", classification_report(y_test, y_predict, labels=[2, 4], target_names=["良性", "恶性"]))

    return None

if __name__ == '__main__':
    logistic()
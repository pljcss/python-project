# -*- coding:utf-8 -*-
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression, SGDRegressor, Ridge
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error # 回归性能评估

def linear():
    """
    线性回归直接预测房屋价格
    正规方程
    :return:
    """
    # 获取数据
    lb = load_boston()

    # 分割数据集到训练集和测试集
    x_train, x_test, y_train, y_test = train_test_split(lb.data, lb.target, test_size=0.25)

    print(y_train, y_test)


    # 进行标准化处理, 特征值和目标值都需要进行标准化处理
    # 实例化两个标准化API
    std_x = StandardScaler()

    x_train = std_x.fit_transform(x_train)
    x_test = std_x.transform(x_test)

    # 目标值
    std_y = StandardScaler()
    y_train = std_y.fit_transform(y_train.reshape(-1, 1)) # 0.19版本的要求转换器,estimator必须是二维的, 需要转换成二维的
    y_test = std_y.transform(y_test.reshape(-1, 1))

    # estimator预测
    # 正规方程求解方式预测结果
    lr = LinearRegression()
    lr.fit(x_train, y_train)

    # 权重参数, 集回归系数
    print(lr.coef_)

    # 预测测试集的房价
    # y_predict = lr.predict(x_test)
    y_lr_predict = std_y.inverse_transform(lr.predict(x_test)) # 转换为标准化之前的数据
    print("正规方程测试集里面每个样本的房价: ", y_lr_predict)

    print("正规方程的均方误差: ", mean_squared_error(std_y.inverse_transform(y_test), y_lr_predict))

    return None

def linear2():
    """
    线性回归直接预测房屋价格
    梯度下降
    :return:
    """
    # 获取数据
    lb = load_boston()

    # 分割数据集到训练集和测试集
    x_train, x_test, y_train, y_test = train_test_split(lb.data, lb.target, test_size=0.25)

    print(y_train, y_test)


    # 进行标准化处理, 特征值和目标值都需要进行标准化处理
    # 实例化两个标准化API
    std_x = StandardScaler()

    x_train = std_x.fit_transform(x_train)
    x_test = std_x.transform(x_test)

    # 目标值
    std_y = StandardScaler()
    y_train = std_y.fit_transform(y_train.reshape(-1, 1)) # 0.19版本的要求转换器,estimator必须是二维的, 需要转换成二维的
    y_test = std_y.transform(y_test.reshape(-1, 1))

    # estimator预测
    # 梯度下降去预测房价
    sgd = SGDRegressor()

    sgd.fit(x_train, y_train)

    print(sgd.coef_)

    # 预测测试集的房价
    y_sgd_predict = std_y.inverse_transform(sgd.predict(x_test))

    print("梯度下降测试集里每个房子的预测价格", y_sgd_predict)

    print("梯度下降的均方误差: ", mean_squared_error(std_y.inverse_transform(y_test), y_sgd_predict))

    return None

def linear3():
    """
    岭回归直接预测房屋价格
    :return:
    """
    # 获取数据
    lb = load_boston()

    # 分割数据集到训练集和测试集
    x_train, x_test, y_train, y_test = train_test_split(lb.data, lb.target, test_size=0.25) # 分割随机的

    print(y_train, y_test)


    # 进行标准化处理, 特征值和目标值都需要进行标准化处理
    # 实例化两个标准化API
    std_x = StandardScaler()

    x_train = std_x.fit_transform(x_train)
    x_test = std_x.transform(x_test)

    # 目标值
    std_y = StandardScaler()
    y_train = std_y.fit_transform(y_train.reshape(-1, 1)) # 0.19版本的要求转换器,estimator必须是二维的, 需要转换成二维的
    y_test = std_y.transform(y_test.reshape(-1, 1))

    # estimator预测
    # 岭回归去预测房价
    # 可以利用网格搜索去找到合适的参数
    rd = Ridge(alpha=1.0)

    rd.fit(x_train, y_train)

    print(rd.coef_)

    # 预测测试集的房价
    y_rd_predict = std_y.inverse_transform(rd.predict(x_test))

    print("梯度下降测试集里每个房子的预测价格", y_rd_predict)

    print("梯度下降的均方误差: ", mean_squared_error(std_y.inverse_transform(y_test), y_rd_predict))

    return None


if __name__ == '__main__':
    # linear()
    # linear2()

    # 每次预测的结果是不一样的, 如果真正想拿这些数据去预测东西的时候, 其实应该把训练集固定
    linear3()
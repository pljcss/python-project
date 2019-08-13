# -*- coding:utf-8 -*-
import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2' # 去除警告

def myregression():
    """
    使用tensorflow实现一个线性回归预测

    1、作用域 scope

    2、添加权重参数, 损失值等, 在tensorboard中的观察情况
        · 收集变量
        · 合并变量写入事件文件

    3、模型保存与加载
    :return:
    """

    # 将数据放在一个作用域
    with tf.variable_scope("data"):
        # 1、准备特征数据 x特征值[100,1] y目标值[100]
        x = tf.random_normal([100, 1], mean=1.75, stddev=0.5, name="x_data")

        # 2、准备目标值(人为设定关系测试), 矩阵相乘必须是二维的
        y_true = tf.matmul(x, [[0.7]]) + 0.8

    # 建立模型
    with tf.variable_scope("model"):
        # 3、建立线性回归模型, 只有一个特征, 所以只有1个权重; 偏置只有1个 (y = xw + b)
        # 随机给一个权重和偏置的值, 让它从这个点开始去求损失, 然后再当前状态下优化
        # 模型的参数需要用变量去定义, 因为这个权重会不断变化的(weight用变量定义才能优化)
        # trainable参数: 指定这个变量能跟着梯度下降一起优化(默认是True)
        weight = tf.Variable(tf.random_normal([1, 1], mean=0.0, stddev=1.0), name="w", trainable=True) # 权重
        bias = tf.Variable(0.0, name="b") # 偏置

        y_predict = tf.matmul(x, weight) + bias

    # 损失函数
    with tf.variable_scope("loss"):
        # 3、建立损失函数 (均方误差和)
        loss = tf.reduce_mean(tf.square(y_true - y_predict))

    # 优化
    with tf.variable_scope("optimizer"):
        # 4、梯度下降优化损失
        # learn_rate取值,一般去0～1, 也可以是一些大点的个位数值
        # minimize代表最小化损失
        train_op = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

    # 3、收集tensor
    tf.summary.scalar("losses", loss)
    tf.summary.histogram("weights", weight)

    # 定义合并tensor的op
    merged = tf.summary.merge_all()

    # 定一个初始化变量op
    init_op = tf.global_variables_initializer()

    # 定义一个保存模型的实例(只要是op都可以定义在会话前面)
    saver = tf.train.Saver()

    # 5、通过会话运行程序
    with tf.Session() as sess:
        # 初始化变量
        sess.run(init_op)
        # 打印最先随机初始化的权重和偏置
        print("随机初始化的参数权重为: %f, 偏置为: %f" % (weight.eval(), bias.eval()))

        # 建立事件文件
        filterWriter = tf.summary.FileWriter("/Users/saicao/Desktop/tensor_summary/", graph=sess.graph)

        # 运行优化op
        # sess.run(train_op)
        # print("优化后的参数权重为: %f, 偏置为: %f" % (weight.eval(), bias.eval()))

        # 加载模型, 覆盖模型中随机定义的参数, 从上次训练的参数结果开始
        if os.path.exists("/Users/saicao/Desktop/tensor_ckpt/model/checkpoint"):
            saver.restore("/Users/saicao/Desktop/tensor_ckpt/model")

        # 循环训练 运行优化op
        for i in range(200):
            sess.run(train_op)

            # 运行合并的tensor
            summary = sess.run(merged) # 每次运行都要合并
            filterWriter.add_summary(summary, i)

            print("第%d次优化后的参数权重为: %f, 偏置为: %f" % (i, weight.eval(), bias.eval()))

        # 保存模型
        # 也可以放在for循环里面, 比如每隔100步保存一个文件
        saver.save(sess, "/Users/saicao/Desktop/tensor_ckpt/model")

    return None

if __name__ == '__main__':
    myregression()
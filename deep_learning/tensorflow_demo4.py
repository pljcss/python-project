# -*- coding:utf-8 -*-
import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2' # 去除警告

"""
可视化 Tensorboard
"""

# 常量
a = tf.constant(5.0, name="a")
b = tf.constant(6.0, name="b")
sum1 = tf.add(a, b, name="add")


# 变量op
var = tf.Variable(tf.random_normal([2, 3], mean=0.0, stddev=1.0), name="variable")

print(a, var)
init_op = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init_op)

    # 把程序的图文件写入事件文件
    # 第一个参数是写入的路径, 第二个参数是指定的图
    filterWriter = tf.summary.FileWriter("/Users/saicao/Desktop/tensor_summary/", graph=sess.graph)

    print(sess.run([sum1, var]))
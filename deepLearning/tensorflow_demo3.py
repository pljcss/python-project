# -*- coding:utf-8 -*-
import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2' # 去除警告


'''
变量
'''
# 变量op (里面的值仍然是张量类型)
a = tf.constant([1, 2, 3, 4, 5]) # 普通张量

# 创建的随机值张量被变量op包裹
var = tf.Variable(tf.random_normal([2, 3], mean=0.0, stddev=1.0))

print(a, var)

# 1、必须做一个显示的初始化
init_op = tf.global_variables_initializer()

with tf.Session() as sess:
    # 2、必须运行初始化op
    sess.run(init_op)

    print(sess.run([a, var]))
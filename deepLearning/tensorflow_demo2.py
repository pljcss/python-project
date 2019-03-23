# -*- coding:utf-8 -*-
import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2' # 去除警告

a = tf.constant(5.0)
b = tf.constant(6.0)
sum1 = tf.add(a, b)

# print(a)
# print(sum1)

# 定义一个形状不固定的tensor
plt = tf.placeholder(tf.float32, [None, 2])
print(plt)

# 使用静态去固定形状
plt.set_shape([3, 2, 4])
print(plt)

# 对于静态形状来说, 一旦张量形状固定了, 不能再次设置静态形状
# plt.set_shape([4, 2]) # 不能再次修改

# 动态形状可以去创建一个新的张量
plt_reshape = tf.reshape(plt, [3, 2])
print(plt_reshape)



with tf.Session() as sess:
    pass
    # print(sess.run(plt, feed_dict={plt:[[1,2,3],[2,3,4],[5,6,7]]}))

    # 打印tensor的属性 ####
    # print(a.graph)
    # print(a.shape)
    # print(plt.shape)
    # print(a.name)
    # print(a.op)
    #####################
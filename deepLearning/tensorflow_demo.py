# -*- coding:utf-8 -*-
import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2' # 去除警告

# 创建一张图(包含了一组op和tensor), 上下文环境
g = tf.Graph()
print(g) # 打印图
with g.as_default():
    c = tf.constant(11.0)
    print(c.graph) # 打印图


# 实现加法
a = tf.constant(5.0)
b = tf.constant(6.0)
sum1 = tf.add(a, b)


# 默认的这种图, 相当于是给程序分配一段内存
# graph = tf.get_default_graph()
# print(graph) # 打印图

# 训练模型
# 实时的提供数据去训练
# placeholder是一个占位符(此时没有数据, 先占个位置, 在运行的时候在提供数据给你)
# plt也是一个op, 里面装的就是tensor, 但是tensor里面没有具体的数值
# 如果训练样本不固定, 可以用 None 表示
plt = tf.placeholder(tf.float32, [None, 3]) # 第一个参数是数据类型, 第二个参数是形状(两行三列), 第三个参数暂时用不到
print(plt)
# 只能运行一个图, config参数可以
# 只要有上下文环境, 就可以使用方便的eval了
with tf.Session(config=tf.ConfigProto()) as sess:
    # 运行的时候给plt提供数值, feed_dict是一个字典, 值就是填充的数据
    # 定义的是2行3列, 填进去的也必须是2行3列
    # 这就相当于运行的时候, 实时的给你提供数据去运算
    print(sess.run(plt, feed_dict={plt : [[1,2,3], [4,5,6]]}))

    # print(sum1.eval())
    print(a.graph)
    print(sum1.graph)
    print(sess.graph)








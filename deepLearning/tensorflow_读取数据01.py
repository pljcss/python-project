import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2' # 去除警告

"""
模型同步处理数据的过程. 先处理数据, 然后才能取数据训练
"""

# 1、首先定义队列
Q = tf.FIFOQueue(3, tf.float32)

# 放入一些数据
enq_many = Q.enqueue_many([[1, 2, 3], ]) # enqueue_many可以放入一个列表

# 2、定义处理数据的逻辑、取数据的过程(取数据+1, 再入队列)
out_q = Q.dequeue() # tensor

data = out_q + 1

en_q = Q.enqueue(data)

with tf.Session() as sess:
    # 初始化队列
    sess.run(enq_many) # 不初始化定义的列表不会赋给enq_many

    # 处理数据
    for i in range(6):
        sess.run(en_q)

    # 训练数据
    for i in range(Q.size().eval()):
        print(sess.run(Q.dequeue()))
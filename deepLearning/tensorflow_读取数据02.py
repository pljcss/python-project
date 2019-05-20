import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2' # 去除警告

"""
模拟异步 子线程存入样本, 主线程读取样本
"""

# 1、定义一个1000容量的队列
Q = tf.FIFOQueue(1000, tf.float32)

# 2、定义要做的事情, 循环+1, 放入队列中
var = tf.Variable(0.0)

# 实现一个自增 tf.assign_add, 不能使用var = var + 1, 因为每次运行var都被初始化为0.0
# 使用assign_add可以实现var的累加
data = tf.assign_add(var, tf.constant(1.0))
en_q = Q.enqueue(data)

# 3、定义队列管理器op, 指定多少个子线程, 子线程该干什么事
# 队列管理器是专门管理子线程的事情的
# 第一个参数是 哪个队列, 子线程操作哪个队列
# 第二个参数是 定义这个子线程要做哪些操作, 如果多个, [en_1, op1, op2]*3,线程一旦启动就不受控制,cpu去控制
qr = tf.train.QueueRunner(Q, enqueue_ops=[en_q]*2)

# 初始化变量的op
init_op = tf.global_variables_initializer()

# 开启会话
with tf.Session() as sess:
    # 初始化变量
    sess.run(init_op)

    # 开启线程管理器 (主线程开启)
    coord = tf.train.Coordinator()

    # 真正开启子线程
    threads = qr.create_threads(sess, coord=coord, start=True) # coord指定线程协调器

    # 主线程, 不断读取数据训练
    for i in range(300):
        print(sess.run(Q.dequeue()))

    # 回收线性
    coord.request_stop()
    coord.join(threads)

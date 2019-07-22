import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2' # 去除警告

FLAGS = tf.app.flags.FLAGS
tf.app.flags.DEFINE_integer("is_train", 1, "指定模型是训练还是预测")

def full_connected():
    # 获取真实数据
    mnist = input_data.read_data_sets("/Users/saicao/Desktop/stu_data/minist/input_data", one_hot=True)

    # print(mnist.train.labels[0])
    # print(mnist.train.images[0])

    # 1、建立数据的占位置(在实时运行的时候,提供数据)
    # x [None, 784], y_true [None, 10]
    with tf.variable_scope("data"): # 作用域
        x = tf.placeholder(tf.float32, [None, 784])
        y_true = tf.placeholder(tf.int32, [None, 10])

    # 2、建立一个全连层的神经网络, w [784, 10], b [10]
    with tf.variable_scope("fc_model"):
        # 随机初始化权重和偏置
        weight  = tf.Variable(tf.random_normal([784, 10], mean=0.0, stddev=1.0), name="w") # 二维
        bias = tf.Variable(tf.constant(0.0, shape=[10])) # 一维

        # 预测None个样本的输出结果
        # matrix [None, 784] * [784, 10] + [10] = [None, 10]
        y_predict = tf.matmul(x, weight) + bias

    # 3、求出所有样本的损失, 然后求平均值
    with tf.variable_scope("soft_cross"):
        # 求平均交叉熵损失
        # reduce_mean 就是对一个列表的所有数相加, 然后取平均值
        loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y_true, logits=y_predict))

    # 4、梯度下降优化损失
    with tf.variable_scope("optimizer"):
        train_op = tf.train.GradientDescentOptimizer(0.1).minimize(loss) # 学习率

    # 5、计算准确率
    with tf.variable_scope("acc"):
        equal_list = tf.equal(tf.arg_max(y_true, 1), tf.arg_max(y_predict, 1))

        # equal_list None个样本, [1,0,1,1,0,0......]
        accuracy = tf.reduce_mean(tf.cast(equal_list, tf.float32))

    # 收集变量 单个数字值收集
    tf.summary.scalar("losses", loss)
    tf.summary.scalar("acc", accuracy)

    # 高维度变量收集
    tf.summary.histogram("weightes", weight)
    tf.summary.histogram("biases", bias)

    # 定义一个初始化变量的op, 只要是定义op, 都把它拿到会话外面做
    init_op = tf.global_variables_initializer()

    # 定义一个合并变量的op, op需要运行
    merged_op = tf.summary.merge_all()

    # 创建一个saver
    saver = tf.train.Saver()

    # 开启会话去训练
    with tf.Session() as sess:
        # 初始化变量
        sess.run(init_op)

        # 建立events文件, 然后写入
        filewriter = tf.summary.FileWriter("/Users/saicao/Desktop/stu_data/tensor_summary/", graph=sess.graph)

        if FLAGS.is_train == 1:
            # 迭代步数去训练, 更新参数预测
            for i in range(2000):
                # 取出真实存在的特征值和目标值
                mnist_x, mnist_y = mnist.train.next_batch(50)

                # 运行train_op训练
                sess.run(train_op, feed_dict={x: mnist_x, y_true: mnist_y})

                # 写入每步训练的值
                summary = sess.run(merged_op, feed_dict={x: mnist_x, y_true: mnist_y})
                filewriter.add_summary(summary, i)

                print("训练第%d步,准确率为:%f" % (i, sess.run(accuracy, feed_dict={x: mnist_x, y_true: mnist_y})))

            # 保存模型
            saver.save(sess, "/Users/saicao/Desktop/stu_data/tensor_ckpt/fc_model")
        else:
            # 加载模型
            saver.restore(sess, "/Users/saicao/Desktop/stu_data/tensor_ckpt/fc_model")

            # 如果是0, 做出预测
            for i in range(100):
                # 每次测试一张图片 [0,1,0,0,....]
                x_test, y_test = mnist.test.next_batch(1)

                print("第%d张图片, 手写数字是:%d, 预测结果是:%d" % (
                    i,
                    tf.arg_max(y_test, 1).eval(),
                    tf.arg_max(sess.run(y_predict, feed_dict={x: x_test, y_true: y_test}),1).eval()
                ))

    return None

if __name__ == '__main__':
    full_connected()
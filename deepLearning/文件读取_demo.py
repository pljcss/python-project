import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2' # 去除警告

def csvread(filelist):
    """
    读取CSV文件
    :param filelist: 文件路径 + 名字的列表
    :return: 读取的内容
    """

    # 1、构造文件的队列
    file_queue = tf.train.string_input_producer(filelist)

    # 2、构造csv阅读器, 读取队列数据(按一行)
    reader = tf.TextLineReader()
    key, value = reader.read(file_queue)
    # print(value)

    # 3、对每行内容解码
    # record_defaults 指定每一个样本的每一列的类型,还可以指定默认值
    # record_defaults必须是二维的, 装进去的每一列的默认值和类型, 如果填1就代表, 是用int去读取的,空缺位置默认值是1;
    # 如果填2就代表, 是用int去读取的,空缺位置默认值是2;想以字符串可以指定字符串
    # [["None"], [4.0]]
    records = [["None"], ["None"]]
    example, label = tf.decode_csv(value, record_defaults=records) # 有几列数据,就用几个值接收

    print(example, label)

    # 4、想要读取多个数据, 就需要批处理
    # 批处理大小, 跟队列的数据的数量没有影响, 只决定这批次取多少数据
    # batch_size决定最终取多少个数据, 如果batch_size=20,capacity=5,那么会分批次取, 凑够20个作为一批次
    example_batch, label_batch = tf.train.batch([example, label], batch_size=9, num_threads=1, capacity=9)

    print(example_batch, label_batch)

    return example_batch, label_batch


if __name__ == '__main__':
    # 1、找到文件放入列表, 路径+名字 -> 列表
    file_name = os.listdir("/Users/saicao/Desktop/demo_tensorflow")

    filelist = [os.path.join("/Users/saicao/Desktop/demo_tensorflow/", file) for file in file_name]

    # print(filelist)

    example_batch, label_batch = csvread(filelist)

    # 开启会话运行结果
    with tf.Session() as sess:
        # 定义一个线程协调器
        coord = tf.train.Coordinator()

        # 开启读文件的线程
        threads = tf.train.start_queue_runners(sess, coord=coord)

        # 打印读取的内容
        print(sess.run([example_batch, label_batch]))

        # 回收子线程
        coord.request_stop()
        coord.join(threads)


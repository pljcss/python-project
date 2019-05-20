import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2' # 去除警告

"""
写入example
"""
# 定义cifar的目录, 命令行方式
FLAGS = tf.app.flags.FLAGS
tf.app.flags.DEFINE_string("cifar_dir", "/Users/saicao/Desktop/stu_data/tf_binary/cifar-10-batches-bin/", "文件目录")
# 指定的是文件
tf.app.flags.DEFINE_string("cifar_tfrecords", "/Users/saicao/Desktop/stu_data/tf_records/cifar.tfrecords", "存入tfrecords的文件目录")

class CifarRead(object):
    """
    读取二进制文件, 写入tfrecords, 读取tfrecords
    """
    def __init__(self, filelist):
        # 文件列表
        self.filelist = filelist

        # 定义读取的图片的一些属性
        self.height = 32
        self.width = 32
        self.channel = 3
        self.label_bytes = 1
        self.image_bytes = self.height * self.width * self.channel
        self.bytes = self.label_bytes + self.image_bytes

    def read_and_decode(self):
        """
        读取二进制文件转换成张量
        :return:
        """
        # 1、构造文件队列
        file_queue = tf.train.string_input_producer(self.filelist)

        # 2、构造二进制文件读取器, 读取内容
        reader = tf.FixedLengthRecordReader(self.bytes) # 参数: 每个样本的字节数

        key, value = reader.read(file_queue)

        # 3、解码内容
        label_image = tf.decode_raw(value, tf.uint8) # 返回值: 标签 + 特征值

        # 4、分割出图片和标签数据, 切除特征值和目标值
        label = tf.cast(tf.slice(label_image, [0], [self.label_bytes]), tf.int32)
        image = tf.slice(label_image, [self.label_bytes], [self.image_bytes])
        print(label, image)

        # 5、可以对图片的特征数据进行形状改变 [3072] -> [32, 32, 3]
        image_reshape = tf.reshape(image, [self.height, self.width, self.channel])

        print(label, image_reshape)

        # 6、批处理数据
        image_batch, label_batch = tf.train.batch([image_reshape, label], batch_size=10, num_threads=1, capacity=10)

        print(image_batch, label_batch)

        return image_batch, label_batch


    def write_to_tfrecords(self, image_batch, label_batch):
        """
        将图片的特征值和目标值存入tfrecords
        :param image_batch: 10张图片的特征值
        :param label_batch: 10张图片的目标值
        :return: None
        """
        # 1、建立TFrecords
        writer = tf.python_io.TFRecordWriter(FLAGS.cifar_tfrecords)

        # 2、循环将所有样本写入文件, 每张图片样本都要构造example协议
        # eval必须在session里面运行
        for i in range(10):
            # 取出第i个图片数据的特征值和目标值
            image = image_batch[i].eval().tostring()
            label = int(label_batch[i].eval()[0])

            # 构造一个样本的example
            example = tf.train.Example(features=tf.train.Features(feature={
                "image": tf.train.Feature(bytes_list=tf.train.BytesList(value=[image])),
                "label": tf.train.Feature(int64_list=tf.train.Int64List(value=[label]))
            }))

            # 写入单独的样本
            writer.write(example.SerializeToString())

        # 关闭资源
        writer.close()
        return None

if __name__ == '__main__':
    # 1、找到文件放入列表, 路径+名字 -> 列表
    file_name = os.listdir(FLAGS.cifar_dir)
    filelist = [os.path.join(FLAGS.cifar_dir, file) for file in file_name if file[-3:] == "bin"]

    cf = CifarRead(filelist)
    image_batch, label_batch = cf.read_and_decode()

    with tf.Session() as sess:

        sess.run(tf.global_variables_initializer())
        sess.run(tf.local_variables_initializer())

        # 定义一个线程协调器 (主线程开启)
        coord = tf.train.Coordinator()
        # 开启读文件的线程, 不开启无法执行上述方法中定义的操作
        threads = tf.train.start_queue_runners(sess, coord=coord)

        # 存入tfrecords文件
        print("开始存储")

        cf.write_to_tfrecords(image_batch, label_batch)  # 里面有eval, 必须在session里面运行

        print("结束存储")

        # 打印读取的内容
        # print(sess.run([image_batch, label_batch]))

        # 回收子线程
        coord.request_stop()
        coord.join(threads)

import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2' # 去除警告

def picread(filelist):
    """
    读取狗图片并转换成张量
    :param filelist: 文件路径+文件名的列表
    :return: 每张图片的张量
    """
    # 1、构造文件队列
    file_queue = tf.train.string_input_producer(filelist)

    # 2、构造阅读器去读取图片 (默认读取一张图片)
    reader = tf.WholeFileReader()

    key, img = reader.read(file_queue)

    print(img)

    # 3、对读取的图片数据进行解码
    image = tf.image.decode_jpeg(img)

    print(image)

    # 4、处理图片的大小 (统一大小)
    image_resize = tf.image.resize_images(image, [200, 200])

    print(image_resize)

    # 注意: 一定要把样本的形状固定[200, 200, 3],在批处理的时候要求所有的形状必须定义(否则会报错)
    image_resize.set_shape([200, 200, 3])
    print(image_resize)

    # 5、进行批处理
    image_batch = tf.train.batch([image_resize], batch_size=3, num_threads=100, capacity=3)
    print(image_batch)

    return image_batch

if __name__ == '__main__':
    # 1、找到文件放入列表, 路径+名字 -> 列表
    file_name = os.listdir("/Users/saicao/Desktop/dog")
    filelist = [os.path.join("/Users/saicao/Desktop/dog/", file) for file in file_name]

    print(filelist)

    image_batch = picread(filelist)

    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        sess.run(tf.local_variables_initializer())
        # 定义一个线程协调器 (主线程开启)
        coord = tf.train.Coordinator()
        # 开启读文件的线程, 不开启无法执行上述方法中定义的操作
        threads = tf.train.start_queue_runners(sess, coord=coord)

        # 打印读取的内容
        print(sess.run([image_batch]))

        # 回收子线程
        coord.request_stop()
        coord.join(threads)


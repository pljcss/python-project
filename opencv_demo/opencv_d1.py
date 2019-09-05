# -*- coding:utf-8 -*-
import cv2 # opencv读取的格式是BGR
import matplotlib.pyplot as plt
import numpy as np


def read_pic():
    """
    数据读取 - 图片
    :return:
    """
    cat_pic = '/Users/saicao/Desktop/stu_data/pictures/cat.jpg'

    # cv2.IMREAD_COLOR # 彩色图像
    # cv2.IMREAD_GRAYSCALE # 灰度图像
    # img = cv2.imread(cat_pic, cv2.IMREAD_GRAYSCALE)
    # 读彩色图片
    img = cv2.imread(cat_pic)
    # print(img)

    # 图像的基本信息
    print(img.shape)
    print(img.size) # 像素点数
    print(type(img))
    print(img.dtype)


    # 截取部分图像数据
    # cat_cut = img[0:50, 0:200]
    # cv_show('image', cat_cut)

    # 颜色通道提取
    b, g, r = cv2.split(img) # 彩色图片才能split三份
    print(b.shape)

    # 合并
    img = cv2.merge((b,g,r))

    # 展示图像
    # cv_show('image', img)

    # 只保留R 通道, 将其他两个通道的值置为0
    cur_img_r = img.copy()
    cur_img_r[:,:,0] = 0
    cur_img_r[:,:,1] = 0
    cv_show('R', cur_img_r)

    # 只保留G 通道
    cur_img_r = img.copy()
    cur_img_r[:,:,0] = 0
    cur_img_r[:,:,2] = 0
    cv_show('G', cur_img_r)

    # 只保留B 通道
    cur_img_r = img.copy()
    cur_img_r[:,:,1] = 0
    cur_img_r[:,:,2] = 0
    cv_show('B', cur_img_r)


    # 保存图像
    # cv2.imwrite('copy.jpg', img)

def bound_fill():
    """
    边界填充
    :return:
    """
    # 上下左右填充大小
    top_size, bottom_size, left_size, right_size = (200,200,200,200)

    cat_pic = '/Users/saicao/Desktop/stu_data/pictures/cat.jpg'
    img = cv2.imread(cat_pic)

    # 不同的填充效果
    replicate = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, borderType=cv2.BORDER_REPLICATE)
    reflect = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, borderType=cv2.BORDER_REFLECT)
    reflect101 = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, borderType=cv2.BORDER_REFLECT_101)
    wrap = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, borderType=cv2.BORDER_WRAP)
    constant = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, borderType=cv2.BORDER_CONSTANT, value=0)

    # 展示图像
    plt.subplot(231), plt.imshow(img, 'gray'), plt.title('ORIGINAL')
    plt.subplot(232), plt.imshow(replicate, 'gray'), plt.title('REPLICATE')
    plt.subplot(233), plt.imshow(reflect, 'gray'), plt.title('REFLECT')
    plt.subplot(234), plt.imshow(reflect101, 'gray'), plt.title('REFLECT_101')
    plt.subplot(235), plt.imshow(wrap, 'gray'), plt.title('WRAP')
    plt.subplot(236), plt.imshow(constant, 'gray'), plt.title('CONSTANT')

    plt.show()

def threshold_op():
    """
    阈值操作
    :return:
    """
    cat_pic = '/Users/saicao/Desktop/stu_data/pictures/cat.jpg'
    img = cv2.imread(cat_pic)
    img_gray = cv2.imread(cat_pic, cv2.IMREAD_GRAYSCALE)

    ret, thresh1 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
    ret, thresh2 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY_INV)
    ret, thresh3 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_TRUNC)
    ret, thresh4 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_TOZERO)
    ret, thresh5 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_TOZERO_INV)

    titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
    images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

    for i in range(6):
        plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])

    plt.show()


    # cv_show('image', img_gray)

def pic_smooth():
    """
    图像平滑
    :return:
    """
    pic_path = '/Users/saicao/Desktop/stu_data/pictures/lenaNoise.png'
    img = cv2.imread(pic_path)

    # 均值滤波
    # 简单的平均卷积操作
    blur = cv2.blur(img, (3, 3))
    # cv_show('box', blur)

    # 方框滤波
    # 基本和均值一样, 可以选择归一化
    box = cv2.boxFilter(img, -1, (3, 3), normalize=True)

    # 方框滤波
    # 基本和均值一样, 可以选择归一化, 容易越界
    box2 = cv2.boxFilter(img, -1, (3, 3), normalize=False)
    # cv_show('box', box2)

    # 高斯滤波
    # 高斯滤波的卷积核里的数值是满足高斯分布的, 相当于更加重视中间的
    aussian = cv2.GaussianBlur(img, (5,5), 1)
    # cv_show('aussian', aussian)

    # 中值滤波, 相当于用中值代替
    median = cv2.medianBlur(img, 5)
    # cv_show('median', median)

    # 展示所有的
    res = np.hstack((blur, aussian, median)) # 水平
    # res = np.vstack((blur, aussian, median)) # 竖直
    print(res)
    cv_show('median vs average', res)

def read_video():
    """
    数据读取 - 视频
    :return:
    """
    test_video = '/Users/saicao/Desktop/stu_data/pictures/test.mp4'
    # cv2.VideoCapture()可以捕捉摄像头, 用数字来控制不同的设备, 例如 0/1
    # 如果是视频文件, 直接指定视频路径即可
    vc = cv2.VideoCapture(test_video)

    # 监测是否打开正确
    if vc.isOpened():
        open_v, frame = vc.read()
    else:
        open_v = False

    # 读取所有帧
    while open_v:
        ret, frame = vc.read()
        if frame is None:
            break

        if ret is True:
            # 转成黑白的
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow('result', gray)

            # waitKey指处理完一帧, 需要等待的时间
            # 27代表的退出键, 按esc即可退出
            if cv2.waitKey(10) & 0xFF == 27:
                break

    vc.release()
    cv2.destroyAllWindows()

def cv_show(name, img):
    """
    显示图像
    :param name: 窗口名字
    :param img: 读取的图像
    :return:
    """
    # 显示图像, 可以创建多个窗口, 创建显示图像的窗口
    # 第一个参数是窗口的名字
    cv2.imshow(name, img)

    # 等待时间,毫秒级, 0表示任意键终止
    cv2.waitKey(0)
    # cv2.waitKey(1000) # 1000代表1s后关闭
    cv2.destroyAllWindows()

if __name__ == '__main__':
    pic_smooth()
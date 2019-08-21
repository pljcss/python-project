import cv2 as cv
import numpy as np

def get_pos(image):
    blurred = cv.GaussianBlur(image, (5, 5), 0)
    canny = cv.Canny(blurred, 200, 400)
    contours, hierarchy = cv.findContours(canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for i, contour in enumerate(contours):
        M = cv.moments(contour)
        if M['m00'] == 0:
            cx = cy = 0
        else:
            cx, cy = M['m10'] / M['m00'], M['m01'] / M['m00']
        if 6000 < cv.contourArea(contour) < 8000 and 370 < cv.arcLength(contour, True) < 390:
            if cx < 400:
                continue
            x, y, w, h = cv.boundingRect(contour)  # 外接矩形
            cv.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv.imshow('image', image)
            return x
    return 0



if __name__ == '__main__':
    # img = np.ones((200, 200, 3), np.uint8) * 255
    # cv.rectangle(img, (50, 50), (150, 150), (0, 0, 255), 2)
    # cv.imshow('test', img)
    # cv.waitKey(0)
    # cv.destroyAllWindows()
    #
    # cv.imread
    # print(cv2.__version__)
    # # cv2.imread('/sdf.jpg'
    # img = cv2.imread('/Users/caosai/Desktop/dog.jpeg')
    # print(img)
    # cv2.imshow('image',img)


    # img = np.ones((200, 200, 3)) * 255
    # cv2.rectangle(img, (50, 50), (150, 150), (0, 0, 255), 2)
    # cv2.imshow('test', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


    # img0 = cv.imread('/Users/caosai/Desktop/dog.jpeg')
    # get_pos(img0)
    # cv.waitKey(0)
    # cv.destroyAllWindows()


    img = cv.imread("/Users/caosai/Desktop/dog.jpeg")
    cv.imshow("1",img)
    cv.waitKey(10000)



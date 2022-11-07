import cv2
"""def to_right_size(x):
    height=x.shape[0]
    width=x.shape[1]
    if (height>100):
        temp=int(height/100)
        b=cv2.resize(x,(100,100))
        print(b.shape)
        return b
a=cv2.imread("./data/cat.294.jpg")
print(a[2])
#cv2.imshow("orgin",a)
b=to_right_size(a)
#cv2.imshow("after",b)
cv2.waitKey(0)
# -*- coding: utf-8 -*-
"""
"""
@File    : 200113_等比例调整图像分辨率大小.py
@Time    : 2020/1/13 13:38
@Author  : Dontla
@Email   : sxana@qq.com
@Software: PyCharm
"""
import cv2


def img_resize(image):
    height, width = image.shape[0], image.shape[1]

    # 设置新的图片分辨率框架
    width_new = 64
    height_new = 64
    # 判断图片的长宽比率
    if width / height >= width_new / height_new:
        a = abs(height_new - int(height * width_new / width))
        img_new = cv2.resize(image, (width_new, int(height * width_new / width)))
        img_new=cv2.copyMakeBorder(img_new, 0, a, 0, 0, cv2.BORDER_CONSTANT, value=[0, 255, 0])
    else:

        a = abs(height_new - int(width * height_new / height))
        img_new = cv2.resize(image, (int(width * height_new / height), height_new))
        img_new = cv2.copyMakeBorder(img_new, 0, 0, 0, a, cv2.BORDER_CONSTANT, value=[0, 255, 0])
    return img_new


img = cv2.imread('./data/cat.294.jpg')
img_new = img_resize(img)
#img_new=
print(img_new.shape)


cv2.imshow('win', img_new)
cv2.imshow('pre',img)
cv2.waitKey(0)


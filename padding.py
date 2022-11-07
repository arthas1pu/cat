#!/usr/bin/python3
# coding:utf-8

import cv2 as cv

# 读取图像
img = cv.imread("./data/cat.294.jpg")
print(img.shape)
# 显示原图
cv.imshow("test_window0", img)

img1 = cv.copyMakeBorder(img, 10, 10, 10, 10, cv.BORDER_CONSTANT, value=[0, 255, 0])
print(img1.shape[0])
"""img2 = cv.copyMakeBorder(img, 100, 100, 100, 100, cv.BORDER_REFLECT)
img3 = cv.copyMakeBorder(img, 100, 100, 100, 100, cv.BORDER_REPLICATE)
img4 = cv.copyMakeBorder(img, 100, 100, 100, 100, cv.BORDER_WRAP)"""
cv.imshow("BORDER_CONSTANT", img1)
"""cv.imshow("BORDER_REFLECT", img2)
cv.imshow("BORDER_REPLICATE", img3)
cv.imshow("BORDER_WRAP", img4)
"""
# 阻塞等待
key = cv.waitKey(0)

# 输入q，退出
if key == ord('q'):
    cv.destroyAllWindows()
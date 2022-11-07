import cv2 as cv

# 读入原图片

img = cv.imread('./data/cat.294.jpg')

# 打印出图片尺寸

print(img.shape)

# 将图片高和宽分别赋值给x，y

x, y = img.shape[0:2]

# 显示原图

cv.imshow('OriginalPicture', img)

# 缩放到原来的二分之一，输出尺寸格式为（宽，高）

img_test1 = cv.resize(img, (398,397 ))

cv.imshow('resize0', img_test1)

cv.waitKey()

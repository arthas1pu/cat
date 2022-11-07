#0是黑色255是白色
###读取图片
import cv2
#a=cv2.imread("./data/cat.294.jpg")
#cv2.imshow("test",a)
#cv2.waitKey(0)
######读取视频
a=cv2.VideoCapture("./data/jay.mp4")
a.set(3,800)#参数3设置长宽
a.set(4,800)#参数4设置长宽
a.set(10,100)#参数10设置亮度QQ
while True:
    succes,img=a.read()
    cv2.imshow("test",img)
    if cv2.waitKey(50)&0xFF==ord("q"):
        break
###改色在opencv中默认图像模式为BGR而非RGB而电脑上的图片是以rgb存储的
"""a=cv2.imread("./data/cat.640.jpg")
b=cv2.cvtColor(a,cv2.COLOR_BGR2RGB)
c=cv2.cvtColor(a,cv2.COLOR_BGR2GRAY)
cv2.imshow("okk",a)
cv2.imshow("NO",b)
cv2.imshow("fuck",c)
print(a.shape)
cv2.waitKey(0)
"""

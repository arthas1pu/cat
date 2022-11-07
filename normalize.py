import numpy as np
#####标准化数据以便更好的下降参考https://blog.csdn.net/hqh131360239/article/details/79061535
#a=np.array([[3,4],[6,8]])
#b=np.linalg.norm(a,axis=1,keepdims=True)
#print(a)
#print(b)
####这里使用的方法是除以2次范数
###竖着的方向axis=0，横着方向干axis=1


#求exp即e的x次方
#a=np.array([[2,4],[9,0]])
#print(a)
#b=np.exp(a)
#print(b)

####矩阵乘法使用np.dot,逐元素的乘法使用np.multiply



####初始化矩阵
a=np.zeros([100,1])
print(a)










#####softmax 二分分类时使用
#a=np.array([[4,6,9],[7,2,7]])
#def softmax(x):
   # x_exp=np.exp(a)
   # x_sum=np.sum(x_exp,axis=1,keepdims=True)
   # s=x_exp/x_sum;
   # return s*/
#print(a)
#b=softmax(a)
#print(b)
###image to vector
t_image = np.array([[[ 0.67826139,  0.29380381],
                     [ 0.90714982,  0.52835647],
                     [ 0.4215251 ,  0.45017551]],

                   [[ 0.92814219,  0.96677647],
                    [ 0.85304703,  0.52351845],
                    [ 0.19981397,  0.27417313]],

                   [[ 0.60659855,  0.00533165],
                    [ 0.10820313,  0.49978937],
                    [ 0.34144279,  0.94630077]]])
print(t_image)
v=t_image.reshape((t_image.shape[0]*t_image.shape[1]*t_image.shape[2]),1)
print(v)



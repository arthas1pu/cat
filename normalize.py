import numpy as np
#####标准化数据以便更好的下降参考https://blog.csdn.net/hqh131360239/article/details/79061535
a=np.array([[3,4],[6,8]])
b=np.linalg.norm(a,axis=1,keepdims=True)
print(a)
print(b)
####这里使用的方法是除以2次范数
###竖着的方向axis=0，横着方向干axis=1
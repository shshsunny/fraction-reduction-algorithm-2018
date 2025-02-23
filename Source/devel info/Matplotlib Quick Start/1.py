import matplotlib.pyplot as plt
import numpy as np

# 从[-1,1]中等距去50个数作为x的取值
x = np.linspace(-1, 1, 50)
y = 2*x + 1
x, y = list(x), list(y)
print(x, y)
# 第一个是横坐标的值，第二个是纵坐标的值
plt.plot(x, y)#描点
# 必要方法，用于将设置好的figure对象显示出来
plt.show()

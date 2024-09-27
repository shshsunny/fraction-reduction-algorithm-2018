import numpy as np
import matplotlib.pyplot as plt

# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D
# setup the figure and axes
fig = plt.figure(figsize=(10, 5))  # 画布宽长比例
ax = fig.add_subplot(121, projection='3d')
ax.set_title('1')
width = depth = 1
for i in range(-10, 10):
    for j in range(-10, 10):
        ax.bar3d(i, j, 0, width, depth, np.sqrt(i ** 2 + j ** 2), color = np.array([0, 1, 1]))
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('time cost')
plt.show()
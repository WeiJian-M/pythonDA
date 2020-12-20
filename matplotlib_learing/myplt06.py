# 多图合一

import matplotlib.pyplot as plt
import numpy as np

plt.figure()
plt.subplot(2,1,1)#表示整个图像分割成2行2列，当前位置为1
plt.plot([0,1],[0,1])#横坐标变化为[0,1] 竖坐标变化为[0,2]

plt.subplot(2,3,4)
plt.plot([0,1],[0,2])

plt.subplot(2,3,5)
plt.plot([0,1],[0,3])

plt.subplot(2,3,6)
plt.plot([0,1],[0,4])
plt.show()
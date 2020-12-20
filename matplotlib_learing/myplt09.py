# 次坐标轴

import numpy as np
import matplotlib.pyplot as plt

x=np.arange(0,10,0.1)
y1=0.5*x**2
y2=-1*y1
fig = plt.figure()

ax1 = plt.subplot(111)
ax2 = ax1.twinx()#镜像显示
ax1.plot(x, y1, 'g-')
ax2.plot(x, y2, 'b-')

ax1.set_xlabel('X data')
ax1.set_ylabel('Y1 data', color='g')#第一个y坐标轴
ax2.set_ylabel('Y2 data', color='b')#第二个y坐标轴
plt.show()

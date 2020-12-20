# 分格显示

import numpy as np
import matplotlib.pyplot as plt

plt.figure()
'''
使用plt.subplot2grid创建第一个小图，(3,3)表示将整个图像分割成3行3列，
(0,0)表示从第0行0列开始作图，colspan=3表示列的跨度为3。colspan和rowspan缺省时默认跨度为1
'''
ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=3)  # stands for axes
ax1.plot([1, 2], [1, 2])
ax1.set_title('ax1_title')#设置图的标题

#将图像分割成3行3列，从第1行0列开始做图，列的跨度为2
ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=2)

#将图像分割成3行3列，从第1行2列开始做图，行的跨度为2
ax3 = plt.subplot2grid((3, 3), (1, 2), rowspan=2)

#将图像分割成3行3列，从第2行0列开始做图，行与列的跨度默认为1
ax4 = plt.subplot2grid((3, 3), (2, 0))
ax4.scatter([1, 2], [2, 2])
ax4.set_xlabel('ax4_x')
ax4.set_ylabel('ax4_y')
ax5 = plt.subplot2grid((3, 3), (2, 1))

plt.show()

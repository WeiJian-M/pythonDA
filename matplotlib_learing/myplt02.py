# 画图中默认配置的具体内容

import matplotlib.pyplot as plt
import numpy as np

# 创建一个8*6的图，分辨率为80
plt.figure(figsize=(8,6), dpi=80)

# 创建一个1*1的子图，并在第一块绘制
plt.subplot(1,1,1)

X = np.linspace(-np.pi, np.pi, 300, endpoint=True)
Y1 = np.sin(X)
Y2 = np.cos(X)

# 绘制正弦曲线，线条的颜色和粗细均可改变，添加图例
plt.plot(X, Y1, color='green', linewidth=1.0, linestyle='-', label="sin")

# 绘制余弦曲线
plt.plot(X, Y2, color='blue', linewidth=1.0, linestyle='-', label='cos')

# 设置横轴的范围
plt.xlim(-4.0, 4.0)

# 设置纵轴范围
plt.ylim(-1.0, 1.0)

# 设置横轴坐标点
'''
我们可以把 3.142 当做是 π，但毕竟不够精确。
当我们设置记号的时候，我们可以同时设置记号的标签。
注意这里使用了 LaTeX。
'''
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi], [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])

# 设置纵轴坐标点
plt.yticks([-1, 0, +1],[r'$-1$', r'$0$', r'$+1$'])

# 设置图片边界
xmin, xmax = np.min(X), np.max(X)
ymin, ymax = np.min(Y1), np.max(Y1)
dx = (xmax - xmin) * 0.2
dy = (ymax - ymin) * 0.2
plt.xlim(xmin - dx, xmax + dx)
plt.ylim(ymin - dy, ymax + dy)

# 移动坐标轴位置
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))

# 添加图例
plt.legend(loc='upper left')

# 给一些特殊点做注释
t = 2*np.pi/3
plt.plot([t,t],[0,np.sin(t)],color='g',linewidth=2.5,linestyle=":")
plt.scatter([t,],[np.sin(t),], 20, color='g')
'''
plt.annotate(s, xy, xytext)  # 添加注释，除s、xy外其余还有若干可选参数。
s：注释文本，
xy：指定要注释的（x，y）坐标点， 
xytext：可选，指定要放置文本的（x，y）坐标点。如果没有，则默认为xy注释点。
arrowprops：可选，字典形式，用于在xy坐标和xytext间绘制一个指定形状的箭头，本例中指定一个'->'类型的箭头，箭头头部宽和高为0.2/0.4
'''
plt.annotate(r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',xy=(t, np.sin(t)), xytext=(+10, +30), textcoords='offset points', fontsize=16,arrowprops=dict(arrowstyle="->"))
# 以分辨率 72 来保存图片
# plt.savefig("mppng.png", dpi = 72)

# 在屏幕上显示
plt.show()






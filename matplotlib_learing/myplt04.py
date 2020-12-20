# 条形图
import numpy as np
import matplotlib.pyplot as plt

X = np.arange(12)
Y1 = np.random.uniform(0.1,1,12)
Y2 = np.random.uniform(0.1,1,12)
plt.bar(X,Y1,facecolor='r')
plt.bar(X,-Y2,facecolor='b')

#标记值
for x,y in zip(X,Y1):#zip表示可以传递两个值
    plt.text(x,y+0.05,'%.2f'%y,ha='center',va='bottom')#ha表示横向对齐 bottom表示向下对齐
for x,y in zip(X,Y2):
    plt.text(x+0.4,-y-0.05,'%.2f'%y,ha='center',va='top')

plt.show()
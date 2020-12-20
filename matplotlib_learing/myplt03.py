# 散点图

import numpy as np
import matplotlib.pyplot as plt

n = 1024
X = np.random.randn(n)
Y = np.random.randn(n)

plt.scatter(X,Y,s=10,c='g',alpha=1)
plt.xlim(-1,1)
plt.ylim(-1,1)
plt.show()

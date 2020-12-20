# 折线图

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,10)
y = np.random.randint(1,100,10)

plt.plot(x,y)
plt.scatter(x,y,s=20)
for a,b in zip(x,y):
    plt.text(a,b,b)
plt.show()


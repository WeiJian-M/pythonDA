import matplotlib.pyplot as plt
import numpy as np

X = np.linspace(-np.pi, np.pi, 256)
Y1 = np.sin(X)
Y2 = np.cos(X)

plt.plot(X, Y1, 'r-', X, Y2, 'g--')
plt.show()
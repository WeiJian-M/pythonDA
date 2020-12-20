## 热力图、灰度图

import numpy as np
import matplotlib.pyplot as plt

a = np.random.rand(4,4)

fig = plt.figure(figsize = (8,4))

sub01 = plt.subplot(121)
plt.imshow(a)
plt.colorbar()
sub02 = plt.subplot(122)
plt.imshow(a, cmap='gray')
plt.colorbar()

plt.show()

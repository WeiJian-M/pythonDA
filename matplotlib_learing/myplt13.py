## 画极坐标图

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_excel('E:\\2020数模培训\\往年赛题及优秀论文\\近十年赛题及优秀论文\\赛题\\T2019\\A-2019中文\\附件1-凸轮边缘曲线.xlsx')
df2 = pd.read_excel('E:\\2020数模培训\\往年赛题及优秀论文\\近十年赛题及优秀论文\\赛题\\T2019\\A-2019中文\\附件3-弹性模量与压力.xlsx')
q = df['极角（rad）']
r = df['极径（mm）']
f = df2['压力(MPa)']
m = df2['弹性模量(MPa)']
fig = plt.figure()
sub01 = plt.subplot(121, projection='polar')
sub01.plot(q, r)
sub02 = plt.subplot(122)
sub02.plot(f, m)
plt.show()


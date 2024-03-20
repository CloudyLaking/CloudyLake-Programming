#画最简单的xy图
import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 6])
y = np.array([0, 100])

plt.plot(x, y)
plt.show()

plt.plot(x,y,"bo")#用圆点绘制


#画函数图
x = np.arange(0,4*np.pi,0.1) # start,stop,step
y = np.sin(x)
z = np.cos(x)
plt.plot(x,y,"bo",x,z,"bo")
plt.show()

#注意散点图x和y数组的大小一定要相等
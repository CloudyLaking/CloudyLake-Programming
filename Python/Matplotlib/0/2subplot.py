#
import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array([0, 6])
y = np.array([0, 100])

plt.subplot(2, 2, 1)#行数，列数，第几个
plt.plot(x,y)
plt.title("plot 1")
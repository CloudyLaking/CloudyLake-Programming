##数值模拟计算pi并获得运行时间
import time
import math
import numpy
pi0=math.pi

#询问分辨率
x=int(input("需要多少分辨率的网格？（输入正整数）"))
t1=time.time()

#搭建网格
grid = numpy.array([[a, b] 
    for a in range(x)
    for b in range(x)
    if (a>(x/2) or b>(x/2))and (a+(50/x))**2+(b+(50/x))**2<(x**2)])

#计算pi
amount=len(grid)+int((x**2)/4)
t2=time.time()
print("在分辨率为%d*%d的情况下"%(x,x))
print("结果为%.10f"%float(amount*4/(x**2)))
print("pi值应为%.10f"%pi0)
print("运行时间为%.6fs"%(t2-t1))

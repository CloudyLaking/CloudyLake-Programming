#cmath是复数下的math

#循环检测随机数生成的概率
import random
sum=0
for i in range(1,10000):
    aa=random.randrange(0,2,1)
    sum=sum+aa
    print("第",i,"轮的平均数是",sum/i)

#python数学函数还包括abs整数绝对值
#sqrt,max,cmp,ceil,floor等等
#divmod(a,b)返回a除以b的商和余数
#pow(a,b,c)表示a**b%c（如有c）
#factorial(x)整数x(>=0)的阶乘
#log(a,b)默认a=e
'''
ceil(x)
大于等于x的最小的整数
floor(x)
小于等于x的最大的整数
trunc(x)
截取为最接近0的整数
'''

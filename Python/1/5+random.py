#cmath是复数下的math
'''
uniform(a,b)
返回在[a,b]区间的随机实数
randint(a,b)
返回在[a,b]区间的随机整数
choice(seq)
返回序列seq中的随机一个元素 
sample(seq,n)
从序列seq中随机选择 n个不同的元素 
'''
#循环检测生成100次随机数内这一数据的平均概率分布(40%~60%)
import random
lists=[0]*10
for n in range(1,101):
    sum1=0
    for i in range(1,101):
        aa=random.randrange(0,2,1)
        sum1=sum1+aa
    average=sum1/100
    for a in range(0,10): 
        if average>(a*2+39.5)/100 and average<(a*2+41.5)/100:
            lists[a]+=1
        else:
            pass
print("生成100次随机数内这一数据的平均概率分布(40%~60%)")
for a in range(0,10):
    print("%d到%d占比："%(a*2+40,a*2+42),end="")
    print("*"*lists[a]," ",lists[a]/100)



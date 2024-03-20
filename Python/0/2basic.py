#import是导入模块
import math
math.sin(0.8)

from math import sin#只导入math中的sin（节省时间）
sin(1.14514)#用from import导入的好处是不用打math.sin了

from math import *#导入math中全部的对象，会减慢速度

x=3#直接自动定义为整型
type(x)
type (x)==float#x是否为float

#python中再次定义同一个变量会导致前一个失效、
x=2
x=[1,2,3]
print(x)

#bytes类型：
x = b"hello"
y = x[1:3] # 切片操作，得到 b"el"
z = x + b"world" # 拼接操作，得到 b"helloworld"


#分数和复数
from fractions import Fraction
x=Fraction(3,5)
y=Fraction(4,5)
x**2
x.numerator


x=3+4j
abs(x)
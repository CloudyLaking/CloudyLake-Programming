#输入
a=int(input("共有多少头？"))
b=int(input("共有多少脚？"))

#执行
r=[x for x in range(1, a+1) if x*4 + (a - x) * 2 == b]
c=b/2-r

#输出
print("鸡：",c)
print("兔：",r)
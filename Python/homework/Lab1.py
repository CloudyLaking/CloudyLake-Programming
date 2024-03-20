#1.提示”Radius？ “，等待用户输入；
a=float(input("Radius?"))
#2.换行

#3.输出面积
print("Area is:",float(a**2))
#4.显示面积的整数部分是几位数
s=str(int(a**2))
位数=len(s)
print("The integral is a %d-digit number"%位数)
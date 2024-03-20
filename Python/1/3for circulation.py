for num in range(10,20):  # 迭代 10 到 20 (不包含) 之间的数字
   for i in range(2,num): # 根据因子迭代
      if num%i == 0:      # 确定第一个因子
         j=num/i          # 计算第二个因子
         print ('%d 等于 %d * %d' % (num,i,j))
         break            # 跳出当前循环
   else:                  # 循环的 else 部分
      print ('%d 是一个质数' % num)
#把上面print句改成print (num,"等于",i,"*",j)也可以，不过这里输出的j是float，要在上面将j限定为int


#第二个实例
for letter in 'Python':    
   print("当前字母: %s" % letter)
for letters in list:
    print(letters)

#还可以通过索引控制循环：
fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
   print ('当前水果 : %s' % fruits[index])
print ("Good bye!")


#还可以用for循环函数中的参量：
sequence = [12, 34, 34, 23, 45, 76, 89]
for i, j in enumerate(sequence):
     print (i,j)

#for浮点递增
import numpy as np
#方法一按步长
for i in np.arange(0.1, 0.5, 0.01):
    print(i)
#方法二按分段数
for i in np.linspace(0.1, 0.5, 5):
    print(i)


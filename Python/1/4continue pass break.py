#continue在循环中起到一个删除的作用，将循环中的这一个点删掉
var = 10
while var > 0:
    var = var -1
    if var == 5 or var == 8:
        continue
    print ('当前值 :', var)
print ("Good bye!")

#break就是一个直接停止的作用，后面不会继续了
 
for letter in 'Python':     # 第一个实例
   if letter == 'h':
      break
   print ('当前字母 :', letter)
var = 10                    # 第二个实例
while var > 0:              
   print( '当前变量值 :', var)
   var = var -1
   if var == 5:   # 当变量 var 等于 5 时退出循环
      break
 
print ("Good bye!")

#pass是起到一个填补的作用，如果说没有想好写什么可以先弄个pass
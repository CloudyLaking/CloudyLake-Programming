#函数的变量输入其实没有顺序
def printf(a,b):
    print(a,b)
printf(b=10,a=20)#指定到对象





# 可写函数说明
def printinfo( arg1, *vartuple ):
   "打印任何传入的参数"
   print ("输出: ")
   print (arg1)
   print (vartuple)
 
# 调用printinfo 函数
printinfo( 70, 60, 50 )
>>70
>>(60, 50)

#**改为用字典导入
def functionname([formal_args,] **var_args_dict ):
   "函数_文档字符串"
   function_suite
   return [expression]

#*可以单独出现，但是单独出现后后面的参数输入值时必须写c=...

#需要注意函数单独用并不改变原值
#a+10和a=a+10是不一样的
#不过你可以在函数的第一句写个global a，并且不必要return a，这样a就是全局更改了

#函数返回值可以多个一起返回，不过是元组形式
def f():
  return 1,2,3
print(f())
#不过
a,b,c=f()#如果这样接收的话就成功完成了拆包，元组被拆解


#@修改函数内容（修饰器）
def log(pr):#将被装饰函数传入
    def wrapper():
        print("**********")      
        return pr()#执行被装饰的函数
    return wrapper#将装饰完之后的函数返回（返回的是函数名）
@log
def pr():
    print("我是小小洋")
pr()
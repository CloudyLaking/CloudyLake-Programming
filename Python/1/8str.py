a = "Hello"
b = "Python"
if( "H" in a) :#还有not in也是运算符
    print ("H 在变量 a 中" )
else :
    print ("H 不在变量 a 中" )
#转义字符前再加\就可以输出原字符，你也可以用r"\n"或R"\n"

#更新字符串
var1 = 'Hello World!'
print ("已更新字符串 : ", var1[:6] + 'Runoob!')

#转义字符
'''
\000:空
\b:退格 >>>print("Hello \b World!")  Hello World!
\v纵向制表符
\t横向制表符
\v	纵向制表符	
ex:
>>> print("Hello \v World!")
Hello 
       World!
>>>
\t	横向制表符	
>>> print("Hello \t World!")
Hello      World!

\r:将\r后面的内容移到字符串开头，并逐一替换开头部分的字符，直至将 \r 后面的内容完全替换完成。
\f:换行
'''
input()
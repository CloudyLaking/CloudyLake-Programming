#python字符串可以用单、双等等引号作为定界符
#不同定界符可以嵌套
x='why'
y="\nyou"#\n加在这里无效
x+=y

z='你雅'
z.encode('utf-8')#
z.encode('GBK')
_.decode('gbk')#下划线表示最后一次输出结果，decode变回来

#python中的序列类型：list（列表）,tuple（元组）,dict（字典）,set（集合），此外还有string字符串
#字符串不可修改
#元组不能修改，相当于只读列表，标识用()
#列表用[],字典用{}
#列表是有序的，字典是无序的
#dict的方式就是将list中的序号变为了代号，用dict1={"1":"111","2":"222"}这样或者>>> dict(Runoob=1, Google=2, Taobao=3)来定义
#集合是不能有重复元素的用set1={}或set1=set()定义(得要用小括号因为大括号是dict)
#list是最常用的类型:

#数字类型：
#int（有符号整型）
#long（长整型，也可以代表八进制和十六进制）
#float（浮点型）
#complex（复数） complex(a,b)==a+bj

"""
python中的if语句：
if 条件:
    ...
else:
    ...
elif 另一个条件: 
也可以用：... if 条件 else条件
行为 if 条件 else 行为 条件 else 行为 条件

需要注意python没有switch语句
但是3.10之后加入了match语句，其实和switch是一样的
match a:
    case 1:
        print("yes")
    case 2:
        print("nmd")

case也可同时设置多个相同条件：
case 1|2|3|a：
"""

"""
python if中and运算判断采取短路原则，前面判断完毕就不会看后面：
a=0
b=1
if ( a > 0 ) and ( b / a > 2 ):
    print "yes"
else :
    print "no"

如果把and改成or就会报错
"""
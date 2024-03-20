#Python 有两种错误很容易辨认：语法错误和异常
#try是跳过可能出现的错误的方法
try:
    runoob()
except AssertionError as error:
    print(error)
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
finally:
    print('这句话，无论异常是否发生都会执行。')

#上述在try未发生时不执行except，else
#出现了AssertionError就执行这个
#其余错误都是else
#无论如何都会执行finally

#with语法弥补错误，相当于封装了try except finally，就像推导式：
#关键词 with 语句就可以保证诸如文件之类的对象在使用完之后一定会正确的执行他的清理方法:
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
#用完就关了

#assert提前判断谁是错误，直接终止
assert expression
等于
if not expression:
    raise AssertionError
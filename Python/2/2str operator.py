'''
ods(),chr()在unicode和字符串之间转换类型
len()字符串长度

maketrans()制作翻译表，比如定义一个翻译表transtab=str.maketrans("123","abc")
之后调用str.translate(transtab)将str中的字符对应映射换掉


'''

#join()
s1 = "-"
s2 = ""
seq = ("r", "u", "n", "o", "o", "b") # 字符串序列
print (s1.join( seq ))
print (s2.join( seq ))

#ljust(),rjust(),zfill()都是填充0的函数

#index(),rindex()都是寻找函数
#但是没找到会报错
#要判断有没有还是要find()

#lstrip(),rstrip删掉左右开头的某某字符，
#用strip两边都截取
#replace(a,b,c)就是直接替换,c是最大次数

#split在字符串有空格的地方截断，截成一个list

#startswith,endswith判断是否以某一个字符开头结尾
#注意有个s别打错了

#探究isdigit和isnumeric的区别
    dgt=[]
    num=[]
    c=0
    for c in range(2**16):
            ch=chr(c)
            if ch.isdigit():dgt+=ch
            if ch.isnumeric():num+=ch
    print('digits:',dgt)
    print('numeric:',num)

#倒序输出str[::b] 
# [::b]表示的其实是空多少个输出一个，负数就是倒着来输出了
#这个数不能是0
#[b::]和[b:]是一个意思
a=[1,2,3,4,5]
print(a[::-1])    # 取从后向前（相反）的元素
>>>[ 5 4 3 2 1 ]#从第一个（-1）到最后
print(a[::-2])
>>>[5,3,1]
print(a[-2::])
>>>[4,5]#与a[-2:]是一样的
print(a[1::2])#从第二个开始（index1），每两个一取
>>>[2,4]
print(a[-2:])
>>>[4,5]#0是最后一个,-2就是第3个，表示从-2到0，第四个到第五个
print(a[:-2])
>>>[1.2]

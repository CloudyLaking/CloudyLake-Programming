#推导式是独特的数据处理方式
#可以从一个数据序列构建另一个新的数据序列的结构体

#例
names = ['Bob','Tom','alice','Jerry','Wendy','Smith']
new_names = [name.upper()for name in names if len(name)>3]
print(new_names)
>>>['ALICE', 'JERRY', 'WENDY', 'SMITH']

multiples = [i for i in range(30) if i % 3 == 0]
print(multiples)
>>>[0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
mm=[i for i in multiple[2:] if i%2==0]
print(mm)

#例二
list1 = ['python', 'test1', 'test2']
list2 = [word.title() if word.startswith('p') else word.upper() 
        for word in list1]#这样写会清楚很多
print(list2)
>>>['Python', 'TEST1', 'TEST2']

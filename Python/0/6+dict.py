#dict的一些小拓展

#可以用item直接输出
dict1 = {'abc':1,"cde":2,"d":4,"c":567,"d":"key1"}
for k,v in dict1.items():
    print(k,":",v)

#enumerate()还可以查看索引
for i,x in enumerate(dict1):
    print(i,x)

# fromkeys(seq,value) 函数用于创建一个新字典，
# 以序列 seq 中元素做字典的键，value 为字典所有键对应的初始值

#通过两个列表建立映射关系的字典：(非常重要)
new_dict=dict(zip(key,value))
#你也可以用for来循环出来
dictionary = {keys[i]:values[i] for i in range(len(keys))}

#通过get()来调出:
print(dd.get(1))#调出第一个value
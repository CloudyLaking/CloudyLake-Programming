list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

#只有一个元素时要加一个逗号，否则括号在定义时会混淆
list=[1,]

print (list)               
print (list[0])         
print (list[1:3])          #需要注意python中的索引规则有变#从负数开始索引也可以
#1：3表示的是第二个和第三个，不是二三四
print (list[2:])          # 第三个后面的
print (tinylist * 2)       # 输出列表两次
print (list + tinylist)    # 组合


print(arrtest[1:-1])    # 从下标为1的数开始，输出到下标为4但不包含4的所有值
#[786, 2.23, 'runoob']
print(arrtest[-3:-2])   # 从下标为2的数开始，输出到下标为3但不包含3的所有值
#[2.23]

#list操作符：
'''
list.sort()对lists首字母排序,()可输入reverse=True倒序
list.clear(),copy(),remove()
注意a=a.remove("char")无论如何会全部删除
只用a.remove就可以了
这和字符串的那些操作符不一样

list.pop(i)
移除列表中位置i的元素（默认最后一个元素），并且返回该元素的值
list.remove(x)
移除值为x的第一个元素

list.append(x)
添加元素

list.insert(i,x)
在i添加一个x

list.reverse()倒转


'''

#使用zip遍历多个列表：
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))
#注意次数受最短的列表影响（木桶效应）
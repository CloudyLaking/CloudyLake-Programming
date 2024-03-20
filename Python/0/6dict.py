dict = {}
dicts=dict()
dict['one'] = "This is one"
dict[2] = "This is two"
 
tinydict = {'name': 'runoob','code':6734, 'dept': 'sales'}
 
 
print (dict['one'])          # 输出键为'one' 的值
print (dict[2])              # 输出键为 2 的值
print (tinydict )            # 输出完整的字典
print (tinydict.keys())      # 输出所有键
print (tinydict.values())    # 输出所有值

'''
dict的方式就是将list中的序号变为了代号
'''
#结果为：
#This is one
#This is two
#{'name': 'runoob', 'code': 6734, 'dept': 'sales'}
#dict_keys(['name', 'code', 'dept'])
#dict_values(['runoob', 6734, 'sales'])

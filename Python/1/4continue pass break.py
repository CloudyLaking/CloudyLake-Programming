#continue��ѭ������һ��ɾ�������ã���ѭ���е���һ����ɾ��
var = 10
while var > 0:
    var = var -1
    if var == 5 or var == 8:
        continue
    print ('��ǰֵ :', var)
print ("Good bye!")

#break����һ��ֱ��ֹͣ�����ã����治�������
 
for letter in 'Python':     # ��һ��ʵ��
   if letter == 'h':
      break
   print ('��ǰ��ĸ :', letter)
var = 10                    # �ڶ���ʵ��
while var > 0:              
   print( '��ǰ����ֵ :', var)
   var = var -1
   if var == 5:   # ������ var ���� 5 ʱ�˳�ѭ��
      break
 
print ("Good bye!")

#pass����һ��������ã����˵û�����дʲô������Ū��pass
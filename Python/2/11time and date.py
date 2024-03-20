#date日期函数
import datetime
#获取当前日期和时间
current_datetime = datetime.datetime.now()
print(current_datetime)
# 获取当前日期
current_date = datetime.date.today()
print(current_date)
# 格式化日期
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_datetime)  # 输出：2023-07-17 15:30:45

#使用timeit.timer来进行性能测试
>>> from timeit import Timer
>>> Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
0.57535828626024577

#也可以使用time.time()相减得到


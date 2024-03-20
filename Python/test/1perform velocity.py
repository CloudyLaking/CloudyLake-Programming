import time
a=time.time()
for i in range(500000):
    print(i)
b=time.time()
print("%5f"%(b-a))
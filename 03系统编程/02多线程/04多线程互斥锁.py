#引入threading模块的互斥锁和多线程
from threading import Lock,Thread 
import time
#创建全局变量 num
num = 0

#创建函数
def func1():
	global num
	#上锁
	mutex.acquire()
	print("fun1锁上了")
	for n in range(1000000):
		num += 1
	print("全局变量num修改为%d"%num)
	mutex.release()
	print("fun1解开了")

def func2():
	global num
	#上锁
	mutex.acquire()
	print("fun2锁上了")
	for n in range(1000000):
		num += 1
	print("全局变量num修改为%d"%num)
	mutex.release()
	print("fun2解开了")

#创建多线程和锁
mutex = Lock()
threading1 = Thread(target=func1)
threading1.start()
threading2 = Thread(target=func2)
threading2.start()
	
mutex.acquire()
print("主线程锁上了")
print(num)
mutex.release()
print("主线程解开了")


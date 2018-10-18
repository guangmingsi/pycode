from threading import Thread 

#定义全局变量num
num = 0

#定义函数
def func1():
	global num #声明用的全局变量
	for n in range(1000000):
		num +=1
	print("num的值是----%d---"%num)

def func2():
	global num #声明用的全局变量
	for n in range(1000000):
		num +=1
	print("num的值是----%d---"%num)
#创建2个线程

thread1 = Thread(target=func1)
thread1.start()
thread2 = Thread(target=func2)
thread2.start()
print("num最终值是----%d---"%num)
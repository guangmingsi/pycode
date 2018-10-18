from multiprocessing import Pool
import os,time
def test():
	for i in range(3):
		print("-----1----进程id%s"%os.getpid())
		time.sleep(1)


p = Pool(3)#3进程池有3个进程

for i in range(6):
	p.apply_async(test)#调用进程去执行test函数，调用6次但是只有3个，
	#先分配3个进程去执行
	#3个进程执行完之后再去执行剩下的3个
p.close()#关闭进程池，进程池不能在调用
"""for i in range(10):
	p.apply_async(test)""" #报错了 关闭后在调用会崩溃
p.join()

print("进程结束")


from multiprocessing import Pool
import time
import os

def test(num):
	print("子进程工作了")
	for i in range(5):
		print("子进程号%s----进程id%d--"%(num,os.getpid()))

P = Pool(2)
for num in range(5):
	P.apply(test,(num,)) #这里是随机调用进程池里的进程？
P.close()
P.join()
print("子进程都结束完了，父进程可以结束了")
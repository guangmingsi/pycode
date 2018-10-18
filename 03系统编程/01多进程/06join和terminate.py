from multiprocessing import Process
import os
import time
def run(name,age):
	for i in range(10):
		print("子进程运行中，name%s，age%d，进程%d"%(name,age,os.getpid()))
		time.sleep(1)
if __name__ == '__main__':
	p = Process(target=run, args=("hong",18))
	p.start()
	time.sleep(1)
	p.terminate() #直接结束
	#p.join() 等待子进程结束
	print("子进程结束")
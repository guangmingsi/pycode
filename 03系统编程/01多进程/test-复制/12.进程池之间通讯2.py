from multiprocessing import Manager,Pool
import time,random

def write(q,num):
	for i in num:
		if not q.full():
			print("写入队列---%s---"%i)
			q.put(i)
			

def read(q):
	print("开始读取了")
	while True:
		if not q.empty():
			print("读取队列内容---%s---"%q.get())
		else:
			break
#创建一个进程池
p = Pool()
#创建一个进程池用的队列queue
q = Manager().Queue()
#让进程1去执行write函数
p.apply(write,(q,[x for x in range(7)]))
#让进程2去执行read函数
p.apply(read,(q,))

p.close()
p.join()
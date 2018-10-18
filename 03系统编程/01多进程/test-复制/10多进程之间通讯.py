from multiprocessing import Queue,Process
import time

def writ(q):
	print("开始写入队列")
	for i in ["A","b","C","D"]:
		if not q.full():
			q.put(i)
			print("正在写入--%s--"%i)
def read(q):
	print("开始读取队列")
	while True:
		if not q.empty():
			print("正在读取---%s--"%q.get())
		else:
			break

q = Queue()
p = Process(target=writ,args=(q,))
p2 = Process(target=read,args=(q,))
p.start()
p.join()
p2.start()
p2.join()
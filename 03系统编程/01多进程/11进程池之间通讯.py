from multiprocessing import Pool,Manager

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
p = Pool()
q = Manager().Queue()
p.apply(writ,(q,))
p.apply(read,(q,))
p.close()
p.join()
#引入模块
from threading import Thread 
import threading
import time
from queue import Queue

#重写threading.Thread类
class Thread_product(threading.Thread):
	"""docstring for Thread_product"""

	def run(self):
		global queue
		count = 0
		while True:
			if queue.qsize() < 1000:
				for i in range(100):
					count += 1
					msg ="生产产品"+str(count)
					queue.put(msg)
					print(self.name+msg)
			time.sleep(0.5)

class Thread_customer(threading.Thread):
	"""docstring for Thread_product"""

	def run(self):
		global queue
		while True:
			if queue.qsize() > 100:
				for i in range(3):
					msg=self.name+"消耗了%s"+queue.get()
					print(msg)
			time.sleep(1)


#创建队列
queue = Queue()
#创建初始队列
for n in range(100):
	queue.put("生产初始产品%s"%str(n))
#创建多线程
for n1 in range(2):
	t = Thread_product()
	t.start()
for n2 in range(5):
	t1 = Thread_customer()
	t1.start()

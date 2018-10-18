from threading import Thread
import time
def test():
	print("线程开始工作啦--")
	time.sleep(1)

for i in range(5):
	t = Thread(target=test)
	t.start()
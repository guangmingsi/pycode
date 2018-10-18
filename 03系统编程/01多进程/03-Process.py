from multiprocessing import Process
import time

def test():
	while True:
		print("----1------")
		time.sleep(1)
p=Process(target=test)
p.start()
p.stop()
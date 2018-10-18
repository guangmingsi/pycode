from multiprocessing import Process
def test():
	for i in range(5):
		print("-----我是子进程，我结束了你才能结束-------")

p = Process(target=test)
p.start()
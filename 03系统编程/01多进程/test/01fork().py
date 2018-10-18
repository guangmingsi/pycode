import os
import time

def test_fork_func():
	ret = os.fork()
	while True:
		if ret == 0:
			print("----1-----")
			time.sleep(1)
		else:
			print("------2-----")
			time.sleep(1)
test_fork_func()



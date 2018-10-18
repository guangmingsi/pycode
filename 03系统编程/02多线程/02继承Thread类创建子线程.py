import threading
import time

class thread_son(threading.Thread):
    """docstring for thread_son"""


    def run(self):
        time.sleep(1)
        for i in range(5):
            print("子线程开始工作了")
            msg = "我是--"+self.name
            print(msg)

thread = thread_son()
thread.start()
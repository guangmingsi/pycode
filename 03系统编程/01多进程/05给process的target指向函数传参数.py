from multiprocessing import Process
import os

def test(num,num1):
    print("pid=%d,ppid=%d,,,,num=%d,num1=%d"%(os.getpid(), os.getppid(), num,num1))


p = Process(target=test, args=(100,200))#给target指向的函数传递元祖参数
p.start()
print("----main--pid=%d--"%os.getpid())
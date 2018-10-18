from multiprocessing import Pool,Manager
import os

def copy(queue,name,old_filed_name,new_filed_name):
	fr = open(old_filed_name+"/"+name)
	fw = open(new_filed_name+"/"+name,"w")
	content = fr.read()
	fw.write(content)

	fr.close()
	fw.close()

	queue.put(name)

#获取要复制的文件夹名称 test
old_filed_name = input("输入要复制的文件夹名称")

#新建一个复制的文件夹
new_filed_name = old_filed_name + "-复制"
os.mkdir(new_filed_name)
#获取被复制文件夹的文件列表

listname = os.listdir(old_filed_name)
print(listname)
#创建子进程池
pool = Pool(2)

#创建进程队列queue
queue = Manager().Queue()
#根据列表，分配给子进程去copy
for name in listname:
	pool.apply_async(copy,(queue,name,old_filed_name,new_filed_name))
num = 0
allNum = len(listname)-1
print(len(listname))
while True:
	queue.get()
	num += 1
	percent = num/allNum
	print(num)
	print("\r进度%.2f%%"%(percent*100),end=" ")
	if num == allNum:
		break
print("copy完成")






#主进程现实复制进度
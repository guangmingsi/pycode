import threading

#创建threading local对象作为全局变量

local_student = threading.local()

def show_student_name():
	print(local_student.name)


def set_student_name(name):
	local_student.name = name 
	show_student_name()

t1 = threading.Thread(target=set_student_name,args=("laoWang",))
t1.start()
t2 = threading.Thread(target=set_student_name,args=("dongGe",))
t2.start()
def wi(func):
	def inner():
		print("正在验证")
		func()
	return inner
@wi
def f1():
	print("hello,world")
@wi
def f2():
	print("heihei,haha")
f1()
f2()
def zhuang(func):
	def cheng(*args,**kwargs):
		print("闭包功能相乘")
		rs=1
		for i in args:
			rs=rs*i
		print(rs)

		func(*args,**kwargs)
	return cheng	



@zhuang # operate=zhuang（operate）
def operate(a,b,c,d):
	print(a+b+c+d)
	print("%d,%d,%d,%d"%(a,b,c,d))
operate(2,2,3,4)
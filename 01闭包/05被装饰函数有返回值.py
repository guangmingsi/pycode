def zhuangshi(func):
	def extend(*args,**kwargs):
		if min(*args)<0:
			print("error min_num<0")
		else:
			x=func(*args,**kwargs)
			return x
			


	return extend 




@zhuangshi
def sum(a,b):
	return "求和结构%d"%(a+b)
f=sum(1,-2)
if f:
	
	print(f)
else:
	print("oh error")

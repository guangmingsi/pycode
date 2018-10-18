def outfunc(arg):
	def zhuangshi1(func):
		def zhuangshi2(*args,**kwargs):
			if arg=="01":
				func(*args,**kwargs)
				func(*args,**kwargs)
			if arg=="02":
				func(*args,**kwargs)
		return zhuangshi2
	return zhuangshi1
@outfunc("01")
def sum(a,b):
	 print(a+b)
sum(1,2)

@outfunc("02")
def sum(a,b,c):
	print(a+b+c)
sum(1,2,3)
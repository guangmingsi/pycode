def creatuum():
	a,b=0,1
	for i in range(5):
		yield b #程序运行到这个地方的时候，函数停了，把yield后面的值返回
		a,b=b,a+b
a=creatuum()#调用函数实际上就是创建生成器对象，生成器对象返回yield后面的b的值
#for x in a: #每循环一次 从生成器里取出一个值，遍历生成器
#	print(x)

#for x in creatuum():
#	print(x)
#ret=a.__next__()
#print(ret)
#上下两种方式都可以
ret=next(a)
print(ret)
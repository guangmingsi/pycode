def zhuangshi1(func):
	def zhuang():
		print("调用zhuangshi1函数的闭包函数")
		return "装饰1"+func()#被装饰的函数
	return zhuang
def zhuangshi2(func):
	def zhuang():
		print("调用zhuangshi2函数的闭包函数")
		return'装饰2'+func()
	return zhuang

@zhuangshi1
@zhuangshi2
def fun():
	return "我是被装饰的函数"
print(fun())
"""调用zhuangshi1函数的闭包函数
调用zhuangshi2函数的闭包函数
装饰1装饰2我是被装饰的函数
[Finished in 0.0s]"""
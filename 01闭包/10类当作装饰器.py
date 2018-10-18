class Zhuangshi(object):
	def __init__(self,func):
		print("装饰器函数启动")
		self.__func=func
	def __call__(self):
		print("开始装饰")
		return self.__func
@Zhuangshi
def test():
	print("---test----")
test()

"""原理：用类当作装饰器相当于把被装饰函数当作参数传入到类中，然后创建一个
函数名字的对象，test=Zhuangshi（test），装饰后调用test（）相当于直接调用类
对象，会调用重写的call方法，call方法内可以扩展功能，最后返回self.__func,这个属性
保存的是原函数的引用，所以最后不影响远函数调用。"""
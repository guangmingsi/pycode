#应为python是动态语言，所以定义了class类后可以动态增加参数
""""
class Person(object):
		def __init__(self,name,age):
			self.name=name
			self.age=age
p=Person("liu",20)
p.sex="男"
print(p.sex)#动态添加了sex属性
"""
class Person(object):
	"""docstring for Person"""
	__slots__=("name","age")
	def __init__(self,name,age):
		self.name = name
		self.age=age
p=Person("liu",20)
p.sex="男"
print(p.sex)#出错，无法调用sex属性
		
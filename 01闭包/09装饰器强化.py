def note(func):
	def wrapper():
		"??????"
		print("note something")
		return func()
	return wrapper
@note
def test():

	print("i am test")
test()
print(test.__doc__)

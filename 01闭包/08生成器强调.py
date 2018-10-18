def test():
	i =0
	while i<5:
		if i==0:
			temp=yield i
			print(temp)
		else:
			yield i
		i+=1
t=test()
t.send(None)
t.send("haha")
t.__next__()
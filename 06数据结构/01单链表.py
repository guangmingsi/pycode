class SingleNode(object):
	def __init__(self,item):
		self.item =item
		self.next = None


class SingleLinkList(object):
	def __init__(self,node=None):# node是节点对象
		self._head = node

	def is_empty(self):
		return self._head == None

	def length(self):
		cur = self._head
		count = 0
		while cur != None:
			cur =cur.nex
			count +=1
		return count
	def trave(self):
		cur = self._head

		while cur !=None:
			print(cur.item)
			cur = cur.next

	def append(self,item):
		node = SingleNode(item)
		if self.is_empty():
			self._head = node
		else:
			cur = self._head
			while cur.next != None:
				cur =cur.next
			cur.next = node
if __name__ == '__main__':
	node = SingleNode(1)
	ll = SingleLinkList(node)
	ll.append(2)

	ll.append(3)
	ll.append(4)
	ll.trave()			
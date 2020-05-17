#!/Users/brijeshjotaniya/opt/anaconda3/bin/python
# Doubly Linked List implementation

class dbllNode(object):
	def __init__(self, data):
		self.data = data
		self.next_node = None
		self.prev_node = None

class mydbll(object):
	def __init__(self):
		self.head = None
		self.tail = None
		self.size = 0
	def insertHead(self, data):
		self.size += 1
		new_node = dbllNode(data)
		if self.head is None:
			self.head = new_node
			self.tail = new_node
		else:
			self.head.prev_node = new_node
			new_node.next_node = self.head
			self.head = new_node
		return
	def insertTail(self, data):
		self.size += 1
		new_node = dbllNode(data)
		if self.tail is None:
			self.tail = new_node
			self.head = new_node
		else:
			self.tail.next_node = new_node
			new_node.prev_node = self.tail
			self.tail = new_node
		return
	def removeNodeChkH2T(self, data):
		cur_node = self.head
		if cur_node is None:
			return
		elif cur_node.data == data:
			self.size -= 1
			cur_node.next_node.prev_node = None
			self.head = cur_node.next_node
		else:
			while cur_node!=None and cur_node.data != data:
				cur_node = cur_node.next_node
			if cur_node == None:
				print(f'Item {data} not found in this Doubly Linked List')
			else:
				cur_node.prev_node.next_node = cur_node.next_node
				cur_node.next_node.prev_node = cur_node.prev_node
		return
	def removeNodeChkT2H(self, data):
		cur_node = self.tail
		if cur_node is None:
			return
		elif cur_node.data == data:
			self.size -= 1
			cur_node.prev_node.next_node = None
			self.tail = cur_node.prev_node
		else:
			while cur_node!=None and cur_node.data != data:
				cur_node = cur_node.prev_node
			if cur_node == None:
				print(f'Item {data} not found')
			else:
				cur_node.prev_node.next_node = cur_node.next_node
				cur_node.next_node.prev_node = cur_node.prev_node
		return
	def TraverseH2T(self):
		cur_node = self.head
		if cur_node == None:
			return
		else:
			while cur_node != None:
				print(f'Traversing H2T, {cur_node.data}')
				cur_node = cur_node.next_node
		return
	def TraverseT2H(self):
		cur_node = self.tail
		if cur_node == None:
			return
		else:
			while cur_node != None:
				print(f'Traversing T2H, {cur_node.data}')
				cur_node = cur_node.prev_node
		return
	def getSize(self):
		return self.size

def main():
	mydoublylinkedlist = mydbll()
	mydoublylinkedlist.insertHead(12)
	mydoublylinkedlist.insertHead(10)
	mydoublylinkedlist.insertTail(14)
	mydoublylinkedlist.TraverseH2T()
	mydoublylinkedlist.insertHead(8)
	mydoublylinkedlist.removeNodeChkH2T(10)
	mydoublylinkedlist.insertHead(6)
	mydoublylinkedlist.insertTail(16)
	mydoublylinkedlist.insertTail(18)
	mydoublylinkedlist.TraverseT2H()
	mydoublylinkedlist.removeNodeChkT2H(18)
	mydoublylinkedlist.TraverseT2H()
	mydoublylinkedlist.TraverseH2T()
	mydoublylinkedlist.removeNodeChkT2H(14)
	mydoublylinkedlist.removeNodeChkH2T(4)
	mydoublylinkedlist.TraverseH2T()
	mydoublylinkedlist.TraverseT2H()
	mydoublylinkedlist.removeNodeChkH2T(6)
	print(f'Size of the Doubly Linked List is {mydoublylinkedlist.getSize()}')

	return

if __name__ == '__main__':
	main()
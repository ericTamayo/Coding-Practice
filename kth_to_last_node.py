# Write a function kth_to_last_node() that takes an 
# integer kk and the head_node of a singly linked list,
# and returns the kkth to last node in the list.
class LinkedListNode:

	def __init__(self, value):
		self.value = value
		self.next  = None

def kth_to_last_node(k = 0, head = None):
	if k < 1:
		raise ValueError ("Can not find node before 1st Node")
	
	count = 1
	temp = head
	#Find length of list
	while(temp.next != None):
		count += 1
		temp = temp.next 
	
	if k > count:
		raise ValueError("Can not find value larger than list size")

	term = count - k - 1
	
	returnMe = head.next
	for i in range(0,term):
		returnMe = returnMe.next
	return returnMe.value

try:
	a = LinkedListNode("Angel Food")
	b = LinkedListNode("Bundt")
	c = LinkedListNode("Cheese")
	d = LinkedListNode("Devil's Food")
	e = LinkedListNode("Eccles")

	a.next = b
	b.next = c
	c.next = d
	d.next = e

	# returns the node with value 
	# "Devil's Food" (the 2nd to last node)
	print kth_to_last_node(2, a)

except KeyboardInterrupt:
	print "\n"
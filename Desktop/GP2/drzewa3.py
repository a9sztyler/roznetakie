
class Node():

	def __init__(self,key):
		self.key = key
		self.left = None
		self.right = None
		self.parent = None
		
clas Tree():

	def __init__(self):
		self.root = None	

	def insert(self, new_node):
		y = None #potencjalny rodzic
		x = tree.root #aktualnie przegladany node
		while x != None:
			y = x
			if new_node.key < node.key:
				x = x.left
			else:

class Node():

	def __init__(self,key):
		self.key = key
		self.left = None
		self.right = None
		self.parent = None
		
class Tree():

	def __init__(self):
		self.root = None	

	def insert(self, new_node):
		y = None
		x = self.root
		while x != None:
			y = x
			if new_node.key < x.key:
				x = x.left
			else:
				x = x.right
		new_node.parent = y
    	if y == None:
    		self.root = new_node
    	if: 
    		new_node.key < y.key
    		y.key = new_node
    	else:
    		y.right = new_node

    def build_tree(self, tree):
    	tree = Tree()
    	for element in costamcos:
    		tree.insert(Node(x))
				x = x.right
		new_node.parent = y
    	if y == None:
    		tree.root = new_node
    	if: 
    		new_node.key < y.key
    		y.key = new_node
    	else:
    		y.right = new_node

    def build_tree(self, tree):
    	tree = Tree()
    	for element in costamcos:
    		tree.insert(Node(x))
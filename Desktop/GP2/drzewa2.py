import random as random

#my_randoms=[random.randrange(1,101,1) for _ in range (10)]
#print my_randoms 

my_randoms = [47, 66, 21, 74, 73, 17, 79, 34, 90, 51]

class Tree:
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left  = left
        self.right = right

    def __str__(self):
        return str(self.cargo) + " " + str(self.left.cargo) + " " + str(self.right.cargo)

    def insert(self, element, node):
    	if element < node.cargo:
    		if node.left:
    			self.insert(element, node.left)

    		else:
    			dziecko = Tree(element)
    			node.left = dziecko

    	else:
    		if node.right:
    			self.insert(element, node.right)
    		else:
    			dziecko = Tree(element)
    			node.right = dziecko

    def build_tree(self, drzewo):
    	for element in my_randoms[1:]:
			drzewo.insert(element, drzewo)
    	
    	
drzewo = Tree(my_randoms[0]) 
drzewo.build_tree(drzewo)

print my_randoms
print drzewo
#print drzewo.right.right

from Bio import Phylo
from cStringIO import StringIO

drzewo_newick = "(((A, B), C), (D, E))"

drzewo_phylo = Phylo.read(StringIO(drzewo_newick), "newick")
#print drzewo_phylo

lista_drzewo_phylo = []
lista_drzewo_phylo_rev = []


def distance(s):???????????????????
for element in drzewo_newick:
	if element == "(":


for element in drzewo_phylo.find_clades():
	if str(element) != "Clade":
		lista_drzewo_phylo.append(element)

for i in reversed(lista_drzewo_phylo):
	lista_drzewo_phylo_rev.append(i)

#print lista_drzewo_phylo_rev		

class Node():

	def __init__(self,key):
		self.key = key
		self.left = None
		self.right = None
		self.parent = None

	def __str__(self):
		return str(self.key) + " " + str(self.left.key) + " " + str(self.right.key) + " " + str(self.parent)

class Tree():

	def __init__(self):
		self.root = None	
	
	def insert(self, ):
		y = None #potencjalny rodzic
		x = self.root #aktualnie przegladany node

		while x is not None:
			y = x
			if new_node.key < x.key:
				x = x.left
			else:
				x = x.right
		new_node.parent = y
		if y == None:
			self.root = new_node

		elif new_node.key < y.key:
			y.left = new_node

		else:
			y.right = new_node

	def build_tree(self, lista):
		for element in lista:
			self.insert(Node(element))


#new_tree = Tree()
#new_tree.build_tree(lista)
#print new_tree
#print "root", new_tree.root.key
#print "right", new_tree.root.right.key
#print "left", new_tree.root.left.key











    		

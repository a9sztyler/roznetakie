class Tree:
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left  = left
        self.right = right

    def __str__(self):
        return str(self.cargo) + #str(self.left.cargo) + str(self.right.cargo)


nowe_drzewo = Tree(21, Tree(2), Tree(3))
#print nowe_drzewo

nowe_drzewo_2 = Tree('kot')

nowe_drzewo_2.left = Tree('pies')
nowe_drzewo_2.right = Tree('malpa')

print nowe_drzewo_2

	#score = 

	def insert(value, cargo):

	def build_tree()

class Node: 
	def __init__(self, children, number, symbol, parent, index, label):
		self.children = children 
		self.number = number 
		self.symbol = symbol 
		self.parent = parent
		self.index = index
		self.label = label 

	def addChildren(self, childToAdd): 
		self.children.append(childToAdd)

	def getChildren(self):
		return self.children 

	def getNumber(self): 
		return self.number 

	def getSymbol(self): 
		return self.symbol

	def getParent(self):
		return self.parent

	def getIndex(self):
		return self.index

	def setNumber(self, num):
		self.number = num

	def setIndex(self, ind):
		self.index = ind

	def setLabel(self, label):
		self.label = label 

	def getLabel(self):
		return self.label

	def createNewEdge(self, middleChild, endChild):
		self.children.remove(middleChild)
		self.children.append(endChild)


def constructTrie(text):
	root = Node([], 0, '', None, 0, -1)
	Trie = [root] 
	number = 0
	for i in range(len(text)):
		currentNode = root 
		for j in range(i, len(text)): 
			currentSymbol = text[j]
			isChild = False 
			for child in currentNode.getChildren(): 
				if child.getSymbol() == currentSymbol: 
					currentNode = child 
					isChild = True 
			
			if isChild == False: 
				number += 1
				newNode = Node([], number, currentSymbol, currentNode, j, -1)
				Trie.append(newNode)
				currentNode.addChildren(newNode)
				currentNode = newNode

		if len(currentNode.getChildren()) == 0: 
			currentNode.setLabel(i)

	#TrieNodes = {}
	#for node in Trie: 
	#	if node.symbol != '': 
	#		number = node.getNumber()
	#		symbol = node.getSymbol()
	#		parent = node.getParent()
	#		parentNumber = parent.getNumber() 
	#		TrieNodes[(parentNumber, number)] = symbol

	return Trie

def depthFirstSearch(trie, root):
	dfsTree = []
	stack = [root]
	while stack:
		vertex = stack.pop()
		dfsTree.append(vertex)
		for child in vertex.getChildren(): 
			stack.append(child)

	return dfsTree

def constructTree(trie, text): 
	edges = [] 
	root = trie[0]
	#print(len(trie))
	stack = [] 
	stack.append(root)
	c = 0
	while stack: 
		c+= 1
		#print('c: ', c)
		currNode = stack.pop()
		#print("CURRNODE: ", currNode.getSymbol(), currNode.getNumber())
		childrenCopies = list(currNode.getChildren())

		for child in childrenCopies: 
			#print('stack : ')
			#for elem in stack:
				#print(elem.getSymbol(), elem.getNumber())

			currChild = child 

			#print('child : ', child.getSymbol(), child.getNumber())


			if len(currChild.getChildren()) == 1:
				nodes = [] 
				nodes.append(currChild)
				length = 2
				currChild = (currChild.getChildren())[0]
				counter = 0
				while (len(currChild.getChildren())) == 1: 
					counter += 1
					#print('counter: ', counter)
					nodes.append(currChild)
					#print(currChild.getSymbol(), currChild.getNumber())
					length += 1
					currChild = (currChild.getChildren())[0]
				currChild.setNumber(length)
				currNode.createNewEdge(child, currChild)
				#print("TO REMOVE:")
				#for i in range(len(nodes)):
					#print(nodes[i].getSymbol(), nodes[i].getNumber())
					#trie.remove(nodes[i])

				stack.append(currChild)
			else:
				length = 1
				currChild.setNumber(length)             
				stack.append(currChild)


	newTree = depthFirstSearch(trie, root)	
	for i in range(len(newTree)):
		node = newTree[i]
		index = node.getIndex()
		length = node.getNumber() 
		#print(node.getIndex(), node.getNumber())
		print(text[index+1-length:index+1])

	return trie
 

def main():
	with open('rosalind_ba9c.txt', 'r') as myfile:
		data = myfile.readlines()
	text = data[0].rstrip('\n')
	

	trie = constructTrie(text)
	tree = constructTree(trie, text)


if __name__ == "__main__":
	main()
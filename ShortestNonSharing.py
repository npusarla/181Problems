class Node: 
	def __init__(self, children, number, symbol, parent, index, label, color):
		self.children = children 
		self.number = number 
		self.symbol = symbol 
		self.parent = parent
		self.index = index
		self.label = label 
		self.color = color

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

	def setSymbol(self, text):
		self.symbol = text

	def setColor(self, color):
		self.color = color 

	def getColor(self):
		return self.color

	def setParent(self, parent):
		self.parent = parent

def constructTrie(text):
	root = Node([], 0, '', None, 0, -1, 'gray')
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
				newNode = Node([], number, currentSymbol, currentNode, j, -1, 'gray')
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
				currChild.setParent(currNode)
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
		newPat = text[index+1-length:index+1]
		#node.setSymbol(newPat)

	trie = newTree
	return trie, root

def treeInitialization(tree, text):
	#make all the leaves either blue or red, find ALL leaves 
	for node in tree: 
		if len(node.getChildren()) == 0: 
			#check which text it is from 
			index = node.getIndex()
			length = node.getNumber() 
			newPat = text[index+1-length:index+1]
			index1 = 99999999
			index2 = 99999999
			if '#' in newPat: 
				index1 = newPat.index('#')
			if '$' in newPat: 
				index2 = newPat.index('$')

			if index1 < index2: 
				node.setColor('blue')
			else: 
				node.setColor('red')

	return tree

def findRipeNodes(tree):
	ripeNodes = []
	for node in tree: 
		if node.getColor() == 'gray':
			children = node.getChildren()
			isGray = False 
			for child in children: 
				if child.getColor == 'gray':
					isGray = True 

			if isGray == False: 
				ripeNodes.append(node)

	return ripeNodes


def treeColoring(tree, text):
	tree = treeInitialization(tree, text) 
	while(len(findRipeNodes(tree))>0):
		ripeNodes = findRipeNodes(tree)
		for node in ripeNodes: 
			colors = []
			children = node.getChildren()
			for child in children: 
				if child.getColor() not in colors: 
					colors.append(child.getColor())

			if len(colors) > 1: 
				node.setColor('purple')

			elif len(colors) == 1: 
				color = colors[0]
				node.setColor(color)

	return tree

def findShortestSubstring(tree, text, root):
	tree = treeColoring(tree, text)
	queue = [] 
	nodePaths = {}
	for child in root.getChildren(): 
		if child.getColor() != 'red': 
			index = child.getIndex()
			length = child.getNumber() 
			newPat = text[index+1-length:index+1]
			if child.getColor() == 'purple':
				nodePaths[child] = newPat
				queue.append(child)
			elif child.getColor() == 'blue':
				nodePaths[child] = newPat[0]

	while queue: 
		vertex = queue[0]
		queue.remove(vertex)
		oldPat = nodePaths[vertex]
		for child in vertex.getChildren(): 
			index = child.getIndex()
			length = child.getNumber() 
			newPat = text[index+1-length:index+1]
			if child.getColor() == 'purple': 
				nodePaths[child] = oldPat + newPat
				queue.append(child)
			elif child.getColor() == 'blue':
				nodePaths[child] = oldPat + newPat[0]

	minString = text
	for key in nodePaths.keys():
		if key.getColor() == 'blue':
			string = nodePaths[key]
			if '#' not in string:
				if len(string) < len(minString):
					minString = string

	return minString


def main():
	with open('rosalind_ba9f.txt', 'r') as myfile:
		data = myfile.readlines()
	
	text1 = data[0].rstrip('\n')
	text2 = data[1].rstrip('\n')
	
	text1 += '#'
	text2 += '$'
	finalText = text1 + text2
	suffixTrie = constructTrie(finalText)
	suffixTree, root = constructTree(suffixTrie, finalText)
	pattern = findShortestSubstring(suffixTree, finalText, root)

	print(pattern)

if __name__ == "__main__":
	main()
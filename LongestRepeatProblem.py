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
	stack = [] 
	stack.append(root)
	c = 0
	while stack: 
		c+= 1
		currNode = stack.pop()
		childrenCopies = list(currNode.getChildren())

		for child in childrenCopies: 
			currChild = child 

			
			if len(currChild.getChildren()) == 1:
				nodes = [] 
				nodes.append(currChild)
				length = 2
				currChild = (currChild.getChildren())[0]
				counter = 0
				while (len(currChild.getChildren())) == 1: 
					counter += 1
					nodes.append(currChild)
					length += 1
					currChild = (currChild.getChildren())[0]
				currChild.setNumber(length)
				currNode.createNewEdge(child, currChild)
				
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
		#print(text[index+1-length:index+1])

	return newTree, root 

def findLongestRepeat(suffixTree, text, root):
	queue = [] 
	nodePaths = {}
	for child in root.getChildren(): 
		if len(child.getChildren()) > 0: 
			queue.append(child)
			nodePaths[child] = (child.getIndex(), child.getNumber())
	while queue: 
		vertex = queue[0]
		queue.remove(vertex)
		length = nodePaths[vertex][1]
		for child in vertex.getChildren(): 
			if len(child.getChildren()) > 0: 
				queue.append(child)
				newLength = length + child.getNumber()
				nodePaths[child] = (child.getIndex(), newLength)

	substrings = []
	for key in nodePaths.keys(): 
		index = nodePaths[key][0]
		length = nodePaths[key][1]
		newStr = text[index+1-length:index+1]
		substrings.append(newStr)

	maxString = ''
	for string in substrings: 
		if len(string) > len(maxString):
			maxString = string

	return maxString
 

def main():
	with open('rosalind_ba9d (1).txt', 'r') as myfile:
		data = myfile.readlines()
	text = data[0].rstrip('\n')
	text += '$'

	trie = constructTrie(text)
	tree, root = constructTree(trie, text)
	pattern = findLongestRepeat(tree, text, root)

	print(pattern)


if __name__ == "__main__":
	main()
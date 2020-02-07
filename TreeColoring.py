class Node: 
	def __init__(self, children, symbol, parent, color):
		self.children = children 
		self.symbol = symbol 
		self.parent = parent
		self.color = color

	def addChildren(self, childToAdd): 
		self.children.append(childToAdd)

	def getChildren(self):
		return self.children 

	def getSymbol(self): 
		return self.symbol

	def getParent(self):
		return self.parent

	def setSymbol(self, text):
		self.symbol = text

	def setColor(self, color):
		self.color = color 

	def getColor(self):
		return self.color

	def setParent(self, parent):
		self.parent = parent

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

def treeColoring(tree):
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

def betterTreeColoring(node):
	if len(node.getChildren()) == 0:
		return node.getColor()
	initialColor = betterTreeColoring(node.getChildren()[0])
	isSame = True
	children = node.getChildren()
	for i in range(1, len(children)):
		if initialColor != betterTreeColoring(children[i]):
			isSame = False

	if not isSame:
		node.setColor('purple')
	else:
		node.setColor(initialColor)

	return node.getColor()

def main():
	with open('rosalind_ba9p.txt', 'r') as myfile:
		data = myfile.readlines()
	
	nodes = {} 
	i = 0
	text = data[i].rstrip('\n')
	while text != '-':
		separator = i 
		text = text.split()
		node = text[0]
		if text[2] != '{}':
			children = text[2]
			children = children.split(',')
			nodes.setdefault(node, [])
			for child in children: 
				nodes[node].append(child)
		else: 
			nodes[node] = []
		i += 1
		text = data[i].rstrip('\n')

	separator += 2
	#create the tree now 
	tree = [] 
	root = Node([], '0', None, 'gray')
	stack = [] 
	stack.append(root)
	while stack: 
		vertex = stack.pop() 
		for child in nodes[vertex.getSymbol()]: 
			newNode = Node([], child, vertex, 'gray')
			vertex.addChildren(newNode)
			stack.append(newNode)
		tree.append(vertex)

	#leaves colorization 
	for i in range(separator, len(data)):
		text = data[i].rstrip('\n')
		text = text.split()
		symbol = text[0][:-1]
		color = text[1]
		for node in tree: 
			if node.getSymbol() == symbol: 
				node.setColor(color)

	betterTreeColoring(tree[0])
	for node in tree: 
		print(str(node.getSymbol() + ": " + node.getColor()))

if __name__ == "__main__":
	main()
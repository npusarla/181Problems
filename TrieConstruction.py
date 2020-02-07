class Node: 
	def __init__(self, children, number, symbol, parent):
		self.children = children 
		self.number = number 
		self.symbol = symbol 
		self.parent = parent

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




def constructTrie(patterns):
	root = Node([], 0, '', None)
	Trie = [root] 
	number = 0
	for pattern in patterns: 
		currentNode = root 
		for i in range(len(pattern)):
			currentSymbol = pattern[i]
			isChild = False 
			for child in currentNode.getChildren(): 
				if child.getSymbol() == currentSymbol: 
					currentNode = child 
					isChild = True 
			
			if isChild == False: 
				number += 1
				newNode = Node([], number, currentSymbol, currentNode)
				Trie.append(newNode)
				currentNode.addChildren(newNode)
				currentNode = newNode

	TrieNodes = {}
	for node in Trie: 
		if node.symbol != '': 
			number = node.getNumber()
			symbol = node.getSymbol()
			parent = node.getParent()
			parentNumber = parent.getNumber() 
			TrieNodes[(parentNumber, number)] = symbol

	return TrieNodes

def main():
	with open('rosalind_ba9a.txt', 'r') as myfile:
		data = myfile.readlines()
	patterns = []
	for i in range(len(data)):
		text = data[i].rstrip('\n')
		patterns.append(text)

	trie = constructTrie(patterns)
	for pair in trie.keys(): 
		newStr = str(pair[0]) + "->" + str(pair[1]) + ":" + str(trie[pair])
		print(newStr)


if __name__ == "__main__":
	main()
class Node: 
	def __init__(self, children, number, symbol, parent, pattern):
		self.children = children 
		self.number = number 
		self.symbol = symbol 
		self.parent = parent
		self.pattern = pattern 

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

	def getPattern(self):
		return self.pattern



def constructTrie(patterns):
	root = Node([], 0, '', None, '')
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
			currentPattern = currentNode.getPattern() 
			if isChild == False: 
				number += 1
				newPattern = currentPattern + currentSymbol
				newNode = Node([], number, currentSymbol, currentNode, newPattern)
				Trie.append(newNode)
				currentNode.addChildren(newNode)
				currentNode = newNode

	return Trie

def prefixTrieMatching(text, trie):
	counter = 0
	symbol = text[counter]
	v = trie[0]
	while True: 
		if v.getChildren() == []: 
			return v.getPattern() 
		else:
			isChild = False 
			for child in v.getChildren(): 
				if child.getSymbol() == symbol: 
					counter += 1
					if counter < len(text):
						symbol = text[counter]
					v = child 
					isChild = True 
					break
			if isChild == False:
				return ''

def TrieMatching(text, trie):
	positions = [] 
	i = 0
	while len(text) > 0: 
		#path = prefixTrieMatching(text, trie)
		#print(path)
		if prefixTrieMatching(text, trie) != '':
			positions.append(i)
		i += 1
		text = text[1:]
	return positions 

def main():
	with open('rosalind_ba9b.txt', 'r') as myfile:
		data = myfile.readlines()
	
	text = data[0].rstrip('\n')
	patterns = []
	for i in range(1, len(data)):
		string = data[i].rstrip('\n')
		patterns.append(string)


	trie = constructTrie(patterns)
	positions = TrieMatching(text, trie)
	
	for pos in positions: 
		print(pos), 


if __name__ == "__main__":
	main()
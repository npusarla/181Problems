import random

def constructDeBruijn(kmers):
	myDict = {}
	for i in range(len(kmers)):
		kmer = kmers[i]
		node1 = kmer[:-1]
		node2 = kmer[1:]
		if node1 in myDict.keys():
			myDict[node1].append(node2)
		else:
			myDict.setdefault(node1, [])
			myDict[node1].append(node2)
		

	return myDict

def StringSpelledOutbyGenomePath(kmers):
	text = kmers[0]
	
	for i in range(1, len(kmers)):
		motif = kmers[i]
		text = text + motif[len(motif)-1]

	return text 

def EulerCycle(adjacencyMatrix):
	numNodes = len(adjacencyMatrix)
	numEdges = 0
	for theVals in adjacencyMatrix.values():
		for eachVal in theVals:
			numEdges += 1
	randInt = random.randint(1,numNodes-1)
	cycle = [] 
	listOfEdges = []
	keys = adjacencyMatrix.keys()
	startNode = keys[randInt]
	currNodes = adjacencyMatrix[startNode]
	randInt = random.randint(0, len(currNodes)-1)
	currNode = currNodes[randInt]
	cycle.append(startNode)
	listOfEdges.append((startNode, currNode))
	cycle.append(currNode)
	while currNode != startNode:
		if len(listOfEdges) == numEdges:
			break 
		nextNode = 0
		currNodes = adjacencyMatrix[currNode]
		if len(currNodes) > 1: 
			for num in currNodes: 
				pair = (currNode, num)
				if pair not in listOfEdges:
					nextNode = num 
		else:
			nextNode = currNodes[0]

		listOfEdges.append((currNode, nextNode))
		currNode = nextNode
		cycle.append(currNode)

	while len(listOfEdges) < numEdges:
		newNode = 0
		for node in cycle: 
			vals = adjacencyMatrix[node]
			for val in vals:
				if (node,val) not in listOfEdges: 
					newNode = node 

		#follow old cycle - follow the edge that's in list of edges 
		cycle = cycle[:-1]
		char = cycle[0]
		while char != newNode:
			cycle.remove(char)
			cycle.append(char)
			char = cycle[0]
		cycle.append(char)
		startNode = newNode
		currNodes = adjacencyMatrix[startNode]
		#finish traversing old cycle, randomly walk and make new cycle 
		for node in currNodes:
			if (startNode, node) not in listOfEdges:
				currNode = node 
		listOfEdges.append((startNode, currNode))	
		cycle.append(currNode)
		while currNode != startNode:
			if len(listOfEdges) == numEdges:
				break 
			nextNodes = adjacencyMatrix[currNode]
			nextNode = 0
			for node in nextNodes:
				pair = (currNode, node)
				if pair not in listOfEdges:
					nextNode = node 
			listOfEdges.append((currNode, nextNode))
			currNode = nextNode
			cycle.append(currNode)

	return cycle 

def constructUniversal(k):
	text = ''
	kmers = []
	for i in range(2**k):
		#add all possible kmers to a list and then use string reconstruction 
		kmer = format(i, "b")
		if len(kmer) < k:
			diff = k - len(kmer)
			kmer = ("0" * diff) + kmer 
		kmers.append(kmer)

	deBruijn = constructDeBruijn(kmers)
	
	cycle = EulerCycle(deBruijn)
	edges = []
	for i in range(len(cycle)-1):
		edge = cycle[i] + cycle[i+1][-1:]
		edges.append(edge)
	text = StringSpelledOutbyGenomePath(edges)
	text = text[:-(k-1)]
	return text 

def main():
	with open('rosalind_ba3i.txt', 'r') as myfile:
		data = myfile.readlines()
	k = int(data[0])

	text = constructUniversal(k)
	print(text)

if __name__ == "__main__":
	main()

import random

def EulerCycle(adjacencyMatrix):
	numNodes = len(adjacencyMatrix)
	numEdges = 0
	for theVals in adjacencyMatrix.values():
		for eachVal in theVals:
			numEdges += 1
	randInt = random.randint(1,numNodes-1)
	cycle = [] 
	listOfEdges = []
	startNode = randInt
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
				if val not in cycle: 
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

def EulerPath(adjacencyMatrix):
	#find the vertices with odd degree 
	outDegreeDict = {}
	inDegreeDict = {} 
	nodes = []
	#out degree first, in degree second 
	keys = adjacencyMatrix.keys()
	for i in range(len(keys)):
		key = keys[i]
		values = adjacencyMatrix[key]
		outDegreeDict[key] = len(values)
		nodes.append(key)
	for theVals in adjacencyMatrix.values():
		for eachVal in theVals:
			key = eachVal
			if key not in nodes:
				nodes.append(key)
			if key not in inDegreeDict.keys(): 
				inDegreeDict[key] = 1
			else:
				inDegreeDict[key] = inDegreeDict[key] + 1
	
	#check to find the two unbalanced nodes 
	unbalancedNodes = [] 
	for i in range(len(nodes)):
		inDegree = 0
		outDegree = 0
		if nodes[i] in inDegreeDict.keys():
			inDegree = inDegreeDict[nodes[i]]
		if nodes[i] in outDegreeDict.keys():
			outDegree = outDegreeDict[nodes[i]]
		if inDegree == 0:
			inDegreeDict[nodes[i]] = 0
		if outDegree == 0:
			outDegreeDict[nodes[i]] = 0
			adjacencyMatrix[nodes[i]] = []
		if outDegree != inDegree:
			unbalancedNodes.append(nodes[i])

	node1 = unbalancedNodes[0]
	node2 = unbalancedNodes[1]
	startNode = 0
	endNode = 0
	if inDegreeDict[node1] > outDegreeDict[node1]:
		adjacencyMatrix[node1].append(node2)
		startNode = node1 
		endNode = node2
	else: 
		adjacencyMatrix[node2].append(node1)
		startNode = node2
		endNode = node1


	cycle = EulerCycle(adjacencyMatrix)
	#remove an edge and traverse cycle to find a path 
	path = [] 
	index = 0
	for i in range(len(cycle)-1): 
		if cycle[i] == startNode and cycle[i+1] == endNode:
			index = i+1
	#start traversing cycle from this index
	for i in range(index, len(cycle)-1):
		path.append(cycle[i])
	for i in range(index):
		path.append(cycle[i])

	return path 

def main():
	with open('rosalind_ba3g.txt', 'r') as myfile:
		data = myfile.readlines()
	adjacencyMatrix = {}
	keys = adjacencyMatrix.keys()
	for i in range(len(data)):
		edge = data[i].rstrip('\n')
		numbers = edge.split() 
		key = int(numbers[0])
		values = numbers[2].split(",")
		adjacencyMatrix.setdefault(key, [])
		for m in range(len(values)):
			adjacencyMatrix[key].append(int(values[m]))


	path = EulerPath(adjacencyMatrix)
	strPath = str(path[0])
	for i in range(1, len(path)):
		strPath += "->" + str(path[i])

	print(strPath)
	
 
if __name__ == "__main__":
	main()


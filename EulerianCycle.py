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


def main():
	with open('rosalind_ba3f (1).txt', 'r') as myfile:
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


	cycle = EulerCycle(adjacencyMatrix)
	cyclePath = str(cycle[0])
	for i in range(1, len(cycle)):
		cyclePath += "->" + str(cycle[i])
	print(cyclePath)
	
 
if __name__ == "__main__":
	main()



import copy 

def maximalNonBranchingPaths(deBruijnGraph):
	#findDegrees
	outDegreeDict = {}
	inDegreeDict = {} 
	nodes = []
	keys = deBruijnGraph.keys()
	for i in range(len(keys)):
		key = keys[i]
		values = deBruijnGraph[key]
		outDegreeDict[key] = len(values)
		nodes.append(key)
	for theVals in deBruijnGraph.values():
		for eachVal in theVals:
			key = eachVal
			if key not in nodes:
				nodes.append(key)
			if key not in inDegreeDict.keys(): 
				inDegreeDict[key] = 1
			else:
				inDegreeDict[key] = inDegreeDict[key] + 1

	for i in range(len(nodes)):
		inDegree = 0
		outDegree = 0
		if nodes[i] not in inDegreeDict.keys():
			inDegreeDict[nodes[i]] = 0
		if nodes[i] not in outDegreeDict.keys():
			outDegreeDict[nodes[i]] = 0
			deBruijnGraph[nodes[i]] = []

	contigs = [] 
	copyDict = copy.deepcopy(deBruijnGraph)

	for node in nodes:
		if inDegreeDict[node] != 1 or outDegreeDict[node] != 1: 
			#check if there out outdegrees 
			if outDegreeDict[node] > 0:
				for m in range(outDegreeDict[node]):
					path = []
					path.append(node)
					nextNode = deBruijnGraph[node][m]
					index = copyDict[node].index(nextNode)
					del copyDict[node][index]
					while inDegreeDict[nextNode] == 1 and outDegreeDict[nextNode] == 1:
						path.append(nextNode)
						del copyDict[nextNode][0]
						nextNode = deBruijnGraph[nextNode][0]

					path.append(nextNode)
					#until it hits a node with multiple degrees 

					contigs.append(path)

	#find isolated cycles
	for node in deBruijnGraph:
		if copyDict[node] != []:
			cycle = [] 
			nextNode = node
			cycle.append(nextNode)
			while copyDict[nextNode] != node:
				cycle.append(copyDict[nextNode][0])
				a = copyDict[nextNode][0]
				nextNode = copyDict[nextNode][0]
				if a == node:
					break 

			for m in range(len(cycle)-1):
				del copyDict[cycle[m]][0]
			contigs.append(cycle)

	return contigs

def main():
	with open('rosalind_ba3m.txt', 'r') as myfile:
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

	contigs = maximalNonBranchingPaths(adjacencyMatrix)
	for i in range(len(contigs)):
		path = str(contigs[i][0])
		for l in range(1, len(contigs[i])):
			path += " -> " + str(contigs[i][l])
		print(path)
	
 
if __name__ == "__main__":
	main()
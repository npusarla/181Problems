import random 
import copy 

def TopologicalOrdering(adjacencyMatrix, nodes, source, sink):
	orderedList = []
	candidates = []
	values = [] 
	copyDict = copy.deepcopy(adjacencyMatrix)
	listOfEdges = []
	for vals in adjacencyMatrix.values():
		for eachVal in vals:
			values.append(eachVal)
	for node in nodes:
		if node not in values:
			candidates.append(node)

	
	while len(candidates) > 0:
		node = candidates[random.randint(0, len(candidates)-1)]
		orderedList.append(node)
		candidates.remove(node)
		if node in adjacencyMatrix.keys():
			
			outgoingEdges = adjacencyMatrix[node]
			for outgoingEdge in outgoingEdges:
				
				edge = (node, outgoingEdge)
				if edge not in listOfEdges:
					listOfEdges.append(edge)
					index = copyDict[node].index(outgoingEdge)
					del copyDict[node][index]
					
					valuesOfNewGraph = []
					for theVals in copyDict.values():
						for eachVal in theVals:
							valuesOfNewGraph.append(eachVal)

					
					if outgoingEdge not in valuesOfNewGraph:
						candidates.append(outgoingEdge)

					
	return orderedList

def predecessors(node, adjacencyMatrix):
	predecessors = []
	for key in adjacencyMatrix.keys():
		values = adjacencyMatrix[key]
		for eachVal in values:
			if node == eachVal:
				predecessors.append(key)

	return predecessors

def longestPathinaDAG(source, sink, adjacencyMatrix, weightMatrix):
	nodes = [] 
	longestPath = {}
	for node in adjacencyMatrix.keys():
		if node not in nodes:
			nodes.append(node)
	for vals in adjacencyMatrix.values():
		for eachVal in vals:
			if eachVal not in nodes:
				nodes.append(eachVal)

	path = {}
	for node in nodes:
		path[node] = -len(adjacencyMatrix)
		longestPath[node] = ''

	path[source] = 0
	longestPath[source] = str(source)
	topOrderedGraph = TopologicalOrdering(adjacencyMatrix, nodes, source, sink)
	index = topOrderedGraph.index(source)
	
	for i in range(index+1, len(topOrderedGraph)):
		node = topOrderedGraph[i]
		predecess = predecessors(node, adjacencyMatrix)
		if len(predecess) != 0:
			options = []
			paths = []
			for predecessor in predecess:
				if predecessor in topOrderedGraph:
					index = adjacencyMatrix[predecessor].index(node)
					options.append(path[predecessor] + weightMatrix[predecessor][index])
					paths.append(longestPath[predecessor] + " " + str(node))

			path[node] = max(options)
			newIndex = options.index(max(options))
			longestPath[node] = paths[newIndex]


	return path[sink], longestPath[sink]


def main():
	with open('rosalind_ba5d.txt', 'r') as myfile:
		data = myfile.readlines()
	source = int(data[0])
	sink = int(data[1])
	adjacencyMatrix = {}
	weightMatrix = {}
	for i in range(2, len(data)):
		text = data[i].rstrip('\n')
		text = text.split("->")
		node = int(text[0])
		end = text[1].split(":")
		node2 = int(end[0])
		weight = int(end[1])
		if node not in adjacencyMatrix.keys():
			adjacencyMatrix.setdefault(node, [])
			weightMatrix.setdefault(node, [])
		adjacencyMatrix[node].append(node2)
		weightMatrix[node].append(weight) 
		
	longestPathLength, longestPath = longestPathinaDAG(source, sink, 
								adjacencyMatrix, weightMatrix)
	print(longestPathLength)
	longestPath = longestPath.split()
	text = str(longestPath[0])
	for i in range(1, len(longestPath)):
		text += "->" + longestPath[i]
	print(text)

 
if __name__ == "__main__":
	main()
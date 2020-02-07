import copy
import random

def TopologicalOrdering(adjacencyMatrix):
	orderedList = []
	candidates = []
	values = [] 
	nodes = [] 
	for node in adjacencyMatrix.keys():
		if node not in nodes:
			nodes.append(node)
	for vals in adjacencyMatrix.values():
		for eachVal in vals:
			if eachVal not in nodes:
				nodes.append(eachVal)

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

def main():
	with open('rosalind_ba5n.txt', 'r') as myfile:
		data = myfile.readlines()
	adjacencyMatrix = {}
	for i in range(len(data)):
		text = data[i].rstrip('\n')
		text = text.split("->")
		node = int(text[0])
		end = text[1].split(',')
		if node not in adjacencyMatrix.keys():
			adjacencyMatrix.setdefault(node, [])
		for node2 in end: 
			adjacencyMatrix[node].append(int(node2))
		
	topOrder = TopologicalOrdering(adjacencyMatrix)
	text = str(topOrder[0])
	for i in range(1, len(topOrder)):
		text += ", " + str(topOrder[i])
	print(text)

 
if __name__ == "__main__":
	main()
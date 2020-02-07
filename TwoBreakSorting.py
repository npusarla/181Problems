def chromosomeToCycle(chromosome):
	nodes = [0] * 2*len(chromosome)
	for j in range(len(chromosome)):
		i = chromosome[j]
		if i > 0: 
			nodes[(2*j)-1] = (2*i) - 1
			nodes[2*j] = 2*i
		else: 
			nodes[(2*j)-1] = -2*i
			nodes[2*j] = -(2*i) - 1

	nodes = [nodes[-1]] + nodes[:-1]
	
	return nodes 

def coloredEdges(genome):
	edges = [] 
	for chromosome in genome: 
		nodes = chromosomeToCycle(chromosome)
		nodes.append(nodes[0])
		for j in range(len(chromosome)):
			edge = (nodes[2*j+1], nodes[(2*j)+2])
			edges.append(edge)

	return edges

def findCycles(coloredEdges1, coloredEdges2):
	nodes = [] 
	for i in range(len(coloredEdges1)):
		nodes.append(coloredEdges1[i][0])
		nodes.append(coloredEdges1[i][1])
	for i in range(len(coloredEdges2)):
		nodes.append(coloredEdges2[i][0])
		nodes.append(coloredEdges2[i][1])
		
	nodes = list(set(nodes))
	cycles = []
	cycleNum = -1
	coloredEdges = coloredEdges1 + coloredEdges2
	#initialize cycles array
	for i in range(len(nodes)):
		cycles.append(i)
	for  i in range(len(coloredEdges)):
		#print(coloredEdges)
		num1 = coloredEdges[i][0]
		num2 = coloredEdges[i][1]
		#print(len(cycles))
		#print(num1)
		#print(num2)
		if cycles[num1-1] > cycles[num2-1]:
			oldNum = cycles[num1-1]
			cycles[num1-1] = cycles[num2-1]
			cycleNum = cycles[num2-1]

		else: 
			oldNum = cycles[num2-1]
			cycles[num2-1] = cycles[num1-1]
			cycleNum = cycles[num1-1]
		for m in range(len(cycles)):
			if cycles[m] == oldNum: 
				cycles[m] = cycleNum

	cycleNumbers = {}
	for i in range(len(cycles)):
		key = cycles[i]
		if cycles[i] not in cycleNumbers.keys():
			cycleNumbers.setdefault(key, [])
			cycleNumbers[key].append(i+1)
		else: 
			cycleNumbers[key].append(i+1)

	finalCycles = []
	for key in cycleNumbers.keys(): 
		indvCycle = []
		for i in range(len(cycleNumbers[key])):
			indvCycle.append(cycleNumbers[key][i])
		finalCycles.append(indvCycle)

	#print(finalCycles)
	return finalCycles
	

def twoBreakGraph(genomeGraph, i1, i2, j1, j2):
	#print('BEFORE GENOME GRAPH: ', genomeGraph)
	#print(i1, i2, j1, j2)
	for i in range(len(genomeGraph)):
		if genomeGraph[i] == (i1, i2) or genomeGraph[i] == (i2, i1):
			elem = genomeGraph[i]
			genomeGraph.remove(elem)
			#print(elem )
			genomeGraph.append((i1, j1))
			#print((i1, j1))
	for i in range(len(genomeGraph)):
		if genomeGraph[i] == (j1, j2) or genomeGraph[i] == (j2, j1):
			elem2 = genomeGraph[i] 
			genomeGraph.remove(elem2)
			#print(elem2)
			genomeGraph.append((i2, j2))
			#print((i2, j2))

	#print('AFTER GENOME GRAPH: ', genomeGraph)

	return genomeGraph

def cycleToChromosome(nodes):
	chromosome = [0] *(len(nodes)/2)
	for i in range(1, (len(nodes)/2)+1):
		if nodes[(2*i)-1-1] < nodes[(2*i)-1]:
			chromosome[i-1] = nodes[(2*i)-1]/2
		else:
			chromosome[i-1] = -nodes[(2*i)-2]/2

	return chromosome


def graphToGenome(genomeGraph):

	chromosomes = [] 
	copyGenomeGraph = genomeGraph[:]
	cycles = []
	#create cycles 
	nodes = [] 
	for i in range(len(genomeGraph)):
		nodes.append(genomeGraph[i][0])
		nodes.append(genomeGraph[i][1])
	nodes = list(set(nodes))
	while(len(copyGenomeGraph) > 0):
		cycle = []
		startElem = copyGenomeGraph[0]
		cycle.append(startElem[1])
		startElem = copyGenomeGraph[0]
		elem = (0,0)
		#print('startElem: ', startElem)
		secondValue = startElem[1]
		while elem != startElem: 
			if secondValue%2 == 0: 
				firstVal = secondValue - 1
			else: 
				firstVal = secondValue + 1
				#now find edge starting with first value 
			for i in range(len(copyGenomeGraph)):
				edge = copyGenomeGraph[i]
				if edge[0] == firstVal or edge[1] == firstVal: 
					elem = edge
					if edge[0] == firstVal: 
						cycle.append(edge[0])
						cycle.append(edge[1])
						secondValue = elem[1]
					elif edge[1] == firstVal: 
						cycle.append(edge[1])
						cycle.append(edge[0])
						secondValue = elem[0]
					break 
		
			copyGenomeGraph.remove(elem)

		#remove last element of cycle if its more than two elements
		#if len(cycle) > 2: 
		cycle = cycle[:-1]
		cycles.append(cycle)


	for eachCycle in cycles:
		nodes = eachCycle
		chromosome = cycleToChromosome(nodes)
		chromosomes.append(chromosome)

	return chromosomes

def TwoBreakGenome(genome, i1, i2, j1, j2):
	genomeGraph = coloredEdges(genome)
	genomeGraph = twoBreakGraph(genomeGraph, i1, i2, j1, j2)
	#print('TWO BREAK GRAPH: ', genomeGraph)
	chromosome = graphToGenome(genomeGraph)

	return chromosome

def twoBreakSorting(chromosome1, chromosome2):
	rearrangements = []
	rearrangements.append(chromosome1)
	redEdges = coloredEdges(chromosome1)
	blueEdges = coloredEdges(chromosome2)
	breakpointGraph = redEdges + blueEdges
	cycles = findCycles(redEdges, blueEdges)
	count = 0
	for cycle in cycles: 
		if len(cycle) == 2:
			count += 1

	while count != len(cycles): 
		nontrivialCycle = []
		for cycle in cycles: 
			if len(cycle) > 2:
				nontrivialCycle = cycle
				break 

		#print(nontrivialCycle)
		for i in range(len(nontrivialCycle)):
			nodesOfBlueEdges = [] 
			for edge in blueEdges:	
				nodesOfBlueEdges.append(edge[0])
				nodesOfBlueEdges.append(edge[1])

			arbBlueEdge = (0,0)
			nodesOfBlueEdges = list(set(nodesOfBlueEdges))
			if nontrivialCycle[i] in nodesOfBlueEdges: 
				#find the blue edge with that node 
				for edge in blueEdges: 
					if edge[0] == nontrivialCycle[i] or edge[1] == nontrivialCycle[i]: 
						arbBlueEdge = edge 
						break 

			if arbBlueEdge != (0,0):
				break 

		#now find the corresponding red edges 
		i2 = arbBlueEdge[0]
		i3 = arbBlueEdge[1]

		for edge in redEdges:
			if edge[0] == i2 and edge[1] != i3:
				i1 = edge[1]
			elif edge[1] == i2 and edge[0] != i3: 
				i1 = edge[0]
			if edge[0] == i3 and edge[1] != i2: 
				i4 = edge[1]
			elif edge[1] == i3 and edge[0] != i2: 
				i4 = edge[0]		

		#print(i1, i2, i3, i4)
		for i in range(len(redEdges)):
			if redEdges[i] == (i1, i2) or redEdges[i] == (i2, i1):
				elem = redEdges[i]
				redEdges.remove(elem)
				redEdges.append((i1, i4))

			if redEdges[i] == (i3, i4) or redEdges[i] == (i4, i3):
				elem1 = redEdges[i]
				redEdges.remove(elem1)
				redEdges.append((i2, i3))


		breakpointGraph = redEdges + blueEdges
		cycles = findCycles(redEdges, blueEdges)

		count = 0
		for cycle in cycles: 
			if len(cycle) == 2:
				count += 1

		chromosome1 = TwoBreakGenome(chromosome1, i1, i2, i4, i3)
		rearrangements.append(chromosome1)


	#print(rearrangements)
	return rearrangements


def main():
	with open('rosalind_ba6d.txt', 'r') as myfile:
		data = myfile.readlines()
	permutation = data[0].rstrip('\n')
	permutation = permutation.split()
	newPermutation = []
	for i in range(len(permutation)):
		if i == 0: 
			a = permutation[0]
			newNum = int(a[1:])
			newPermutation.append(newNum)
		if i == len(permutation)-1:
			a = permutation[len(permutation)-1].rstrip(')')
			newPermutation.append(int(a))
		if i != 0 and i != len(permutation)-1:
			newPermutation.append(int(permutation[i]))

	newPermutation = list([newPermutation])

	permutation1 = data[1].rstrip('\n')
	permutation1 = permutation1.split() 
	newPermutation1 = []
	for i in range(len(permutation1)):
		if i == 0: 
			a = permutation1[0]
			newNum = int(a[1:])
			newPermutation1.append(newNum)
		if i == len(permutation1)-1:
			a = permutation1[len(permutation1)-1].rstrip(')')
			newPermutation1.append(int(a))
		if i != 0 and i != len(permutation1)-1:
			newPermutation1.append(int(permutation1[i]))

	newPermutation1 = list([newPermutation1])
	
	rearrangements = twoBreakSorting(newPermutation, newPermutation1)
	for i in range(len(rearrangements)):
		newStr = ''
		for j in range(len(rearrangements[i])):
			genome = rearrangements[i]
			for k in range(len(genome[j])):
				gene = genome[j]
				if k == 0: 
					newStr += '(' 
					if gene[k] > 0: 
						newStr += '+' + str(gene[k])
					else: 
						newStr += str(gene[k])
				else: 
					if gene[k] > 0: 
						newStr += ' ' + '+' + str(gene[k])
					else: 
						newStr += ' ' + str(gene[k])
	    
			newStr += ')'
		
		print(newStr)
	


if __name__ == "__main__":
	main()

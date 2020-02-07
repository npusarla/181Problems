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

def twoBreakGraph(genomeGraph, i1, i2, j1, j2):
	for i in range(len(genomeGraph)):
		if genomeGraph[i] == (i1, i2) or genomeGraph[i] == (i2, i1):
			elem = genomeGraph[i]
			genomeGraph.remove(elem)
			genomeGraph.append((i1, j1))
		if genomeGraph[i] == (j1, j2) or genomeGraph[i] == (j2, j1):
			elem2 = genomeGraph[i] 
			genomeGraph.remove(elem2)
			genomeGraph.append((i2, j2))


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
	while(len(copyGenomeGraph) > 0):
		cycle = []
		startElem = copyGenomeGraph[0]
		cycle.append(startElem[1])
		startElem = copyGenomeGraph[0]
		elem = (0,0)
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

		#remove last two elements of the cycle
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
	chromosome = graphToGenome(genomeGraph)

	return chromosome

def main():
	with open('rosalind_ba6k.txt', 'r') as myfile:
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

	indices = data[1].rstrip('\n')
	indices = indices.split(',')
	i1 = int(indices[0])
	i2 = int(indices[1])
	j1 = int(indices[2])
	j2 = int(indices[3])
	
	chromosome = TwoBreakGenome(newPermutation, i1, i2, j1, j2)
	newStr = ''
	for i in range(len(chromosome)):
		if i != 0: 
			newStr += ' '
		for k in range(len(chromosome[i])):
			gene = chromosome[i]
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
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

def main():
	with open('sampleData', 'r') as myfile:
		data = myfile.readlines()
	nodes = data[0].rstrip('\n')
	nodes = nodes.split('(')
	genomeGraph = []
	for i in range(1, len(nodes)):
		pair = nodes[i].split(', ')
		num1 = int(pair[0])
		num2 = int(pair[1][:-1])
		genomeGraph.append((num1, num2))

	chromosomes = graphToGenome(genomeGraph)
	newStr = ''
	for i in range(len(chromosomes)):
		newStr += '('
		for j in range(len(chromosomes[i])):
			if j == 0: 
				if chromosomes[i][j] > 0: 
					newStr += '+' + str(chromosomes[i][j])
				else: 
					newStr += str(chromosomes[i][j])
			else: 
				if chromosomes[i][j] > 0: 
					newStr += ' ' + '+' + str(chromosomes[i][j])
				else: 
					newStr += ' ' + str(chromosomes[i][j])

		newStr += ')'

	print(newStr)

if __name__ == "__main__":
	main()

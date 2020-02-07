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

def twoBreak(genomeGraph1, genomeGraph2):
	blockNum = 0
	for i in range(len(genomeGraph1)):
		chrom = genomeGraph1[i]
		for j in range(len(chrom)):
			blockNum += 1
	
	coloredEdges1 = coloredEdges(genomeGraph1)
	coloredEdges2 = coloredEdges(genomeGraph2) 
	nodes = [] 
	for i in range(len(coloredEdges1)):
		nodes.append(coloredEdges1[i][0])
		nodes.append(coloredEdges1[i][1])
		
	nodes = list(set(nodes))
	cycles = []
	cycleNum = -1
	#initialize cycles array
	for i in range(len(nodes)):
		cycles.append(i)
	for  i in range(len(coloredEdges1)):
		num1 = coloredEdges1[i][0]
		num2 = coloredEdges1[i][1]
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
	for  i in range(len(coloredEdges2)):
		num1 = coloredEdges2[i][0]
		num2 = coloredEdges2[i][1]
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

	cycles = list(set(cycles))
	return blockNum - len(cycles)

def main():
	with open('rosalind_ba6c.txt', 'r') as myfile:
		data = myfile.readlines()
	permutation1 = data[0].rstrip('\n')
	permutation1 = permutation1.split(')')
	permutation2 = data[1].rstrip('\n')
	permutation2 = permutation2.split(')')
	permutations = [permutation1, permutation2]
	chromosomes1 = [] 
	chromosomes2 = []
	for k in range(len(permutations)):
		permutation = permutations[k]
		for i in range(len(permutation)-1):
			chromosome = permutation[i].split()
			chrom1 = []
			for j in range(len(chromosome)):
				if j == 0: 
					a = chromosome[0]
					newNum = int(a[1:])
					chrom1.append(newNum)
				else:
					chrom1.append(int(chromosome[j]))

	
			if k == 0: 
				chromosomes1.append(chrom1)
			else: 
				chromosomes2.append(chrom1)
			

	twoBreakDist = twoBreak(chromosomes1, chromosomes2)
	print(twoBreakDist)
	#newStr = str(edges[0])
	#for i in range(1, len(edges)):
#		newStr += ', ' + str(edges[i])

	#print(newStr)

if __name__ == "__main__":
	main()
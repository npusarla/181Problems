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

def main():
	with open('rosalind_ba6h.txt', 'r') as myfile:
		data = myfile.readlines()
	permutation = data[0].rstrip('\n')
	permutation = permutation.split(')')
	chromosomes = [] 
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

		chromosomes.append(chrom1)

	edges = coloredEdges(chromosomes)
	newStr = str(edges[0])
	for i in range(1, len(edges)):
		newStr += ', ' + str(edges[i])

	print(newStr)

if __name__ == "__main__":
	main()

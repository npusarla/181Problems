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

def main():
	with open('rosalind_ba6j.txt', 'r') as myfile:
		data = myfile.readlines()
	nodes = data[0].rstrip('\n')
	nodes = nodes.split('(')
	genomeGraph = []
	for i in range(1, len(nodes)):
		pair = nodes[i].split(', ')
		num1 = int(pair[0])
		num2 = int(pair[1][:-1])
		genomeGraph.append((num1, num2))

	indices = data[1].rstrip('\n')
	indices = indices.split(',')
	i1 = int(indices[0])
	i2 = int(indices[1])
	j1 = int(indices[2])
	j2 = int(indices[3])

	newGraph = twoBreakGraph(genomeGraph, i1, i2, j1, j2)
	newStr = str(newGraph[0])
	for i in range(1, len(newGraph)):
		newStr += ', ' + str(newGraph[i])

	print(newStr)

if __name__ == "__main__":
	main()

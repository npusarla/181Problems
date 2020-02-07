def prefix(kmer):
	return kmer[:-1]

def suffix(kmer):
	return kmer[1:]

def constructDeBruijn(kmers):
	myDict = {}
	for i in range(len(kmers)):
		kmer = kmers[i]
		node1 = prefix(kmer)
		node2 = suffix(kmer)
		if node1 in myDict.keys():
			myDict[node1].append(node2)
		else:
			myDict.setdefault(node1, [])
			myDict[node1].append(node2)
		
	return myDict

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
	for node in nodes:
		if inDegreeDict[node] != 1 or outDegreeDict[node] != 1: 
			#check if there out outdegrees 
			if outDegreeDict[node] > 0:
				for m in range(outDegreeDict[node]):
					path = []
					path.append(node)
					nextNode = deBruijnGraph[node][m]
					while inDegreeDict[nextNode] == 1 and outDegreeDict[nextNode] == 1:
						path.append(nextNode)
						nextNode = deBruijnGraph[nextNode][0]
					path.append(nextNode)
					#until it hits a node with multiple degrees 

					contigs.append(path)

	return contigs

def generateContigs(kmers):
	deBruijn = constructDeBruijn(kmers)
	contigs = maximalNonBranchingPaths(deBruijn)
	texts = []
	for i in range(len(contigs)):
		path = contigs[i]
		text = path[0]
		for l in range(1, len(path)):
			text += path[l][-1:]
		texts.append(text)

	return texts 

def main():
	with open('rosalind_ba3k.txt', 'r') as myfile:
		data = myfile.readlines()
	kmers = [] 
	for i in range(len(data)):
		kmer = data[i].rstrip('\n')
		kmers.append(kmer)

	contigs = generateContigs(kmers)
	for contig in contigs:
		print(contig),
	#print(text)

if __name__ == "__main__":
	main()

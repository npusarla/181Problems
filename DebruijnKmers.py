def constructDeBruijn(kmers):
	myDict = {}
	for i in range(len(kmers)):
		kmer = kmers[i]
		node1 = kmer[:-1]
		node2 = kmer[1:]
		if node1 in myDict.keys():
			myDict[node1].append(node2)
		else:
			myDict.setdefault(node1, [])
			myDict[node1].append(node2)
		

	return myDict

def main():
	with open('rosalind_ba3e.txt', 'r') as myfile:
		data = myfile.readlines()
	kmers = [] 
	for i in range(len(data)):
		kmers.append(data[i].rstrip('\n'))

	pairs = constructDeBruijn(kmers)
	keyPairs = pairs.keys()
	keyPairs.sort()

	for key in keyPairs:
		text = key + " -> " 
		if len(pairs[key]) > 1:
			for i in range(len(pairs[key])):
				if i == len(pairs[key])-1:
					text += pairs[key][i] 
				else:
					text += pairs[key][i] + ","
		else:
			text += pairs[key][0]

		print(text) 
 
if __name__ == "__main__":
	main()
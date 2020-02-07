def getKmers(k, text):
	kmers = [] 
	for i in range(len(text)-k+1):
		kmers.append(text[i:i+k])

	kmers.sort()
	return kmers 

def constructGraph(kmers):
	pairs = [] 
	for i in range(len(kmers)):
		for j in range(len(kmers)):
			kmer1 = kmers[i]
			kmer2 = kmers[j]
			if(kmer1[1:] == kmer2[:-1]):
				pairs.append((kmer1, kmer2))

	return pairs 

def constructDeBruijn(k, text):
	kmers = getKmers(k, text)
	
	myDict = {}
	for i in range(len(text)-k+1):
		kmer = text[i:i+k]
		node1 = kmer[:-1]
		node2 = kmer[1:]
		if node1 in myDict.keys():
			myDict[node1].append(node2)
		else:
			myDict.setdefault(node1, [])
			myDict[node1].append(node2)
		

	return myDict

def main():
	with open('rosalind_ba3d.txt', 'r') as myfile:
		data = myfile.readlines()
	k = int(data[0])
	text = data[1]
	text = text.rstrip('\n')

	pairs = constructDeBruijn(k, text)
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
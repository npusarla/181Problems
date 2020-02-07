def constructGraph(kmers):
	pairs = [] 
	for i in range(len(kmers)):
		for j in range(len(kmers)):
			kmer1 = kmers[i]
			kmer2 = kmers[j]
			if(kmer1[1:] == kmer2[:-1]):
				pairs.append((kmer1, kmer2))

	return pairs 

def main():
	with open('rosalind_ba3c.txt', 'r') as myfile:
		data = myfile.readlines()
	kmers = []
	for i in range(len(data)):
		kmers.append(data[i].rstrip('\n'))

	pairs = constructGraph(kmers)
	pairs.sort()

	for i in range(len(pairs)):
		text = pairs[i][0] + " -> " + pairs[i][1]
		print(text) 
 
if __name__ == "__main__":
	main()
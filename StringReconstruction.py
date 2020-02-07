def prefix(kmer):
	return kmer[:-1]

def suffix(kmer):
	return kmer[1:]

def constructString(kmers, k):
	text = ''
	currKmer = ''
	listOfSuffixes = []
	for kmer in kmers:
		listOfSuffixes.append(suffix(kmer))
	for kmer in kmers:
		if prefix(kmer) not in listOfSuffixes:
			text = kmer 
			currKmer = kmer 
	kmers.remove(currKmer)
	while len(kmers) > 0: 
		if len(kmers) == 1:
			kmer = kmers[0]
			text += kmer[-1:]
			kmers.remove(kmer)
		else:
			for kmer in kmers:
				if suffix(currKmer) == prefix(kmer):
					text += kmer[-1:]
					currKmer = kmer 
					kmers.remove(kmer)
					break
	return text 

def main():
	with open('rosalind_ba3h.txt', 'r') as myfile:
		data = myfile.readlines()
	k = int(data[0])
	kmers = [] 
	for i in range(1, len(data)):
		kmers.append(data[i].rstrip('\n'))

	text = constructString(kmers, k)
	print(text)

if __name__ == "__main__":
	main()

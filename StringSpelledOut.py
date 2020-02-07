def StringSpelledOutbyGenomePath(kmers):
	text = kmers[0]
	
	for i in range(1, len(kmers)):
		motif = kmers[i]
		text = text + motif[len(motif)-1]

	return text 

def main():
	with open('rosalind_ba3b.txt', 'r') as myfile:
		data = myfile.readlines()
	kmers = [] 
	for i in range(len(data)):
		kmer = data[i]
		kmer = kmer.rstrip('\n')
		kmers.append(kmer)
		
	text = StringSpelledOutbyGenomePath(kmers)

	print(text)
 
if __name__ == "__main__":
	main()
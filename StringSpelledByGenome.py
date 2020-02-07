def StringSpelledOutbyPairs(kmers, k, d):
	text = kmers[0].split("|")
	text1 = text[0]
	text2 = text[1]
	
	for i in range(1, len(kmers)):
		motif = kmers[i].split("|")
		text1 = text1 + motif[0][len(motif[0])-1]
		text2 = text2 + motif[1][len(motif[1])-1]

	text = text1[0:k+d] + text2
	return text 

def main():
	with open('rosalind_ba3l.txt', 'r') as myfile:
		data = myfile.readlines()
	numbers = data[0].split()
	k = int(numbers[0])
	d = int(numbers[1])
	kmers = [] 
	for i in range(1, len(data)):
		kmer = data[i].rstrip('\n')
		kmers.append(kmer)

	text = StringSpelledOutbyPairs(kmers, k, d)
	print(text)

if __name__ == "__main__":
	main()

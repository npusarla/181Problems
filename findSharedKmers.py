def ReverseSymbol(symbol): 
	if symbol == 'A': 
		return 'T'
	if symbol == 'C': 
		return 'G'
	if symbol == 'G':
		return 'C'
	if symbol == 'T':
		return 'A'

def ReverseComplement(pattern):
	patternComp = '' 
	for symbol in pattern: 
		patternComp = patternComp + ReverseSymbol(symbol) 

	return patternComp 

def SymbolToNumber(symbol): 
	if symbol == 'A':
		return 0
	if symbol == 'C':
		return 1 
	if symbol == 'G':
		return 2
	if symbol == 'T':
		return 3

def PatternToNumber(pattern): 
	if len(pattern) == 0: 
		return 0 
	symbol = pattern[len(pattern)-1] 
	prefix = pattern[:-1]
	return (4*PatternToNumber(prefix)) + SymbolToNumber(symbol) 

def firstKmerIndex(kmer, v):
	positions = []
	for i in range(len(v)-len(kmer)+1):
		newkmer = v[i:i+len(kmer)]
		if newkmer == kmer: 
			positions.append(i)

	return positions 


def findKmers(k, v, w):
	sharedKmers = []
	freqArray = [0] * 4**k
	for i in range(len(v)-k+1):
		kmer = v[i:i+k]
		num = PatternToNumber(kmer)
		freqArray[num] = freqArray[num] + 1
		
	for i in range(len(w)-k+1):
		kmer = w[i:i+k]
		revKmer = ReverseComplement(kmer)
		revNum = PatternToNumber(revKmer)
		num = PatternToNumber(kmer)
		if freqArray[num] > 0: 
			positions = firstKmerIndex(kmer, v)
			for pos in positions: 
				sharedKmers.append((pos, i))
		if freqArray[revNum] > 0: 
			positions = firstKmerIndex(revKmer, v)
			for pos in positions:
				sharedKmers.append((pos, i))

	#sharedKmers.sort()
	return sharedKmers

def main():
	with open('rosalind_ba6e.txt', 'r') as myfile:
		data = myfile.readlines()
	k = int(data[0])
	v = data[1].rstrip('\n')
	w = data[2].rstrip('\n')

	#print(v)
	#print(w)
	sharedKmers = findKmers(k, v, w)
	for pair in sharedKmers:
		print(pair)
 
if __name__ == "__main__":
	main()
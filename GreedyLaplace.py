def profileMostProbable(text, k, matrix):
	probKmer = text[0:k]
	highestProb = 0
	for i in range(len(text)-k+1):
		kmer = text[i:i+k]
		probability = 1
		for a in range(len(kmer)):
			symbol = kmer[a] 
			j = 0
			if symbol == 'A':
				j = 0 
			if symbol == 'C':
				j = 1
			if symbol == 'G':
				j = 2
			if symbol == 'T':
				j = 3
			
			probability = probability * matrix[j][a]
		if probability > highestProb:
			highestProb = probability
			probKmer = kmer 

	return probKmer

def SymbolToNumber(symbol):
	if symbol == 'A':
		return 0
	if symbol == 'C':
		return 1
	if symbol == 'G':
		return 2
	if symbol == 'T':
		return 3

def formProfile(motifmatrix, k, t):
	countMatrix = [[0] * k for a in range(4)]
	sumOfCol = 0
	for col in range(k):
		for row in range(len(motifmatrix)):
			text = motifmatrix[row]
			symbol = text[col]
			num = SymbolToNumber(symbol)
			countMatrix[num][col] = countMatrix[num][col] + 1

	for row in range(len(countMatrix)):
		for col in range(k):
			countMatrix[row][col] = countMatrix[row][col] + 1

	for row in range(4):
		sumOfCol += countMatrix[row][0]

	profileMatrix = [[0] * k for a in range(4)]
	for row in range(4):
		for col in range(k):
			div = countMatrix[row][col]
			profileMatrix[row][col] = div/float(sumOfCol)

	return profileMatrix

def findScore(motifs, k): 
	score = 0
	for col in range(k):
		col_i = []
		for row in range(len(motifs)):
			text = motifs[row]
			col_i.append(text[col])
		freqArray = [0, 0, 0, 0] 
		for sym in col_i:
			symNum = SymbolToNumber(sym)
			freqArray[symNum] = freqArray[symNum] + 1
		maxFreq = max(freqArray)
		score_i = sum(freqArray) - max(freqArray)
		score += score_i

	return score

def GreedyMotifSearch(dna, k, t):
	bestMotifs = [] 
	for i in range(t):
		text = dna[i]
		kmer = text[0:k]
		bestMotifs.append(kmer)

	for c in range(len(dna[0])-k+1):
		motifs = ['']
		text = dna[0]
		motif = text[c:c+k]
		motifs[0] = motif 
		for i in range(1,t):
			profileMatrix = formProfile(motifs, k, t)
			newMotif = profileMostProbable(dna[i], k, profileMatrix)
			motifs.append(newMotif)

		if findScore(motifs, k) < findScore(bestMotifs, k): 
			bestMotifs = motifs

	return bestMotifs

def main():
	with open('rosalind_ba2e.txt', 'r') as myfile:
		data = myfile.readlines()
	numbers = data[0]
	numbers = numbers.rstrip('\n')
	nums = numbers.split()
	k = int(nums[0])
	t = int(nums[1])
	dna = []
	for i in range(1, len(data)):
		text = data[i]
		text = text.rstrip('\n')
		dna.append(text)
		
	bestMotifs = GreedyMotifSearch(dna, k, t)
	for motif in bestMotifs:
		print(motif)
 
if __name__ == "__main__":
	main()

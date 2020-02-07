import random

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

def GenerateMotifs(profileMatrix, dna, k):
	motifs = []
	for i in range(len(dna)):
		text = dna[i]
		newMotif = profileMostProbable(text, k, profileMatrix)
		motifs.append(newMotif)

	return motifs

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

def GenerateMostLikelyMotif(text, k, profileMatrix):
	probArray = [] 
	for i in range(len(text)-k+1):
		kmer = text[i:i+k]
		probability = 1
		for a in range(len(kmer)):
			symbol = kmer[a] 
			j = SymbolToNumber(symbol)
			probability = probability * profileMatrix[j][a]

		probArray.append(probability)

	sumOfProb = sum(probArray)
	for m in range(len(probArray)):
		probArray[m] = probArray[m]/float(sumOfProb)
	randNum = random.uniform(0,1)
	for a in range(1, len(probArray)):
		probArray[a] = probArray[a-1] + probArray[a]
	m = 0
	while randNum > probArray[m]:
		m = m + 1
	indexOfkmer = m 
	likelyKmer = text[m:m+k]

	return likelyKmer


def GibbsSampler(dna, k, t, N):
	motifs = []
	bestMotifs = [] 
	for i in range(t):
		text = dna[i]
		size = len(text) - k 
		rand = random.randint(0, size)
		randkmer = text[rand:rand+k]
		motifs.append(randkmer)

	bestMotifs = motifs
	for i in range(N):
		a = random.randint(0, t-1)
		newMotifs = []
		for m in range(t):
			if m != a: 
				newMotifs.append(motifs[m])
		profile = formProfile(newMotifs, k, t)
		motifs[a] = GenerateMostLikelyMotif(dna[a], k, profile)
		if findScore(motifs, k) < findScore(bestMotifs, k):
			bestMotifs = motifs 

	return bestMotifs


def main():
	with open('rosalind_ba2g.txt', 'r') as myfile:
		data = myfile.readlines()
	numbers = data[0]
	numbers = numbers.rstrip('\n')
	nums = numbers.split()
	k = int(nums[0])
	t = int(nums[1])
	N = int(nums[2])
	dna = []
	for i in range(1, len(data)):
		text = data[i]
		text = text.rstrip('\n')
		dna.append(text)
		
	bestMotifs = GibbsSampler(dna, k, t, N)
	scoreBest = findScore(bestMotifs, k)
	for i in range(20):
		random1 = GibbsSampler(dna, k, t, N)
		if findScore(random1, k) < scoreBest:
			scoreBest = findScore(random1, k)
			bestMotifs = random1

	for motif in bestMotifs:
		print(motif)
 
if __name__ == "__main__":
	main()
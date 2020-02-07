def HammingDistance(text1, text2):
	count = 0
	for i in range(len(text1)):
		if text1[i] != text2[i]:
			count = count + 1
	return count

def DistanceBetweenPatternAndString(pattern, dna):
	k = len(pattern)
	distance = 0
	for i in range(len(dna)):
		text = dna[i]
		hammingDistance = len(text)
		for i in range(len(text)-k+1):
			kmer = text[i:i+k]
			if hammingDistance > HammingDistance(kmer, pattern):
				hammingDistance = HammingDistance(kmer, pattern)
		distance = distance + hammingDistance

	return distance 

def main():
	with open('rosalind_ba2h.txt', 'r') as myfile:
		data = myfile.readlines()
	pattern = data[0]
	pattern = pattern.rstrip('\n')
	strings = data[1]
	strings = strings.rstrip('\n')
	dna = strings.split()
		
	distance = DistanceBetweenPatternAndString(pattern, dna)
	print(distance)
 
if __name__ == "__main__":
	main()

def profileMostProbable(text, k, matrix):
	probKmer = ''
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


def main():
	with open('rosalind_ba2c (1).txt', 'r') as myfile:
		data = myfile.readlines()
	text = data[0]
	text = text.rstrip('\n')
	k = int(data[1])
	matrix = []
	for i in range(2, len(data)):
		numbers = data[i]
		numbers = numbers.rstrip('\n')
		nums = numbers.split()
		for a in range(len(nums)):
			nums[a] = float(nums[a])
		matrix.append(nums)
		
	probKmer = profileMostProbable(text, k, matrix)
	print(probKmer)
 
if __name__ == "__main__":
	main()

def breakpoints(genome):
	genome = [0] + genome
	genome.append(len(genome))
	breakpointNumber = 0 
	for i in range(len(genome)-1):
		if genome[i+1] - genome[i] != 1: 
			breakpointNumber += 1

	return breakpointNumber

def main():
	with open('rosalind_ba6b.txt', 'r') as myfile:
		data = myfile.readlines()
	permutation = data[0].rstrip('\n')
	permutation = permutation.split()
	newPermutation = []
	for i in range(len(permutation)):
		if i == 0: 
			a = permutation[0]
			newNum = int(a[1:])
			newPermutation.append(newNum)
		if i == len(permutation)-1:
			a = permutation[len(permutation)-1].rstrip(')')
			newPermutation.append(int(a))
		if i != 0 and i != len(permutation)-1:
			newPermutation.append(int(permutation[i]))
	
	breakpointNum = breakpoints(newPermutation)

	print(breakpointNum)



if __name__ == "__main__":
	main()
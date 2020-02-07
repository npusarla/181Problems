def cycleToChromosome(nodes):
	chromosome = [0] *(len(nodes)/2)
	for i in range(1, (len(nodes)/2)+1):
		if nodes[(2*i)-1-1] < nodes[(2*i)-1]:
			chromosome[i-1] = nodes[(2*i)-1]/2
		else:
			chromosome[i-1] = -nodes[(2*i)-2]/2

	return chromosome

def main():
	with open('rosalind_ba6g.txt', 'r') as myfile:
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
	
	chromosome = cycleToChromosome(newPermutation)
	newStr = '('
	for i in range(len(chromosome)):
		if i == 0: 
			if chromosome[i] > 0:
				newStr += "+" + str(chromosome[i])
			else:
				newStr += str(chromosome[i])
		else: 
			if chromosome[i] > 0:
				newStr += ' ' + '+' + str(chromosome[i])
			else:
				newStr += ' ' + str(chromosome[i])

	newStr += ')'
	print(newStr)


if __name__ == "__main__":
	main()
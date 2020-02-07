def chromosomeToCycle(chromosome):
	nodes = [0] * 2*len(chromosome)
	for j in range(len(chromosome)):
		i = chromosome[j]
		if i > 0: 
			nodes[(2*j)-1] = (2*i) - 1
			nodes[2*j] = 2*i
		else: 
			nodes[(2*j)-1] = -2*i
			nodes[2*j] = -(2*i) - 1

	nodes = [nodes[-1]] + nodes[:-1]
	return nodes 

def main():
	with open('rosalind_ba6f.txt', 'r') as myfile:
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
	
	nodes = chromosomeToCycle(newPermutation)
	newStr = '('
	for i in range(len(nodes)):
		if i == 0: 
			newStr += str(nodes[i])
		else: 
			newStr += ' ' + str(nodes[i])

	newStr += ')'
	print(newStr)


if __name__ == "__main__":
	main()
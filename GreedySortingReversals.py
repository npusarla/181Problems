def GreedySorting(permutation):
	listOfPermutations = []
	for i in range(len(permutation)):
		if permutation[i] != i+1:
			#find the location of i 
			if i+1 not in permutation:
				index = permutation.index(-(i+1))
			else: 
				index = permutation.index(i+1)
			reversal = [] 
			for k in range(i,index+1):
				newNum = -permutation[k]
				reversal.append(newNum)
			reversal.reverse()
			newList = permutation[0:i] + reversal + permutation[index+1:]
			permutation = newList
			listOfPermutations.append(newList)
			# print(listOfPermutations)
			
			if permutation[i] != i+1:
				newList = []
				for m in range(len(permutation)):
					newList.append(permutation[m])
				newList[i] = -newList[i]
				listOfPermutations.append(newList)
				permutation = newList
		

	return listOfPermutations


def main():
	with open('rosalind_ba6a.txt', 'r') as myfile:
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
	permutations = GreedySorting(newPermutation)

	for perm in permutations:
		newStr = '('
		for i in range(len(perm)):
			if i != 0:
				if perm[i] > 0:
					newStr += " " + "+" + str(perm[i])
				else: 
					newStr += " " + str(perm[i])
			else: 
				if perm[i] > 0:
					newStr += "+" + str(perm[i])
				else: 
					newStr += str(perm[i])

		newStr += ')'
		print(newStr)



if __name__ == "__main__":
	main()
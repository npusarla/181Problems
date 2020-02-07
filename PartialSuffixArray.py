def suffixArray(text, k): 
	array = {}
	for i in range(len(text)): 
		array[text[i:]] = i 

	arrayKeys = sorted(array.keys())
	positions = []
	partial = [] 
	for i in range(len(arrayKeys)):
		pos = arrayKeys[i]
		positions.append(array[pos])
		if array[pos]%k == 0: 
			partial.append((i, array[pos]))

	return partial 


def main():
	with open('rosalind_ba9q.txt', 'r') as myfile:
		data = myfile.readlines()
	text = data[0].rstrip('\n')
	k = int(data[1].rstrip('\n'))

	partial = suffixArray(text, k)
	for pair in partial: 
		print(str(pair[0]) + ',' + str(pair[1]))


if __name__ == "__main__":
	main()
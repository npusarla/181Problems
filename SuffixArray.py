def suffixArray(text): 
	array = {}
	for i in range(len(text)): 
		array[text[i:]] = i 

	arrayKeys = sorted(array.keys())
	positions = []
	for pos in arrayKeys:
		positions.append(array[pos])

	return positions


def main():
	with open('sampleData', 'r') as myfile:
		data = myfile.readlines()
	text = data[0].rstrip('\n')
	

	newStr = suffixArray(text)
	print(newStr)


if __name__ == "__main__":
	main()
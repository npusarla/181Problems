def suffixArray(text): 
	array = {}
	for i in range(len(text)): 
		array[text[i:]] = i 

	arrayKeys = sorted(array.keys())
	positions = []
	for pos in arrayKeys:
		positions.append(array[pos])

	return positions

def patternMatching(text, pattern, suffixArray):
	minIndex = 0
	maxIndex = len(text) - 1
	while minIndex <= maxIndex: 
		midIndex = (minIndex+maxIndex)//2
		pos = suffixArray[midIndex]
		if pattern > text[pos:]:
			minIndex = midIndex + 1
		else: 
			maxIndex = midIndex - 1

	#print(minIndex)
	suffix = text[suffixArray[minIndex]:]
	if pattern == suffix[:len(pattern)]:
		first = minIndex
	else: 
		return 'pattern does not appear'

	#print(first)
	minIndex = first 
	#print(suffixArray[first])
	maxIndex = len(text) - 1
	while minIndex <= maxIndex: 
		midIndex = (minIndex+maxIndex)//2
		suffix = text[suffixArray[midIndex]:]
		if pattern == suffix[:len(pattern)]:
			minIndex = midIndex + 1
		else: 
			maxIndex = midIndex - 1

	last = maxIndex
	return (first, last)

def main():
	with open('rosalind_ba9h.txt', 'r') as myfile:
		data = myfile.readlines()
	
	text = data[0].rstrip('\n')
	patterns = []
	for i in range(1, len(data)):
		string = data[i].rstrip('\n')
		patterns.append(string)
	
	positions = suffixArray(text)

	listOfPos = []
	for pattern in patterns: 
		rangeOfPattern = patternMatching(text, pattern, positions)
		for num in range(rangeOfPattern[0], rangeOfPattern[1]+1): 
			listOfPos.append(positions[num])

	listOfPos = sorted(listOfPos)
	for pos in listOfPos: 
		print(pos),


if __name__ == "__main__":
	main()


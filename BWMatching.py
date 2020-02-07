def createFirstAndLast(text):
	lastColumn = []
	firstColumn = []
	positions = {} 
	for i in range(len(text)):
		positions[text[i]] = 0 
	for i in range(len(text)):
		char = text[i]
		pos = positions[char]
		pos += 1
		lastColumn.append((char, pos))
		positions[char] = pos 

	newText = sorted(text)
	for i in range(len(text)):
		positions[text[i]] = 0 
	for char in newText: 
		pos = positions[char]
		pos += 1
		firstColumn.append((char, pos))
		positions[char] = pos 

	return firstColumn, lastColumn

def lastToFirst(firstColumn, lastColumn, index):
	char = lastColumn[index]
	firstIndex = firstColumn.index(char)
	return firstIndex

def bwMatching(firstText, lastText, text, pattern): 
	lastColumn = text
	firstColumn = sorted(text)
	top = 0
	bottom = len(lastColumn)-1
	while top <= bottom: 
		if len(pattern) != 0: 
			symbol = pattern[-1]
			pattern = pattern[:-1]
			ranges = [] 
			for i in range(top, bottom+1):
				if lastColumn[i] == symbol: 
					ranges.append(i)
			if ranges: 
				topIndex = ranges[0]
				bottomIndex = ranges[-1]
				top = lastToFirst(firstText, lastText, topIndex)
				bottom = lastToFirst(firstText, lastText, bottomIndex)
			else: 
				return 0 

		else: 
			return bottom-top+1 

def main():
	with open('rosalind_ba9l.txt', 'r') as myfile:
		data = myfile.readlines()
	text = data[0].rstrip('\n')
	patterns = data[1].rstrip('\n').split() 

	firstColumn, lastColumn = createFirstAndLast(text)
	#print(firstColumn, lastColumn)
	for pattern in patterns: 
		index = bwMatching(firstColumn, lastColumn, text, pattern)
		print(index), 


if __name__ == "__main__":
	main()




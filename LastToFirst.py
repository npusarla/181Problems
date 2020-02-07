def lastToFirst(text, index):
	lastColumn = []
	firstColumn = []
	for i in range(len(text)):
		char = text[i]
		pos = 1 
		for pair in lastColumn: 
			if (char, pos) in lastColumn: 
				pos += 1 
		lastColumn.append((char, pos))

	newText = sorted(text)
	for char in newText: 
		pos = 1
		for pair in firstColumn: 
			if (char, pos) in firstColumn: 
				pos += 1
		firstColumn.append((char, pos))

	char = lastColumn[index]
	firstIndex = firstColumn.index(char)
	return firstIndex

def main():
	with open('rosalind_ba9k.txt', 'r') as myfile:
		data = myfile.readlines()
	text = data[0].rstrip('\n')
	index = int(data[1].rstrip('\n'))

	burrowWheeler = lastToFirst(text, index)

	print(burrowWheeler)


if __name__ == "__main__":
	main()

def burrowsReconstruct(text):
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

	reconstructedText = [firstColumn[0]]
	while len(reconstructedText) < len(text): 
		charToLook = reconstructedText[-1]
		index = lastColumn.index(charToLook)
		reconstructedText.append(firstColumn[index])

	lastVar = reconstructedText[0]
	reconstructedText = reconstructedText[1:] 
	reconstructedText.append(lastVar)
	
	newText = '' 
	for pair in reconstructedText: 	
		newText += str(pair[0])

	return newText

def main():
	with open('rosalind_ba9j.txt', 'r') as myfile:
		data = myfile.readlines()
	text = data[0].rstrip('\n')

	burrowWheeler = burrowsReconstruct(text)

	print(burrowWheeler)


if __name__ == "__main__":
	main()

def FirstOccurrence(text):
	text = sorted(text)
	positions = {}
	positions['$'] = 0
	for i in range(len(text)-1):
		if text[i] != text[i+1]:
			positions[text[i+1]] = i+1 

	return positions 


def firstOccSymbol(positions, symbol):
	return positions[symbol]

def count(symbol, num, lastColumn):
	count = 0
	for i in range(num):
		if lastColumn[i] == symbol: 
			count += 1

	return count

def betterBWMatching(positions, lastColumn, pattern):
	top = 0 
	bottom = len(lastColumn) - 1
	while top <= bottom: 
		if pattern: 
			symbol = pattern[-1]
			pattern = pattern[:-1]
			top = firstOccSymbol(positions, symbol) + count(symbol, top, lastColumn)
			bottom = firstOccSymbol(positions, symbol) + (count(symbol, bottom+1, lastColumn)-1)

		else: 
			return bottom-top+1 

	return 0


def main():
	with open('rosalind_ba9m.txt', 'r') as myfile:
		data = myfile.readlines()
	text = data[0].rstrip('\n')
	patterns = data[1].rstrip('\n').split() 

	positions = FirstOccurrence(text)
	for pattern in patterns: 
		index = betterBWMatching(positions, text, pattern)
		print(index), 


if __name__ == "__main__":
	main()

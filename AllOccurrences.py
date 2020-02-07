def findAllOccurrences(): 

	

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
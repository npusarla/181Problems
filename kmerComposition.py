def getKmers(k, text):
	kmers = [] 
	for i in range(len(text)-k+1):
		kmers.append(text[i:i+k])

	kmers.sort()
	return kmers 

def main():
	with open('rosalind_ba3a.txt', 'r') as myfile:
		data = myfile.readlines()
	numbers = data[0]
	k = int(numbers)
	text = data[1]
	text = text.rstrip('\n')
		
	kmers = getKmers(k, text)

	for motif in kmers:
		print(motif)
 
if __name__ == "__main__":
	main()
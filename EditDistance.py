def editDistance(text1, text2):
	lengths = {} 
	lengths[(-1,-1)] = 0
	for i in range(len(text2)):
		lengths[(-1,i)] = lengths[(-1,i-1)] + 1
		
	for i in range(len(text1)):
		lengths[(i, -1)] = lengths[(i-1, -1)] + 1
		
	for i in range(0, len(text1)):
		for j in range(0, len(text2)):
			
			length1 = lengths[(i-1, j)] + 1
			length2 = lengths[(i, j-1)] + 1
			if text1[i] == text2[j]:
				length3 = lengths[(i-1, j-1)] 
			else:
				length3 = lengths[(i-1, j-1)] + 1
			
			lengths[(i,j)]= min(length1, length2, length3)
			

	return lengths[len(text1)-1, len(text2)-1]

def main():
	with open('rosalind_ba5g.txt', 'r') as myfile:
		data = myfile.readlines()
	text1 = data[0].rstrip('\n')
	text2 = data[1].rstrip('\n')
	
	editDist = editDistance(text1, text2)
	print(editDist)

 
if __name__ == "__main__":
	main()
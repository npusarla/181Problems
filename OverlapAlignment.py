import sys

sys.setrecursionlimit(5000)


def alignmentFitting(text1, text2):
	lengths = {} 
	backtrack = {}
	lengths[(-1,-1)] = 0
	backtrack[(-1,-1)] = '' 
	for i in range(len(text2)):
		lengths[(-1,i)] = lengths[(-1, i-1)] - 1
		backtrack[(-1,i)] = "right"
	for i in range(len(text1)):
		lengths[(i, -1)] = 0
		backtrack[(i, -1)] = "down"
	
	for i in range(0, len(text1)):
		for j in range(0, len(text2)):
			
			length1 = lengths[(i-1, j)] - 2
			length2 = lengths[(i, j-1)] - 2
			if text1[i] == text2[j]:
				length3 = lengths[(i-1, j-1)] + 1
			else:
				length3 = lengths[(i-1, j-1)] - 2
			#print(length1, length2, length3)
			lengths[(i,j)]= max(length1, length2, length3)
			#print(lengths[(i,j)])
			if lengths[(i, j)] == length1:
				backtrack[(i, j)] = "down"
			elif lengths[(i, j)] == length2:
				backtrack[(i, j)] = "right"
			else:
				backtrack[(i, j)] = "diagonal"
			

	str1 = ''
	str2 = ''
	maxScore = 0
	coordinates = (0,0)
	for key in lengths.keys():
		if key[0] == len(text1) -1:
			if maxScore < lengths[key]:
				maxScore = lengths[key]
				coordinates = key 
	
	output = outputLCS(backtrack, text1, text2, coordinates[0], coordinates[1], str1, str2)
	str1 = output[0][::-1]
	str2 = output[1][::-1]

	return maxScore, str1, str2

def outputLCS(backtrack, text1, text2, i, j, str1, str2):
	if j == -1:
		return str1, str2

	if backtrack[(i, j)] == "down":
		str1 += text1[i]
		str2 += '-'
		return outputLCS(backtrack, text1, text2, i-1, j, str1, str2)
	elif backtrack[(i, j)] == "right":
		str1 += '-'
		str2 += text2[j]
		return outputLCS(backtrack, text1, text2, i, j-1, str1, str2)
	elif backtrack[(i, j)] == "diagonal":
		str1 += text1[i]
		str2 += text2[j]
		return outputLCS(backtrack, text1, text2, i-1, j-1, str1, str2)


def main():
	with open('rosalind_ba5i.txt', 'r') as myfile:
		data = myfile.readlines()
	text1 = data[0].rstrip('\n')
	text2 = data[1].rstrip('\n')
	
	score, align1, align2 = alignmentFitting(text1, text2)
	print(score)
	print(align1)
	print(align2)
 
if __name__ == "__main__":
	main()
import sys
scoringMatrix = [] 
lettersDict = {}
sys.setrecursionlimit(5000)
def parseScoringMatrix(matrix):
	letters = matrix[0].rstrip('\n').split()
	for i in range(len(letters)):
		lettersDict[letters[i]] = i 
 
	#produce a scoring matrix 
	for i in range(1, len(matrix)):
		text = matrix[i].rstrip('\n').split() 
		newText = [] 
		for k in range(1, len(text)):
			newText.append(int(text[k]))
		scoringMatrix.append(newText)


def alignmentGlobal(text1, text2):
	lengths = {} 
	backtrack = {}
	lengths[(-1,-1)] = 0
	backtrack[(-1,-1)] = ''  
	for i in range(len(text2)):
		lengths[(-1,i)] = lengths[(-1,i-1)] - 5
		backtrack[(-1,i)] = "right"
	for i in range(len(text1)):
		lengths[(i, -1)] = lengths[(i-1, -1)] - 5
		backtrack[(i, -1)] = "down"
	for i in range(0, len(text1)):
		for j in range(0, len(text2)):
			length1 = lengths[(i-1, j)] - 5
			length2 = lengths[(i, j-1)] - 5
			index1 = lettersDict[text1[i]]
			index2 = lettersDict[text2[j]]
			if text1[i] == text2[j]:
				length3 = lengths[(i-1, j-1)] + scoringMatrix[index1][index1]
			else:
				length3 = lengths[(i-1, j-1)] + scoringMatrix[index2][index1]
			
			lengths[(i,j)]= max(length1, length2, length3)
			
			if lengths[(i, j)] == length1:
				backtrack[(i, j)] = "down"
			elif lengths[(i, j)] == length2:
				backtrack[(i, j)] = "right"
			else:
				backtrack[(i, j)] = "diagonal"

	str1 = ''
	str2 = ''
	output = outputLCS(backtrack, text1, text2, len(text1)-1, len(text2)-1, str1, str2)
	str1 = output[0][::-1]
	str2 = output[1][::-1]

	return lengths[(len(text1)-1, len(text2)-1)], str1, str2

def outputLCS(backtrack, text1, text2, i, j, str1, str2):
	if backtrack[(i, j)] == '' and (i == -1 or j == -1):
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
	with open('sampleData', 'r') as myfile:
		data = myfile.readlines()
	text1 = data[0].rstrip('\n')
	text2 = data[1].rstrip('\n')
	with open('ScoringMatrix.txt', 'r') as scoreMat: 
		matrix = scoreMat.readlines()
		
	parseScoringMatrix(matrix)
	score, align1, align2 = alignmentGlobal(text1, text2)
	print(score)
	print(align1)
	print(align2)
 
if __name__ == "__main__":
	main()
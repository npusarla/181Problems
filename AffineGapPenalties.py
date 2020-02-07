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


def affineGapPenalty(text1, text2):
	lengthsLower = {} 
	lengthsMiddle = {}
	lengthsUpper = {}
	backtrackLower = {}
	backtrackMiddle = {}
	backtrackUpper = {}
	lengthsLower[(-1,-1)] = -1 * sys.maxsize
	lengthsMiddle[(-1,-1)] = 0
	lengthsUpper[(-1,-1)] = -1 * sys.maxsize
	backtrackLower[(-1,-1)] = ''
	backtrackMiddle[(-1,-1)] = ''
	backtrackUpper[(-1,-1)] = ''  
	for i in range(len(text2)):
		if i == 0:
			lengthsUpper[(-1,i)] = -11
			lengthsMiddle[(-1, i)] = -11
			backtrackUpper[(-1,i)] = "toUpper"
		else: 
			lengthsUpper[(-1,i)] = lengthsUpper[(-1,i-1)] - 1
			lengthsMiddle[(-1, i)] = lengthsMiddle[(-1,i-1)] - 1
			backtrackUpper[(-1,i)] = "right"
		lengthsLower[(-1, i)] = -sys.maxsize
		backtrackLower[(-1, i)] = ''
		backtrackMiddle[(-1, i)] = ''
	for i in range(len(text1)):
		if i == 0:
			lengthsLower[(i, -1)] = -11
			lengthsMiddle[(i, -1)] = -11
			backtrackLower[(i, -1)] = "toLower"
		else: 
			lengthsLower[(i, -1)] = lengthsLower[(i-1, -1)] - 1
			lengthsMiddle[(i, -1)] = lengthsMiddle[(i-1, -1)] - 1
			backtrackLower[(i, -1)] = "down"
		lengthsUpper[(i, -1)] = -sys.maxsize
		backtrackUpper[(i, -1)] = ''
		backtrackMiddle[(i, -1)] = ''

	#for i in range(0, len(text1)):
		#for j in range(0, len(text2)):
			#lengthsLower[(i, j)] = -sys.maxsize
			#lengthsMiddle[(i, j)] = -sys.maxsize
			#lengthsUpper[(i, j)] = -sys.maxsize
	for i in range(0, len(text1)):
		for j in range(0, len(text2)):
			index1 = lettersDict[text1[i]]
			index2 = lettersDict[text2[j]]
			length1Lower = lengthsLower[(i-1, j)] - 1
			length2Lower = lengthsMiddle[(i-1, j)] - 11
			lengthsLower[(i,j)]= max(length1Lower, length2Lower)
			length1Upper = lengthsUpper[(i,j-1)] - 1
			length2Upper = lengthsMiddle[(i, j-1)] - 11
			lengthsUpper[(i,j)] = max(length1Upper, length2Upper)
			length1Middle = lengthsLower[(i,j)]
			length2Middle = lengthsMiddle[(i-1, j-1)] + scoringMatrix[index1][index2]
			length3Middle = lengthsUpper[(i,j)]
			index1 = lettersDict[text1[i]]
			index2 = lettersDict[text2[j]]
			
			#print(lengthsLower[(i,j)])
			lengthsMiddle[(i,j)] = max(length1Middle, length2Middle, length3Middle)
			
			#print(lengthsUpper[(i,j)])
			
			if lengthsLower[(i, j)] == length1Lower:
				backtrackLower[(i, j)] = "down"
			elif lengthsLower[(i, j)] == length2Lower:
				backtrackLower[(i, j)] = "toLower"
			if lengthsMiddle[(i, j)] == length1Middle:
				backtrackMiddle[(i, j)] = "fromLower"
			elif lengthsMiddle[(i, j)] == length2Middle:
				backtrackMiddle[(i, j)] = "diagonal"
			elif lengthsMiddle[(i, j)] == length3Middle:
				backtrackMiddle[(i, j)] = "fromUpper"
			if lengthsUpper[(i,j)] == length1Upper: 
				backtrackUpper[(i,j)] = "right"
			elif lengthsUpper[(i,j)] == length2Upper:
				backtrackUpper[(i,j)] = "toUpper"
			

	str1 = ''
	str2 = ''
	output = outputLCS(backtrackMiddle, backtrackLower, backtrackUpper, backtrackMiddle, text1, text2, len(text1)-1, len(text2)-1, str1, str2)
	str1 = output[0][::-1]
	str2 = output[1][::-1]

	return lengthsMiddle[(len(text1)-1, len(text2)-1)], str1, str2

def outputLCS(currentBackT, backtrackLower, backtrackUpper, backtrackMiddle, text1, text2, i, j, str1, str2):

	if currentBackT[(i, j)] == '' and (i == -1 or j == -1):
		return str1, str2

	if currentBackT[(i, j)] == "down":
		str1 += text1[i]
		str2 += '-'
		return outputLCS(currentBackT, backtrackLower, backtrackUpper, backtrackMiddle, text1, text2, i-1, j, str1, str2)
	elif currentBackT[(i,j)] == "toLower":
		str1 += text1[i]
		str2 += '-'
		return outputLCS(backtrackMiddle, backtrackLower, backtrackUpper, backtrackMiddle, text1, text2, i-1, j, str1, str2)
	elif currentBackT[(i,j)] == "fromLower":
		return outputLCS(backtrackLower, backtrackLower, backtrackUpper, backtrackMiddle, text1, text2, i, j, str1, str2)
	elif currentBackT[(i, j)] == "diagonal":
		str1 += text1[i]
		str2 += text2[j]
		return outputLCS(backtrackMiddle, backtrackLower, backtrackUpper, backtrackMiddle, text1, text2, i-1, j-1, str1, str2)
	elif currentBackT[(i,j)] == "fromUpper":
		return outputLCS(backtrackUpper, backtrackLower, backtrackUpper, backtrackMiddle, text1, text2, i, j, str1, str2)
	elif currentBackT[(i, j)] == "right":
		str1 += '-'
		str2 += text2[j]
		return outputLCS(currentBackT, backtrackLower, backtrackUpper, backtrackMiddle, text1, text2, i, j-1, str1, str2)
	elif currentBackT[(i,j)] == "toUpper":
		str1 += '-'
		str2 += text2[j]
		return outputLCS(backtrackMiddle, backtrackLower, backtrackUpper, backtrackMiddle, text1, text2, i, j-1, str1, str2)
	

def main():
	with open('rosalind_ba5j.txt', 'r') as myfile:
		data = myfile.readlines()
	text1 = data[0].rstrip('\n')
	text2 = data[1].rstrip('\n')
	with open('ScoringMatrix.txt', 'r') as scoreMat: 
		matrix = scoreMat.readlines()
		
	parseScoringMatrix(matrix)
	score, align1, align2 = affineGapPenalty(text1, text2)
	print(score)
	print(align1)
	print(align2)
 
if __name__ == "__main__":
	main()
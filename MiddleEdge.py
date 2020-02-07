scoringMatrix = [] 
lettersDict = {}

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


def linearSpaceMiddle(v, w):
	array1 = []
	array2 = []
	backtrack = []
	array1.append(0)
	array2.append(-5) 
	backtrack.append("right")
	for i in range(1, len(v)+1):
		array1.append(array1[i-1] - 5)
	k = 0

	while k < len(w):
		if k != 0: 
			array1 = array2
			array2 = [] 
			array2.append(array1[0] - 5)
			backtrack = [] 
			backtrack.append("right")
		
		for i in range(1, len(v)+1):
			length1 = array2[i-1] - 5
			length2 = array1[i] - 5
			index1 = lettersDict[v[i-1]]
			index2 = lettersDict[w[k]]
			length3 = array1[i-1] + scoringMatrix[index1][index2]
			
			score = max(length1, length2, length3)
				# print('score: ', score)
				# print(i, (length1, length2, length3))
			print('before last append:')
			if k == len(w) - 1:
				# if i == len(v):
				print('score: ', score)
				print(length1, length2, length3)
				print(backtrack)

			if score == length3:
				backtrack.append("diagonal")
			elif score == length1:
				backtrack.append("down")
			elif score == length2: 
				backtrack.append("right")
			# if k == len(w) - 1:
			# 	print('bt : ', backtrack[-1])
			# 	print(len(backtrack))
			print('after last append:')
			if k == len(w) - 1:
				# if i == len(v):
				print(backtrack)
			
			array2.append(score)
			
		k += 1

	print(backtrack)

	return backtrack, array2

def middleEdge(v, w):
	middle = len(w)/2 
	backtrack1, leftList = linearSpaceMiddle(v, w[0:middle])
	rightHalf = w[middle:len(w)]
	backtrack2, rightList = linearSpaceMiddle(v[::-1], rightHalf[::-1])
	rightList = rightList[::-1]
	maxScore = -5000
	middleNodeIndex = 0 
	for i in range(len(leftList)):
		if (leftList[i] + rightList[i]) > maxScore:
			maxScore = leftList[i] + rightList[i]
			middleNodeIndex = i 

	middleCoords = (middleNodeIndex, middle)
	backtrack2 = backtrack2[::-1]
	print(backtrack2)
	print(len(backtrack2))
	edgeDirection = backtrack2[middleNodeIndex]
	if edgeDirection == "diagonal":
		nextCoords = (middleNodeIndex+1, middle + 1)
	elif edgeDirection == "right":
		nextCoords = (middleNodeIndex, middle + 1)
	else:
		nextCoords = (middleNodeIndex + 1, middle)

	return middleCoords, nextCoords


def main():
	with open('sampleData', 'r') as myfile:
		data = myfile.readlines()
	v = data[0].rstrip('\n')
	w = data[1].rstrip('\n')
	with open('ScoringMatrix.txt', 'r') as scoreMat: 
		matrix = scoreMat.readlines()
		
	parseScoringMatrix(matrix)
	middleCoords = middleEdge(v,w)
	print(str(middleCoords[0]) + ' ' + str(middleCoords[1]))
 
if __name__ == "__main__":
	main()

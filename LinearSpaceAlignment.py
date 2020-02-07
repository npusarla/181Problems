import sys
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

def calculateScore(str1, str2):
	score = 0
	for i in range(len(str1)):
		if str1[i] != '-' and str2[i] != '-':
			index1 = lettersDict[str1[i]]
			index2 = lettersDict[str2[i]]
			score += scoringMatrix[index1][index2]
		else:
			score += -5

	return score 


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
			if v[i-1] == w[k]:
				length3 = array1[i-1] + scoringMatrix[index1][index1]
			else:
				length3 = array1[i-1] + scoringMatrix[index2][index1]
			
			score = max(length1, length2, length3)
			if score == length3:
				backtrack.append("diagonal")
			elif score == length1:
				backtrack.append("down")
			elif score == length2: 
				backtrack.append("right")
			array2.append(score)
			
		k += 1

	return backtrack, array2

def middleEdge(v, w):
	middle = len(w)/2 
	backtrack, leftList = linearSpaceMiddle(v, w[0:middle])
	rightHalf = w[middle:len(w)]
	backtrack, rightList = linearSpaceMiddle(v[::-1], rightHalf[::-1])
	rightList = rightList[::-1]
	maxScore = -1 * sys.maxsize
	middleNodeIndex = 0 
	for i in range(len(leftList)):
		if (leftList[i] + rightList[i]) > maxScore:
			maxScore = leftList[i] + rightList[i]
			middleNodeIndex = i 

	middleCoords = (middleNodeIndex, middle)
	

	backtrack = backtrack[::-1]
	edgeDirection = backtrack[middleNodeIndex]
	if edgeDirection == "diagonal":
		nextCoords = (middleNodeIndex+1, middle + 1)
	elif edgeDirection == "right":
		nextCoords = (middleNodeIndex, middle + 1)
	else:
		nextCoords = (middleNodeIndex + 1, middle)

	return middleCoords, edgeDirection

def linearSpaceAlignment(v, w, top, bottom, left, right):
	if left == right: 
		return v[top:bottom], '-'*(bottom-top)
	if top == bottom: 
		return '-'*(right-left), w[left:right]
	
	(vertical, horizontal), midEdge = middleEdge(v[top:bottom], w[left:right])
	print(v[top:bottom], w[left:right])
	print(vertical, horizontal, midEdge)

	vertical += top
	horizontal += left

	str1, str2 = linearSpaceAlignment(v, w, top, vertical, left, horizontal)
	
	if midEdge == "right":
		str1 += '-'
		str2 += w[horizontal]
		horizontal = horizontal + 1
	if midEdge == "diagonal":
		str1 += v[vertical]
		str2 += w[horizontal]
		horizontal = horizontal + 1
		vertical = vertical + 1
	if midEdge == "down":
		str1 += v[vertical]
		str2 += '-'
		vertical = vertical + 1
	
	oneP, secondP = linearSpaceAlignment(v, w, vertical, bottom, horizontal, right)
	str1 += oneP
	str2 += secondP
	
	return str1, str2


def main():
	with open('rosalind_ba5l.txt', 'r') as myfile:
		data = myfile.readlines()
	v = data[0].rstrip('\n')
	w = data[1].rstrip('\n')
	with open('ScoringMatrix.txt', 'r') as scoreMat: 
		matrix = scoreMat.readlines()
		
	parseScoringMatrix(matrix)
	alignment1, alignment2 = linearSpaceAlignment(v, w, 0, len(v), 0, len(w))
	score = calculateScore(alignment1, alignment2)
	print(score)
	print(alignment1)
	print(alignment2)

if __name__ == "__main__":
	main()

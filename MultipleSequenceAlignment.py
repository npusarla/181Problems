def multipleSequenceAlignment(v, w, u):
	lengths = {} 
	backtrack = {}
	backtrack[(-1, -1, -1)] = ''
	for i in range(-1, len(v)):
		for j in range(-1, len(w)):
			for k in range(-1, len(u)):
				lengths[(i, j, k)] = 0
	for i in range(len(v)):
		backtrack[(i, -1, -1)] = "firstDir"
	for j in range(len(w)):
		backtrack[(-1, j, -1)] = "secondDir"
	for k in range(len(u)):
		backtrack[(-1, -1, k)] = "thirdDir"
	for i in range(len(v)):
		for j in range(len(w)):
			backtrack[(i, j, -1)] = "fourthDir"
	for i in range(len(v)):
		for k in range(len(u)):
			backtrack[(i, -1, k)] = "fifthDir"
	for j in range(len(w)):
		for k in range(len(u)):
			backtrack[(-1, j, k)] = "sixthDir"

	for i in range(0, len(v)):
		for j in range(0, len(w)):
			for k in range(0, len(u)):
				length1 = lengths[(i-1, j, k)] #this means that (v[i], -, -)
				length2 = lengths[(i, j-1, k)] #this means that (-, w[j], -) 
				length3 = lengths[(i, j, k-1)] #this means that (-, -, u[k])
				length4 = lengths[(i-1, j-1, k)] #this means that (v[i], w[j], -)	
				length5 = lengths[(i-1, j, k-1)] #this means that (v[i], -, u[k])
				length6 = lengths[(i, j-1, k-1)] #this means that (-, w[j], u[k])			
				if v[i] == w[j] and v[i] == u[k]: 
					length7 = lengths[(i-1, j-1, k-1)] + 1 #this means that (v[i], w[j], u[k])
				else:
					length7 = lengths[(i-1, j-1, k-1)] 
				
				lengths[(i,j,k)]= max(length1, length2, length3, length4, length5, length6, length7)
				
				if lengths[(i, j, k)] == length1:
					backtrack[(i, j, k)] = "firstDir"
				if lengths[(i, j, k)] == length2:
					backtrack[(i, j, k)] = "secondDir"
				if lengths[(i, j, k)] == length3:
					backtrack[(i, j, k)] = "thirdDir"
				if lengths[(i, j, k)] == length4:
					backtrack[(i, j, k)] = "fourthDir"
				if lengths[(i, j, k)] == length5:
					backtrack[(i, j, k)] = "fifthDir"
				if lengths[(i, j, k)] == length6:
					backtrack[(i, j, k)] = "sixthDir"
				if lengths[(i, j, k)] == length7:
					backtrack[(i, j, k)] = "seventhDir"

	str1 = ''
	str2 = ''
	str3 = ''
	output = outputLCS(backtrack, v, w, u, len(v)-1, len(w)-1, len(u)-1, str1, str2, str3)
	str1 = output[0][::-1]
	str2 = output[1][::-1]
	str3 = output[2][::-1]

	return lengths[(len(v)-1, len(w)-1, len(u)-1)], str1, str2, str3

def outputLCS(backtrack, v, w, u, i, j, k, str1, str2, str3):
	if backtrack[(i, j, k)] == '' and (i == -1 or j == -1 or k == -1):
		return str1, str2, str3

	if backtrack[(i, j, k)] == "firstDir":
		str1 += v[i]
		str2 += '-'
		str3 += '-'
		return outputLCS(backtrack, v, w, u, i-1, j, k, str1, str2, str3)
	elif backtrack[(i, j, k)] == "secondDir":
		str1 += '-'
		str2 += w[j]
		str3 += '-'
		return outputLCS(backtrack, v, w, u, i, j-1, k, str1, str2, str3)
	elif backtrack[(i, j, k)] == "thirdDir":
		str1 += '-'
		str2 += '-'
		str3 += u[k]
		return outputLCS(backtrack, v, w, u, i, j, k-1, str1, str2, str3)
	elif backtrack[(i, j, k)] == "fourthDir":
		str1 += v[i]
		str2 += w[j]
		str3 += '-'
		return outputLCS(backtrack, v, w, u, i-1, j-1, k, str1, str2, str3)
	elif backtrack[(i, j, k)] == "fifthDir":
		str1 += v[i]
		str2 += '-'
		str3 += u[k]
		return outputLCS(backtrack, v, w, u, i-1, j, k-1, str1, str2, str3)
	elif backtrack[(i, j, k)] == "sixthDir":
		str1 += '-'
		str2 += w[j]
		str3 += u[k]
		return outputLCS(backtrack, v, w, u, i, j-1, k-1, str1, str2, str3)
	elif backtrack[(i, j, k)] == "seventhDir":
		str1 += v[i]
		str2 += w[j]
		str3 += u[k]
		return outputLCS(backtrack, v, w, u, i-1, j-1, k-1, str1, str2, str3)


def main():
	with open('rosalind_ba5m.txt', 'r') as myfile:
		data = myfile.readlines()
	text1 = data[0].rstrip('\n')
	text2 = data[1].rstrip('\n')
	text3 = data[2].rstrip('\n')
		
	score, align1, align2, align3  = multipleSequenceAlignment(text1, text2, text3)
	print(score)
	print(align1)
	print(align2)
	print(align3)
 
if __name__ == "__main__":
	main()
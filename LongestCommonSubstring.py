def findLongestString(text1, text2, text3):
	longestString = text1
	listOfStrings = [text2, text3]
	for i in range(len(listOfStrings)):
		if len(listOfStrings[i]) > len(longestString):
			longestString = listOfStrings[i]

	return longestString

def longestCommonSubstring(text1, text2):
	lengths = {} 
	lengths[('','')] = ''
	for i in range(len(text2)):
		lengths[('',text2[0:i+1])] = ''
	for i in range(len(text1)):
		lengths[(text1[0:i+1], '')] = ''
	for char1 in range(0, len(text1)):
		for char2 in range(0, len(text2)):
			length1 = lengths[(text1[0:char1], text2[0:char2+1])]
			length2 = lengths[(text1[0:char1+1], text2[0:char2])]
			if text1[char1] == text2[char2]:
				length3 = lengths[(text1[0:char1], text2[0:char2])] + text1[char1]
			else:
				length3 = lengths[(text1[0:char1], text2[0:char2])]
			lengths[(text1[0:char1+1], text2[0:char2+1])]=findLongestString(length1, length2, length3)

	return lengths[(text1, text2)]

def main():
	with open('rosalind_ba5c.txt', 'r') as myfile:
		data = myfile.readlines()
	text1 = data[0].rstrip('\n')
	text2 = data[1].rstrip('\n')
		
	longestSubstring = longestCommonSubstring(text1, text2)
	print(longestSubstring)
 
if __name__ == "__main__":
	main()
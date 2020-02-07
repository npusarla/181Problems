def suffixArray(text): 
	array = {}
	for i in range(len(text)): 
		array[text[i:]] = i 

	arrayKeys = sorted(array.keys())

	return arrayKeys

def treeFromArray
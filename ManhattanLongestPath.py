def longestPath(n, m, right, down):
	length = {}
	length[(0, 0)] = 0 
	for i in range(1, n+1):
		length[(i, 0)] = length[(i-1,0)] + down[i-1][0]
	for i in range(1, m+1):
		length[(0,i)] = length[(0, i-1)] + right[0][i-1]
	for i in range(1, n+1):
		for j in range(1, m+1):
			length[(i,j)] = max(length[(i-1,j)] + down[i-1][j], length[(i, j-1)] + right[i][j-1])

	return length[(n,m)]

def main():
	with open('rosalind_ba5b.txt', 'r') as myfile:
		data = myfile.readlines()
	nAndm = data[0].rstrip('\n').split()
	n = int(nAndm[0])
	m = int(nAndm[1])
	down = []
	right = [] 
	for i in range(1, len(data)):
		if 1 <= i <= n:
			text = data[i].rstrip('\n').split()
			text = list(map(int, text))
			down.append(text)
		if n+2 <= i <= n+n+2:
			text = data[i].rstrip('\n').split()
			text = list(map(int, text))
			right.append(text)
		
	pathLength = longestPath(n, m, right, down)
	print(pathLength)
 
if __name__ == "__main__":
	main()
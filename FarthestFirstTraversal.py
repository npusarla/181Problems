import math 

def euclideanDistance(v, w):
	distance = 0
	m = len(v)
	for i in range(m):
		distance += ((v[i]-w[i])**2)

	return math.sqrt(distance)

def minDistToCenter(dataPoint, centers):
	minDist = 99999999
	for point in centers: 
		distance = euclideanDistance(point, dataPoint)
		if distance < minDist: 
			minDist = distance

	return minDist

def maxDistance(data, centers):
	maxDist = 0 
	dataPoint = []
	for point in data: 
		distance = minDistToCenter(point, centers)
		if distance > maxDist: 
			maxDist = distance
			dataPoint = point 

	return dataPoint

def farthestFirstTraversal(k, data):
	centers = [data[0]]
	while(len(centers) < k):
		dataPoint = maxDistance(data, centers)
		centers.append(dataPoint)

	return centers 

def main():
	with open('rosalind_ba8a.txt', 'r') as myfile:
		data = myfile.readlines()
	
	numbers = data[0].rstrip('\n')
	numbers = numbers.split() 
	k = int(numbers[0])
	m = int(numbers[1])
	points = []
	for i in range(1, len(data)):
		string = data[i].rstrip('\n')
		setOfPoints = string.split() 
		for i in range(m): 
			setOfPoints[i] = float(setOfPoints[i])

		points.append(setOfPoints)

	centers = farthestFirstTraversal(k, points)
	for center in centers: 
		newStr = str(center[0])
		for i in range(1,m):
			newStr += ' ' + str(center[i])
		print(newStr)

if __name__ == "__main__":
	main()



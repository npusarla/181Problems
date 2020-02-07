import math 
import random 

def euclideanDistance(v, w):
	distance = 0
	m = len(v)
	for i in range(m):
		distance += ((v[i]-w[i])**2)

	return math.sqrt(distance)

def minDistToCenter(dataPoint, centers):
	minDist = 99999999
	minPoint = [] 
	for point in centers: 
		distance = euclideanDistance(point, dataPoint)
		if distance < minDist: 
			minDist = distance
			minPoint = point 

	return minDist, minPoint

def calculatePulls(B, dataPoint, centers):
	pulls = []
	for center in centers: 
		distance = math.exp(-1 * B * euclideanDistance(dataPoint, center))
		pulls.append(distance)

	return pulls 

def fromCentersToClusters(data, centers, B):
	hiddenMatrix = {} 
	k = len(centers)
	for j in range(len(data)):
		dataPoint = data[j]
		if tuple(dataPoint) not in centers:
			pulls = calculatePulls(B, dataPoint, centers)
			sumOfPulls = sum(pulls)
			for i in range(len(centers)):
				center = centers[i]
				hiddenMatrix[(i, j)] = pulls[i]/sumOfPulls
			#center = minDistToCenter(dataPoint, centers)[1]
			#clusters[tuple(center)].append(dataPoint)
				
	return hiddenMatrix

def fromClustersToCenters(data, hiddenMatrix, k, m):
	centers = [] 
	for i in range(k):
		newCenter = [] 
		pulls = [] 
		for j in range(len(data)):
			pulls.append(hiddenMatrix[(i,j)])
		for index in range(m):
			sums = [] 
			for j in range(len(data)):
				dataPoint = data[j]
				sums.append(pulls[j] * dataPoint[index])

			newCenter.append(sum(sums)/sum(pulls))

		centers.append(newCenter)				

	return centers

def softKClustering(k, m, B, data):
	centers = []
	for i in range(k):
		centers.append(data[i])
	for i in range(100):
		hiddenMatrix = fromCentersToClusters(data, centers, B)
		centers = fromClustersToCenters(data, hiddenMatrix, k, m)

	return centers

def main():
	with open('rosalind_ba8d.txt', 'r') as myfile:
		data = myfile.readlines()
	
	numbers = data[0].rstrip('\n')
	numbers = numbers.split() 
	k = int(numbers[0])
	m = int(numbers[1])
	B = float(data[1].rstrip('\n'))
	points = []
	for i in range(2, len(data)):
		string = data[i].rstrip('\n')
		setOfPoints = string.split() 
		for i in range(m): 
			setOfPoints[i] = float(setOfPoints[i])

		points.append(setOfPoints)

	centers = softKClustering(k, m, B, points)
	for center in centers: 
		newStr = str(round(center[0],3))
		indexOfPeriod = newStr.index('.')
		needZeroes = 0
		if len(newStr[indexOfPeriod+1:]) < 3: 
			needZeroes = 3 - len(newStr[indexOfPeriod+1:])
		for i in range(needZeroes):
			newStr += '0'
		for i in range(1,m):
			toAdd = str(round(center[i],3))
			indexOfPeriod = toAdd.index('.')
			needZeroes = 0
			if len(toAdd[indexOfPeriod+1:]) < 3: 
				needZeroes = 3 - len(toAdd[indexOfPeriod+1:])
			for k in range(needZeroes):
				toAdd += '0'
			newStr += ' ' + toAdd
		print(newStr)

if __name__ == "__main__":
	main()

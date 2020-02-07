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

def randomlyChoosePoint(centers, data):
	distances = [] 
	points = [] 
	for dataPoint in data: 
		distances.append((minDistToCenter(dataPoint, centers)[0])**2)
		points.append(dataPoint)

	sumOfArray = sum(distances)
	probArray = [] 
	for m in range(len(distances)):
		probArray.append(distances[m]/sumOfArray)
	randNum = random.uniform(0,1)
	for a in range(1, len(probArray)):
		probArray[a] = probArray[a-1] + probArray[a]
	m = 0
	while randNum > probArray[m]:
		m = m + 1

	likelyPoint = points[m]
	return likelyPoint
	
def kMeansandInitializer(data, k):
	centers = [data[0]]
	while (len(centers) < k):
		dataPoint = randomlyChoosePoint(centers, data)
		centers.append(dataPoint)

	return centers

def fromCentersToClusters(data, centers):
	clusters = {}
	for center in centers: 
		clusters.setdefault(tuple(center), [])
		#clusters[tuple(center)] = [] 
	for dataPoint in data: 
		if tuple(dataPoint) not in centers: 
			center = minDistToCenter(dataPoint, centers)[1]
			clusters[tuple(center)].append(dataPoint)

	return clusters 

def fromClustersToCenters(data, clusters, m):
	centers = [] 
	for center in clusters.keys(): 
		newCenter = [] 
		for i in range(m): 
			numbers = [] 
			for dataPoint in clusters[center]:
				numbers.append(dataPoint[i])
			newCenter.append(sum(numbers)/len(numbers))
		
		centers.append(newCenter)

	return centers

def lloydAlgorithm(k, m, data):
	centers = []
	for i in range(k):
		centers.append(data[i])
	clusters = fromCentersToClusters(data, centers)
	newCenters = fromClustersToCenters(data, clusters, m)
	while (newCenters != centers):
		centers = newCenters
		clusters = fromCentersToClusters(data, centers)
		newCenters = fromClustersToCenters(data, clusters, m)

	return newCenters

def main():
	with open('rosalind_ba8c.txt', 'r') as myfile:
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

	centers = lloydAlgorithm(k, m, points)
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

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

def squaredErrorDistortion(data, centers):
	distance = 0 
	for dataPoint in data: 
		distance += ((minDistToCenter(dataPoint, centers))**2)

	errorDist = distance/len(data)
	return errorDist

def main():
	with open('rosalind_ba8b.txt', 'r') as myfile:
		data = myfile.readlines()
	
	numbers = data[0].rstrip('\n')
	numbers = numbers.split() 
	k = int(numbers[0])
	m = int(numbers[1])
	centers = []
	points = [] 
	midPoint = data.index('--------\n')
	for i in range(1, len(data)):
		if i != midPoint: 
			string = data[i].rstrip('\n')
			setOfPoints = string.split() 
		for k in range(m): 
			setOfPoints[k] = float(setOfPoints[k])
		if i < midPoint: 
			centers.append(setOfPoints)
		elif i > midPoint: 
			points.append(setOfPoints)

	distance = squaredErrorDistortion(points, centers)
	print(round(distance,3))

if __name__ == "__main__":
	main()
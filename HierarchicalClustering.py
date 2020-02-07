def findAvgDistance(cluster1, cluster2, D):
	#print("CLUSTER1: ", cluster1)
	#print("CLUSTER2: ", cluster2)
	sumOfPoints = 0 
	totalVals = 0
	for point in cluster1: 
		numOfPoints = point.split('_')
		totalVals += len(numOfPoints)
		for point2 in cluster2:
			sumOfPoints += D[(point, point2)] * len(numOfPoints)

	#find the number of values in cluster 1
	avgDistance = sumOfPoints/totalVals
	#print("AVG DISTANCE: ", avgDistance)
	return avgDistance

def hierarchicalClustering(D, n):
	clusters = [] 
	T = {} 
	for i in range(1,n+1): 
		T[str(i)] = [str(i)] 

	while len(T.keys()) > 1: 
		mindist = 999999
		cluster1 = ''
		cluster2 = ''
		for key in T.keys(): 
			for key2 in T.keys(): 
				if key != key2: 
					distance = findAvgDistance(T[key], T[key2], D)
					if distance < mindist: 
						mindist = distance
						cluster1 = key
						cluster2 = key2

		#print("MINDIST: ", mindist)
		Cnew = cluster1 + '_' + cluster2
		T[Cnew] = [cluster1]
		T[Cnew].append(cluster2)
		#T[Cnew] =  cluster + '_' + cluster2
		#print(T[Cnew])
		T.pop(cluster1, None)
		T.pop(cluster2, None)
		#use previous values to calculate new distances 
		for theKey in T.keys(): 
			if theKey!=Cnew: 
				D[(cluster1 + '_' + cluster2, theKey)] = findAvgDistance(T[Cnew], T[theKey], D)
				D[(theKey, cluster1 + '_' + cluster2)] = findAvgDistance(T[Cnew], T[theKey], D)
				#print("CLUSTER1: ", T[theKey])
				#print("CLUSTER2: ", T[Cnew])
				#print("AVG DIST: ", D[(cluster1 + '_' + cluster2, theKey)])
		#print(D)
				

		T[Cnew] =  [cluster1 + '_' + cluster2]
		clusters.append(T[Cnew])
		#remove the values from the dictionary 
		for key in D.keys(): 
			if cluster1 in key: 
				D.pop(key, None)
			if cluster2 in key: 
				D.pop(key, None)

	return clusters


def main():
	with open('rosalind_ba8e.txt', 'r') as myfile:
		data = myfile.readlines()
	
	n = int(data[0].rstrip('\n'))
	D = {} 
	for i in range(1, len(data)):
		string = data[i].rstrip('\n')
		setOfPoints = string.split() 
		for j in range(1, n+1):
			D[(str(i), str(j))] = float(setOfPoints[j-1])

	#print(D)
	clusters = hierarchicalClustering(D, n)
	for cluster in clusters: 
		cluster = cluster[0].split('_')
		newStr = cluster[0]
		for i in range(1, len(cluster)):
			newStr += ' ' + cluster[i]
		print(newStr)

if __name__ == "__main__":
	main()


import numpy as np 

def kNearestNeighbors(data,predict,k,d):
	euclidean = np.sum(np.linalg.norm(data[:,0:3] - predict,axis=1),axis=1)
	indices = euclidean.argsort()[:k]
	delta = 0
	denominator = 0
	for index in indices:
		delta += ( data[index,3] - data[index,2] )*( d - euclidean[index] )
		denominator += d - euclidean[index]
	
	delta /= denominator 

	return delta

def parseDataForKNN(dataset, look_back=4):
	finalData = []
	for i in range(len(dataset)-look_back-1):
		temp = dataset[i:(i+look_back)]
		finalData.append(temp)
	return np.array(finalData)
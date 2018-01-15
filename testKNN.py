#################### Import Section of the code #############################

librarynames = [('sys','sys'), ('numpy','np'),('Loadfile','Loadfile'), 
								('os','os'), ('plot','plot') , ('knn','knn'),
								('showFrames','showFrames')]

for (library,lib) in librarynames:
	try:
		library = __import__(library)
	except Exception as e:
		print(e,"\nPlease Install the package or Check for the file.")
		sys.exit()
	else:
		globals()[lib] = library

#################### Import Section ends here ################################


################ Main function to test Kalman Filter #########################
def main():
	#Generate training data
	objectname = "Van"
	objectid = "0"
	trainingFilename = "0000"
	objectfullname = objectname + objectid
	coordinates,_ = Loadfile.getData(trainingFilename)
	trainingCoordinates =knn.parseDataForKNN(coordinates.get(objectfullname))
	# trainingCoordinates = np.array(trainingCoordinates)

	# #Generate test data
	objectname = "Cyclist"
	objectid = "1"
	testingFilename = "0000"
	objectfullname = objectname + objectid
	coordinates, imagepath = Loadfile.getData(testingFilename)
	testingCoordinates = knn.parseDataForKNN(coordinates.get(objectfullname))
	testingCoordinates = np.array(testingCoordinates)
	trueCoordinates = testingCoordinates[:,3]
	imagePath = imagepath.get(objectfullname)
	
	#Actual KNN predictions
	predictedCoordinate = []
	for testCoordinates in testingCoordinates:
		predicted = testCoordinates[2] + \
				knn.kNearestNeighbors(trainingCoordinates,
												   testCoordinates[0:3],10,11)

		Xp = int(np.ceil(predicted[0])); Yp = int(np.ceil(predicted[1]))
		predictedCoordinate.append([Xp,Yp])
	
	# print(predictedCoordinate - trueCoordinates)
	predictedCoordinate = np.array(predictedCoordinate) 
	trueCoordinates = np.array(trueCoordinates)
	error = np.linalg.norm(predictedCoordinate - trueCoordinates,axis=1)**2
	MeanSquareError = 10*np.log10(np.mean(error))
	print("Mean Square Error : ", MeanSquareError)
	showFrames.showFrames(imagePath,predictedCoordinate,trueCoordinates,
													'K-Nearest-Neighbor', 3)
	plot.plotPredictions(trueCoordinates,predictedCoordinate,
														'K-Nearest-Neighbor')
	plot.plotError(error,'K-Nearest-Neighbor')
	np.save()

###################### Main function ends here ##############################

if __name__ == '__main__':
	try:
		main()
	except Exception as e:
		raise e
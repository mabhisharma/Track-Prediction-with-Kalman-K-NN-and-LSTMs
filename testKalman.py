#################### Import Section of the code #############################

librarynames = [('sys', 'sys'), ('numpy','np'), ('kalmanFilter', 'kalman'),
				    ('Loadfile','Loadfile'), ('os','os'), ('plot','plot') ,
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
	coordinates,imagepath = Loadfile.getData("0000")
	objectname = "Cyclist"
	objectid = "1"
	objectfullname = objectname + objectid
	trueCoordinates = np.matrix(coordinates.get(objectfullname))
	imagePath = imagepath.get(objectfullname)
	predicted = []
	KF = kalman.KalmanFilter(dt=1,method="Accerelation")
	for index in range(len(trueCoordinates)):
		Xp,_,Yp,_ = np.array(KF.predict())
		predicted.append([Xp,Yp])
		Xc = trueCoordinates[index,0]
		Yc = trueCoordinates[index,1]
		KF.correct([[Xc],[Yc]])
		
	predicted = np.matrix(predicted)
	error = np.linalg.norm(trueCoordinates - predicted,axis=1)**2
	MeanSquareError = 10*np.log10(np.mean(error[10:]))
	print("Mean Square Error : ", MeanSquareError)
	showFrames.showFrames(imagePath,predicted,trueCoordinates, "Kalman Filter")

	plot.plotPredictions(trueCoordinates,predicted,'Kalman Filter')
	plot.plotError(error[10:],'Kalman Filter')

###################### Main function ends here ##############################

if __name__ == '__main__':
	try:
		main()
	except Exception as e:
		raise e
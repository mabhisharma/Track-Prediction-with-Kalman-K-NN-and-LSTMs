# #################### Import Section of the code ###########################

import Loadfile
import numpy as np  
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
import showFrames
from LSTM import lstmModel
import plot

# #################### Import Section ends here #############################

######################## Helper Functions  ##################################

def getData(startfile, endfile, objectname, objectid, scaler):
	Xc, Yc, imagePath = [], [], []
	for i in range(startfile, endfile+1):
		filename = str(format(int(i), '04d'))
		coordinates,imagepath = Loadfile.getData(filename)
		objectfullname = objectname + objectid
		trueCoordinates = np.matrix(coordinates.get(objectfullname))
		imagePath.append(imagepath.get(objectfullname))
		if trueCoordinates.any():
			for index in range(len(trueCoordinates)):
				Xc.append(trueCoordinates[index,0]) 
				Yc.append(trueCoordinates[index,1]) 

	X, Y = np.array(Xc).reshape(-1,1), np.array(Yc).reshape(-1,1)
	data = np.hstack((X,Y))
	data = scaler.fit_transform(data)
	return data, np.array(imagePath).flatten()

def create_dataset(dataset, look_back=3):
	dataX, dataY = [], []
	for i in range(len(dataset)-look_back-1):
		a = dataset[i:(i+look_back)]
		dataX.append(a)
		dataY.append(dataset[i + look_back])

	data_input, data_output = np.array(dataX), np.array(dataY)

	return data_input, data_output


################## Helper Functions ends here ###############################


def main(training=True, saveModel=True):

	# Generate training and testing data and normalise it.
	scaler = MinMaxScaler(feature_range=(0, 1))
	training_data, training_imagepath = getData(0, 0, "Van", "0", scaler)
	training_input, training_ouput = create_dataset(training_data)
	testing_data, testing_imagepath = getData(0, 0, "Cyclist", "1", scaler) 
	testing_input, testing_output = create_dataset(testing_data)
	modelfilename  = "model2.yaml"
	weightfilename = "model2.h5"


	if training == True:
		# Create a RNN model with LSTM cells.
		# Hidden units of a single LSTM cell
		hidden_unit = 32
		Model = lstmModel(True, (training_input, training_ouput), 
																hidden_unit)
		Model.compileModel(loss='mae', optimizer='adam')
		Model.fitModel()
		print("Trainig Complete")

		if saveModel:
			Model.saveModel(modelfilename, weightfilename)
	
	else :
		Model = lstmModel(training=False)
		Model.loadModel(modelfilename, weightfilename)
		predictions = Model.prediction(testing_input)
		predictions = scaler.inverse_transform(predictions)
		truevalues = scaler.inverse_transform(testing_output)
		error = np.linalg.norm(predictions - truevalues,axis=1)**2
		MeanSquareError = 10*np.log10(np.mean(error))
		print("Mean Square Error : ", MeanSquareError)
		showFrames.showFrames(testing_imagepath,predictions,truevalues, 
																	"LSTM",3)
		plot.plotPredictions(truevalues,predictions,'LSTM')
		plot.plotError(error,'LSTM')

if __name__ == '__main__':
	try:
		main(training=False, saveModel=False)
	except Exception as e:
		print(e)
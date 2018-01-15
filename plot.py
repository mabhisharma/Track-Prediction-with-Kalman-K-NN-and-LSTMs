import matplotlib.pyplot as plt

def plotPredictions(actual,predicted,method):
	plt.figure()
	plt.plot(actual[:,0],actual[:,1],'+',label='Actual data')
	plt.plot(predicted[:,0],predicted[:,1],'*',label= method+ ' Prediction')
	plt.legend()
	plt.title('Actual vs. ' + method + ' Predicted', fontweight='bold')
	plt.xlabel('X-Coordinates')
	plt.ylabel('Y-Coordinates')
	plt.show(block=True)

def plotError(error,method):
	plt.figure()
	plt.plot(error,'+-',label=method +'Error')
	plt.legend()
	plt.title('Error while using ' + method, fontweight='bold')
	plt.xlabel('X-Coordinates')
	plt.ylabel('Y-Coordinates')
	plt.show(block=True)
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.models import model_from_yaml


#################### LSTM Class Section starts here  #########################

class lstmModel(object):
	"""docstring for LSTM"""
	def __init__(self, training=True, training_data=[], hidden_units=32):
		
		super(lstmModel, self).__init__()
		if training:
			self.training_input, self.training_output = training_data
			print((self.training_input.shape[1], self.training_input.shape[2]))
			self.model = Sequential()
			
			self.model.add(LSTM(hidden_units, input_shape=(
					self.training_input.shape[1], self.training_input.shape[2])))
			
			self.model.add(Dense(self.training_output.shape[1]))


	def compileModel(self, loss, optimizer):
		self.model.compile(loss=loss, optimizer=optimizer)

	def fitModel(self, epochs=300, batch_size=2):
		self.model.fit(self.training_input, self.training_output, epochs=epochs,
														  batch_size=batch_size, 
														  verbose=2, 
														  shuffle=False)

	def prediction(self, data):
		return self.model.predict(data)

	def saveModel(self, modelfilename, weightfilename):
		model_yaml = self.model.to_yaml()
		with open(modelfilename, "w") as yaml_file:
		    yaml_file.write(model_yaml)

		self.model.save_weights(weightfilename)
		print("Saved model to disk")

	def loadModel(self, modelfilename, weightfilename):
		yaml_file = open(modelfilename, 'r')
		loaded_model = yaml_file.read()
		yaml_file.close()
		model = model_from_yaml(loaded_model)
		self.model = model
		model.load_weights(weightfilename)
		print("Loaded model from disk")

#################### LSTM Class Section ends here   #########################
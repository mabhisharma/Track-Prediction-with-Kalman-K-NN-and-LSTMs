#################### Import Section of the code #############################
librarynames = [('sys','sys'), ('collections', 'collections'), 
								 ('configparser','configparser'),('os','os')]

for (library,lib) in librarynames:
	try:
		library = __import__(library)
	except Exception as e:
		print(e,"\nPlease Install the package or Check for the file.")
		sys.exit()
	else:
		globals()[lib] = library

#################### Import Section ends here ################################



def getData(filename):
	config = configparser.ConfigParser()
	config.read('config')
	trainingLabelsDirectory = config.get('trainingLabelsDirectory','path')
	testingLabelsDirectory  = config.get('testingLabelsDirectory', 'path')
	trainingImageDirectory  = config.get('trainingImageDirectory', 'path')
	testingImageDirectory   = config.get('testingImageDirectory',  'path')

	coordinates = collections.defaultdict(list)
	imagepath = collections.defaultdict(list)
	file = open(os.path.join(trainingLabelsDirectory,filename+".txt"),"r")
	for line in file.readlines():
		values = line.strip().split(' ')
		if values[2] != 'DontCare':
			object_name = str(values[2]) + str(values[1])
			frameid = str(format(int(values[0]), '06d'))
			X = int((float(values[6])+float(values[8]))/2)
			Y = int((float(values[7])+float(values[9]))/2)
			coordinates[object_name].append([X,Y])
			imagepath[object_name].append(os.path.join(trainingImageDirectory, filename, frameid + ".png"))

	return coordinates, imagepath


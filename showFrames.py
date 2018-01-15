import cv2
import time
import numpy as np 

def createimage(w,h):
	size = (w, h, 1)
	img = np.ones((w,h,3),np.uint8)*255
	return img

def showFrames(filenames,predicted,actual,method,buffer=0,sleeptime=0):
	fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
	out = cv2.VideoWriter(method+".avi", fourcc, 10.0, (1242, 375))

	for index in range(len(predicted)):
		img = cv2.imread(filenames[index+buffer],1)
		cv2.circle(img,(int(predicted[index,0]),int(predicted[index,1])),
														  5,(255,0,0),-1)
		
		cv2.circle(img,(int(actual[index,0]),int(actual[index,1])),5,
															(0,255,0),-1)
		
		cv2.putText(img, method, (0,20),0, 0.7, (0,255,255),2)
		cv2.putText(img,"Frame Number : " + str(index), (0,40),0, 0.7, 
															 (0,0,255),2)
		
		cv2.putText(img,"Predicted : Blue", (0,60),0, 0.7, (255,0,0),2)
		cv2.putText(img,"Actual : Green" , (0,80),0, 0.7, (0,255,0),2)
		cv2.imshow('image',img)
		out.write(img)
		if index == 123:
			cv2.imwrite(method + '.png',img)
		time.sleep(sleeptime)
		
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	
	out.release()
	cv2.destroyAllWindows()

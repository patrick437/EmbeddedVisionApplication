#!/usr/bin/python3

import cv2
from  picamera2 import Picamera2
import time


def createCamera():
	picam = Picamera2()
	picam.configure(picam.create_preview_configuration(main={"format":"XRGB8888","size": (640,480)}))
	picam.start()
	time.sleep(2) #Allow camera time to warm up
	return picam

def captureImageArrays(picam):
	im = picam.capture_array()
	grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
	return im

def iterateThroughData(im):

	print( len(im) )
	

	
def main():
	cv2.startWindowThread()#start threading in the main loop rather thenn the function

	picam1 = createCamera()
	picam2 = createCamera()

	while True:
		im1 = captureImageArrays(picam1)
		im2 = captureImageArrays(picam2)

		cv2.imshow("Camera", im1)
		cv2.imshow("Camera2", im2)	

		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	picam1.stop()
	picam2.stop()	
	cv2.destroyAllWindows()

if __name__ == "__main__":
	main()
	
	
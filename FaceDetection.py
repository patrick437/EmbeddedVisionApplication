#!/usr/bin/python3

import cv2
from  picamera2 import Picamera2


def createCamera():
	cv2.startWindowThread()

	picam2 = Picamera2()
	picam2.configure(picam2.create_preview_configuration(main={"format":"XRGB8888","size": (640,480)}))
	picam2.start()
	return picam2
	


def captureImageArrays(picam2):
	im = picam2.capture_array()
	grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
	return im

def iterateThroughData(im):

	print( len(im) )

	
def main():
	
	picam2 = createCamera()

	im = captureImageArrays(picam2)

	cv2.imshow("Camera", im)
	cv2.waitKey()
	
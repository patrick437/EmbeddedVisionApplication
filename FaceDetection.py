#!/usr/bin/python3

import cv2
from  picamera2 import Picamera2


def createCamera():
	cv2.startWindowThread()
	picam = Picamera2()
	picam.configure(picam.create_preview_configuration(main={"format":"XRGB8888","size": (640,480)}))
	picam.start()
	return picam

def captureImageArrays(picam):
	im = picam.capture_array()
	grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
	return im

def iterateThroughData(im):

	print( len(im) )
	

	
def main():
	
	picam1 = createCamera()
	picam2 = createCamera()
	im1 = captureImageArrays(picam1)
	im2 = captureImageArrays(picam2)

	cv2.imshow("Camera", im1)
	cv2.imshow("Camera2", im2)	
	cv2.waitKey()
	
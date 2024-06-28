#!/usr/bin/python3

import cv2
from  picamera2 import Picamera2


def createCamera():
	cv2.startWindowThread()

	picam1 = Picamera2()
	picam2 = Picamera2()

	picam2.configure(picam1.create_preview_configuration(main={"format":"XRGB8888","size": (640,480)}))
	picam2.configure(picam2.create_preview_configuration(main={"format":"XRGB8888","size": (640,480)}))

	picam1.start()
	picam2.start()

	return picam1, picam2

def captureImageArrays(picam1, picam2):
	im1 = picam1.capture_array()
	im2 = picam2.capture_array()

	grey1 = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
	grey2 = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)

	return im1, im2

def iterateThroughData(im1, im2):

	print( len(im1) )
	print( len(im2) )

	
def main():
	
	picam1, picam2 = createCamera()

	im1, im2 = captureImageArrays(picam1, picam2)

	cv2.imshow("Camera", im1)
	cv2.imshow("Camera2", im2)	
	cv2.waitKey()
	
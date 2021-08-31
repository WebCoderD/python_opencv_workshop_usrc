"New python file opening a photo of a lasagna that I made recently"
import cv2
import numpy

#read image
las = cv2.imread('Photos/lasagna.JPG')
cv2.imshow('lasagna', las)

cv2.waitKey(0)

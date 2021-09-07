"""
Shape Finding of pentagon .
"""

import cv2
import numpy as np

frame = cv2.imread ('..\Photos/collage.png')
edges = cv2.Canny(frame,100,200) # This uses the canny edge detector. The 100 and 200 are rather arbitrary parameters; the second should be larger than the first, play around to see what numbers work best for each image.


# Load another pentagon from a template
pentagon = cv2.imread('..\Photos\pentagon.png')
pentagonCanny = cv2.Canny(pentagon,100,200) #make a canny
pentagonContours, hierarchy = cv2.findContours(pentagonCanny,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE) #find the contours of our pentagon image
#hierarchy denotes which contours are parents and the children of those parent contours

pentagonBlank = np.zeros(pentagon.shape)
cv2.polylines(pentagonBlank,pentagonContours,True,(255),1)
# Find its contours and create a moment set for checking

pentagonMoments = cv2.moments(pentagonContours[1]) #moment is average of intensities, which allows us to get the center of a contour
pentagonHuMoments= cv2.HuMoments(pentagonMoments)

print("pentagonHuMoments:\n",pentagonHuMoments,"\n")

contours, hierarchy = cv2.findContours(edges,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
# Get rid of the ones with an area smaller than tiny

blankImage = np.zeros(edges.shape)

goodContours=[]
for contour in contours:
    if cv2.contourArea(contour)>100:
        contourMoments = cv2.moments(contour)
        contourHuMoments = cv2.HuMoments(contourMoments)
        #find the difference between moments
        delta = np.sum(pentagonHuMoments-contourHuMoments)
        if (np.abs(delta)<0.002): #0.002 is our threshold
            goodContours.append(contour)
            cv2.polylines(blankImage,contour,True,(255),1)

#cv2.imshow("original", frame)
cv2.imshow("pentagon", pentagonBlank)
cv2.imshow("pentagonContour", pentagonCanny)
cv2.imshow("edges", edges) 
cv2.imshow("good contours", blankImage) 
cv2.waitKey(-1)



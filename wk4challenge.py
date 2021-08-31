#challenge 1.1 
import cv2

las = cv2.imread('..\Photos\lasagna.JPG')
cv2.imshow('lasagna', las)

init_width=int(las.shape[1])
init_height=int(las.shape[0])
init_dimensions = (init_width,init_height)

width=int(las.shape[1]*0.5)
height=int(las.shape[0]*0.5)
dimensions = (width,height)

lasagna_new_size = cv2.resize(las,dimensions,interpolation =cv2.INTER_AREA)

cv2.imshow('lasagna different size', lasagna_new_size)

lined = cv2.line(lasagna_new_size,(0,0),(250,250),(255,255,0),thickness=2)
cv2.imshow('Line',lined)

greyscale=cv2.cvtColor(las,cv2.COLOR_BGR2GRAY)
cv2.imshow('Grey',greyscale)

blur=cv2.GaussianBlur(las,(9,9),cv2.BORDER_DEFAULT)
cv2.imshow('Blur',blur)

canny=cv2.Canny(las,125,200)
cv2.imshow('Canny',canny)

rotPoint=(width//2,height//2)
rotMat = cv2.getRotationMatrix2D(rotPoint,45,scale=1.0)

las_rotate = cv2.warpAffine(las,rotMat,init_dimensions)
cv2.imshow('lasagna rotated', las_rotate)

cv2.waitKey(0)
cv2.destroyAllWindows()
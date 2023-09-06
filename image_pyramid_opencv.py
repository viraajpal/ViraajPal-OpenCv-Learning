# the correct code i had make it as comment and what i have error in my code it is mentioned below
'''import cv2
import numpy as np

img = cv2.imread('img_25.png')
layer = img.copy()
gp = [layer]

for i in range(6):
    layer = cv2.pyrDown(layer)
    gp.append(layer)

layer = gp[5]
cv2.imshow('upper level Gaussian Pyramid', layer)
lp = [layer]

for i in range(5, 0, -1):
    gaussian_extended = cv2.pyrUp(gp[i])
    gaussian_extended = cv2.resize(gaussian_extended, gp[i-1].shape[:2][::-1])
    laplacian = cv2.subtract(gp[i-1], gaussian_extended)
    cv2.imshow(str(i), laplacian)

cv2.imshow("original image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()'''


import cv2
import numpy as np

img = cv2.imread('img_25.png')
layer = img.copy()
gp = [layer]
#lr1 = cv2.pyrDown(img)
#lr2 = cv2.pyrDown(img)
for i in range(6):
    layer = cv2.pyrDown(layer)
    gp.append(layer)
    #cv2.imshow(str(i), layer)

layer = gp[5]
cv2.imshow('upper level Gaussian Pyramid', layer)
lp =[layer]

for i in range(5, 0, -1):
    gaussian_extended = cv2.pyrUp(gp[i])
    laplacian = cv2.substract(gp[i-1], gaussian_extended)
    cv2.imshow(str(i), laplacian)

#hr2 = cv2.pyrUp(lr2)
#cv2.imshow("original image", img)
#cv2.imshow('pyrDown 1 image', lr1)
#cv2.imshow('pyrDown 2 image', lr2)
#cv2.imshow('pyrUp 1 image', hr2)
# LAPLACIAN PYRAMID
# GAUSSIAN PYRAMID

cv2.imshow("original image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

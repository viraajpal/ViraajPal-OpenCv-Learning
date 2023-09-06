import numpy as np
'''import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('img_1.png')

#img = np.zeros((200, 200), np.uint8)
#cv.rectangle(img, (0, 100), (200, 200), (255), -1)
#cv.rectangle(img, (0, 50), (100, 100), (127), -1)
#b, g, r = cv.split(img)
hist = cv.calcHist(([img], [0], None), [256], [0, 256])
plt.plot(hist)

#cv.imshow('img', img)
#cv.imshow('b', b)
#cv.imshow('g', g)
#cv.imshow('r', r)

#plt.hist(b.ravel(), 256, [0, 256])
#plt.hist(g.ravel(), 256, [0, 256])
#plt.hist(r.ravel(), 256, [0, 256])
plt.show()
cv.waitKey(0)
cv.destroyAllWindows()'''


import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('img_1.png')

# Check if the image was loaded successfully
if img is None:
    print("Error: Failed to load the image file.")
    exit()

# Convert the image to grayscale
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Calculate the histogram
hist = cv.calcHist([gray_img], [0], None, [256], [0, 256])

# Plot the histogram
plt.plot(hist)

# Display the image and histogram
cv.imshow('img', img)
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()

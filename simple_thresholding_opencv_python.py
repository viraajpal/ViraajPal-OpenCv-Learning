import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the image
image = cv2.imread('gradient.png', 0)  # 0 means grayscale mode

# Apply thresholding
threshold_value = 128  # Adjust this value according to your needs
max_value = 255  # Maximum value assigned to pixels exceeding the threshold
_, thresholded_image = cv2.threshold(image, threshold_value, max_value, cv2.THRESH_BINARY)
_, thresholded_image_1 = cv2.threshold(image, threshold_value, max_value, cv2.THRESH_BINARY_INV)

titles = ['Original image', 'BINARY', 'BINARY_INV']
images = [image, thresholded_image, thresholded_image_1]

for i in range(3):
    plt.subplot(1, 3, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()








# Display the original and thresholded images
#cv2.imshow('Original Image', image)
#cv2.imshow('Thresholded Image', thresholded_image)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

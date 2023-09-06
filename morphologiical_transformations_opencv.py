import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('img_2.png', cv2.IMREAD_GRAYSCALE)  # Make sure to provide the correct file extension
_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)
titles = ['image', 'mask']  # Add 'mask' to the titles list
images = [img, mask]  # Add 'mask' to the images list

for i in range(2):
    plt.subplot(1, 2, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()
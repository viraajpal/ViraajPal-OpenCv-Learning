import cv2
import numpy as np

# Load the orange and apple images
orange = cv2.imread('img_3.png')
apple = cv2.imread('img_4.png')

# Resize the images to have the same dimensions
orange_resized = cv2.resize(orange, (apple.shape[1], apple.shape[0]))

# Generate the Gaussian pyramid for the orange image
orange_copy = orange_resized.copy()
orange_pyramid = [orange_copy]
for i in range(6):
    orange_copy = cv2.pyrDown(orange_copy)
    orange_pyramid.append(orange_copy)

# Generate the Gaussian pyramid for the apple image
apple_copy = apple.copy()
apple_pyramid = [apple_copy]
for i in range(6):
    apple_copy = cv2.pyrDown(apple_copy)
    apple_pyramid.append(apple_copy)

# Generate the Laplacian pyramid for the orange image
orange_pyramid_up = [orange_pyramid[5]]
for i in range(5, 0, -1):
    gaussian_expanded = cv2.pyrUp(orange_pyramid[i])
    laplacian = cv2.subtract(orange_pyramid[i - 1], cv2.resize(gaussian_expanded, orange_pyramid[i - 1].shape[:2][::-1]))
    orange_pyramid_up.append(laplacian)

# Generate the Laplacian pyramid for the apple image
apple_pyramid_up = [apple_pyramid[5]]
for i in range(5, 0, -1):
    gaussian_expanded = cv2.pyrUp(apple_pyramid[i])
    laplacian = cv2.subtract(apple_pyramid[i - 1], cv2.resize(gaussian_expanded, apple_pyramid[i - 1].shape[:2][::-1]))
    apple_pyramid_up.append(laplacian)

# Blend the images at each level of the pyramids
blended_pyramid = []
for orange_lap, apple_lap in zip(orange_pyramid_up, apple_pyramid_up):
    cols, rows, ch = orange_lap.shape
    blended = np.hstack((orange_lap[:, :cols // 2], apple_lap[:, cols // 2:]))
    blended_pyramid.append(blended)

# Reconstruct the blended image
blended_reconstruct = blended_pyramid[0]
for i in range(1, 6):
    blended_reconstruct = cv2.pyrUp(blended_reconstruct)
    blended_reconstruct = cv2.add(blended_pyramid[i], blended_reconstruct)

# Display the images
cv2.imshow('Orange', orange)
cv2.imshow('Apple', apple)
cv2.imshow('Blended', blended_reconstruct)
cv2.waitKey(0)
cv2.destroyAllWindows()

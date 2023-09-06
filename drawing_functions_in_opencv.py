import numpy as np
import cv2

img = np.zeros([512, 512, 3], np.uint8)
img = cv2.line(img, (0, 0), (255, 255), (0, 0, 255), 10)
img = cv2.line(img, (0, 255), (255, 255), (0, 255, 0), 10)
img = cv2.rectangle(img, (487, 89), (456, 123), (0, 0, 255), 10)
img = cv2.circle(img, (447, 0), 67, (0, 255, 0), -1)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV', (10, 500), font, 4, (0, 255, 255), 10, cv2.LINE_AA)

cv2.imshow('image', img)

cv2.waitKey(0)

cv2.destroyAllWindows()

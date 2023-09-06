import cv2

img = cv2.imread('somu.png', -1)

print(img)

cv2.imshow('image', img)

k = cv2.waitKey(50000) & 0xFF

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.destroyAllWindows()
    cv2.imwrite('img_abc.jpg', img)
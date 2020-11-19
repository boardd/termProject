import cv2
import numpy as np

img = cv2.imread("testImage.jpeg")
print(img.shape)
imgResized = cv2.resize(img, (1680,1050))
cv2.imshow("Test Image", imgResized)

cv2.waitKey(0)
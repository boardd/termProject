import cv2
import numpy as np


# img = cv2.imread("resources/alanhsu.jpg")
# print(img)
# print("==================================")

def crop(img, x1, y1, x2, y2):
    croppedImg = img[y1:y2,x1:x2]
    return croppedImg

# output = crop(img, 100, 100, 200, 200)
# print(output)
# # cv2.imshow("src", img)
# # cv2.imshow("output", output)

# # cv2.waitKey(0)
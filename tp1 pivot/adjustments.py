import cv2
import numpy as np
import time

# img = cv2.imread("resources/alanhsu.jpg")
# print(img)
# print("==================================")
def increaseSat(img):
    resultImg = np.zeros((img.shape)).astype(np.uint8)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    for row in range(img.shape[0]):
        for col in range(img.shape[1]):
            hue = img[row][col][0]
            sat = img[row][col][1]
            val = img[row][col][2]
            sat += 10
            if sat > 255:
                sat = 255
            resultImg[row][col][0] = hue
            resultImg[row][col][1] = sat
            resultImg[row][col][2] = val
    resultImg = cv2.cvtColor(resultImg, cv2.COLOR_HSV2BGR)
    return resultImg

def decreaseSat(img):
    resultImg = np.zeros((img.shape)).astype(np.uint8)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    for row in range(img.shape[0]):
        for col in range(img.shape[1]):
            hue = img[row][col][0]
            sat = img[row][col][1]
            val = img[row][col][2]
            sat -= 10
            if sat < 0:
                sat = 0
            resultImg[row][col][0] = hue
            resultImg[row][col][1] = sat
            resultImg[row][col][2] = val
    resultImg = cv2.cvtColor(resultImg, cv2.COLOR_HSV2BGR)
    return resultImg

def increaseContrast(img):
    resultImg = np.zeros(img.shape).astype(np.uint8)
    alpha = 1.1
    for row in range(img.shape[0]):
        for col in range(img.shape[1]):
            for value in range(img.shape[2]):
                newValue =  alpha * img[row][col][value] 
                if newValue > 255:
                    newValue = 255
                resultImg[row][col][value] = newValue
    return resultImg.astype(np.uint8)

def decreaseContrast(img):
    resultImg = np.zeros(img.shape).astype(np.uint8)
    alpha = 0.9
    for row in range(img.shape[0]):
        for col in range(img.shape[1]):
            for value in range(img.shape[2]):
                newValue =  alpha * img[row][col][value] 
                resultImg[row][col][value] = newValue
    return resultImg.astype(np.uint8)

def increaseBrightness(img):
    resultImg = np.zeros(img.shape).astype(np.uint8)
    beta = 10
    for row in range(img.shape[0]):
        for col in range(img.shape[1]):
            for value in range(img.shape[2]):
                newValue =  img[row][col][value] + beta
                if newValue > 255:
                    newValue = 255
                resultImg[row][col][value] = newValue
    return resultImg.astype(np.uint8)

def decreaseBrightness(img):
    resultImg = np.zeros(img.shape).astype(np.uint8)
    beta = -10
    for row in range(img.shape[0]):
        for col in range(img.shape[1]):
            for value in range(img.shape[2]):
                newValue =  img[row][col][value] + beta
                if newValue < 0:
                    newValue = 0
                resultImg[row][col][value] = newValue
    return resultImg.astype(np.uint8)


# output = increaseContrast(img)
# cv2.imshow("src", img)
# cv2.imshow("output", output)

# cv2.waitKey(0)
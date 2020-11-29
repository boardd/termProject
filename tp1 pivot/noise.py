#bilateral filter
import cv2
import numpy as np
from blurs import *

img = cv2.imread("resources/img4.jpg")

def bilateral(img, weight = 1 , kernelSize = 3, isGaussian = False, variance=1):
    kernel = np.ones((kernelSize, kernelSize), np.float32)
    if len(img.shape) != 3:
        grey = True
    else:
        grey = False
    if isGaussian:
        total = 0
        for row in range(kernelSize):
            newRow = row - kernelSize // 2
            for col in range(kernelSize):
                newCol = col - kernelSize // 2
                kernel[row][col] = gaussianModel(newCol, newRow, variance)
                total += kernel[row][col]
        for row in range(kernelSize):
            for col in range(kernelSize):
                kernel[row][col] /= total
    kernelOffset = kernelSize // 2
    directions = sorted([i * -1 for i in range(kernelSize // 2 + 1)] + [i for i in range(1,kernelSize//2 + 1)])
    if not grey:
        redChannel = np.array(img[:,:,2])
        greenChannel = np.array(img[:,:,1])
        blueChannel = np.array(img[:,:,0])
        allChannels = (blueChannel, greenChannel, redChannel)
        temp = (np.zeros(allChannels[0].shape), np.zeros(allChannels[0].shape),np.zeros(allChannels[0].shape))
    else:
        allChannels = [img]
        temp = np.zeros(img.shape)
    for i, channel in enumerate(allChannels):
        for row in range(channel.shape[0]):
            for col in range(channel.shape[1]):
                count = 0
                result = 0
                for drow in directions:
                    for dcol in directions:
                        newRow = row + drow
                        newCol = col + dcol
                        if ((0 <= newRow < channel.shape[0]) and
                            (0 <= newCol < channel.shape[1])):
                                count += 1
                                srcValue = channel[row][col]
                                newValue = channel[newRow][newCol]
                                difference = abs(newValue - srcValue)
                                if difference == 0:
                                    difference = 1
                                constant = (kernel[drow + kernelOffset][dcol + kernelOffset]) * (weight*(1/difference))
                                result += (channel[newRow][newCol] * constant)
                if not isGaussian:
                    value = result / count
                else:
                    value = result
                if not grey:
                    temp[i][row][col] = round(value) 
                else:
                    temp[row][col] = round(value)   
    if not grey:
        fullImage = np.dstack(temp).astype(np.uint8)
        return fullImage
    return temp

output1 = bilateral(img, True, 1)
cv2.imshow("output1", output1)
cv2.imshow("reference", img)
cv2.waitKey(0)
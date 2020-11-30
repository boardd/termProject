from cmu_112_graphics import *
import os
import cv2
import numpy as np
import math
from blurs import *
    
def edgeDetection(img, selected, scale = 0.15):
    ogImg = img
    if len(img.shape) != 3: grey = True
    else: grey = False
    img = blur(img,3, True, 1)
    laplacianFilter = np.array([[ 0, 0,-1, 0, 0],
                                [ 0,-1,-2,-1, 0],
                                [-1,-2,17,-2,-1],
                                [ 0,-1,-2,-1, 0],
                                [ 0, 0,-1, 0, 0]])
    basicFilter = np.array([[-1,-1,-1],
                            [-1,9,-1],
                            [-1,-1,-1]])
    doublePrimeFilter = np.array([[0,1,0],
                                [1,-4,1],
                                [0,1,0]])
    if selected == "laplacian":
        kernel = laplacianFilter * -1
    elif selected == "basic":
        kernel = basicFilter
    elif selected == "doublePrime":
        kernel = doublePrimeFilter
    kernelSize = kernel.shape[0]
    kernelOffset = kernelSize // 2
    directions = sorted([i * -1 for i in range( kernelSize // 2 + 1)] + [i for i in range(1, kernelSize // 2 + 1)])
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
                result = 0
                for drow in directions:
                    for dcol in directions:
                        newRow = row + drow
                        newCol = col + dcol
                        if ((0 <= newRow < channel.shape[0]) and
                            (0 <= newCol < channel.shape[1])):
                                constant = kernel[drow + kernelOffset][dcol + kernelOffset]
                                result += (channel[newRow][newCol] * constant)
                value = result
                if value < 0:
                    value = 0
                elif value > 255:
                    value = 255
                if not grey:
                    temp[i][row][col] = round(value)
                else:
                    temp[row][col] = round(value)
    if not grey:
        fullImage = np.dstack(temp)
    else:
        fullImage = temp
    # newFullImage = (fullImage * scale).astype(np.uint8)
    # resultImg = np.add(ogImg, newFullImage)
    return fullImage

def unSharpen(img, scale = 0.1):
    ogImg = img
    img = blur(img, 5, True, 1)
    img = cv2.bitwise_not(img)
    img = (img * scale).astype(np.uint8)
    output = np.add(ogImg, img)
    return output

# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# output  = sharpen2(img, 0.1)
# cv2.imshow("source", img)
# cv2.imshow("output", output)
# output1, newoutput1 = sharpen(img, "laplacian", 0.15)
# # img = medianFilter(img, 3)
# output2 = cv2.filter2D(img, -1, np.array([[ 0, 0,-1, 0, 0],
#                                 [ 0,-1,-2,-1, 0],
#                                 [-1,-2,16,-2,-1],
#                                 [ 0,-1,-2,-1, 0],
#                                 [ 0, 0,-1, 0, 0]]) )
# newoutput2 = np.add(img, (output2*0.15).astype(np.uint8))
# cv2.imshow("original", img)
# cv2.imshow("my code", newoutput1)
# cv2.imshow("my filtered", output1)
# cv2.imshow("reference filtered", output2)
# cv2.imshow("reference", newoutput2)
# cv2.waitKey(0)

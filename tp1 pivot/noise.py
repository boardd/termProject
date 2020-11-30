#bilateral filter
import cv2
import numpy as np
from blurs import *

# img = cv2.imread("resources/img6.jpg")

def gaussianModel(dist,variance):
    return (1/(2*math.pi*(variance**2)))*math.exp((-(dist**2))/(2*(variance**2)))

def bilateral(img, kernelSize = 3, sigS = 1, sigR = 1):
    kernel = np.ones((kernelSize, kernelSize), np.float32)
    if len(img.shape) != 3:
        grey = True
    else:
        grey = False
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
                                srcValue = channel[row][col]
                                newValue = channel[newRow][newCol]
                                difference = abs(int(newValue) - int(srcValue))
                                distance = ((newCol - col )**2 + (newRow - row)**2)**0.5
                                # print(difference)
                                weight = (gaussianModel(distance, sigS) * gaussianModel(difference, sigR))
                                result += (channel[newRow][newCol] * weight)
                                count += weight
                value = result / count
                # print(value)
                if not grey:
                    temp[i][row][col] = round(value) 
                else:
                    temp[row][col] = round(value)   
    if not grey:
        fullImage = np.dstack(temp).astype(np.uint8)
        return fullImage
    return temp.astype(np.uint8)

# # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# output1 = bilateral(img, 3, 50, 25)
# print(output1 == img)
# # output2 = blur(img, 3, True, 1)
# cv2.imshow("output1", output1)
# # cv2.imshow("output2", output2)
# cv2.imshow("reference", img)
# cv2.waitKey(0)
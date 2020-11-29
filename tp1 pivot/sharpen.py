import cv2
import numpy as np

img = cv2.imread("resources/img4.jpg")

def medianFilter(img, kernelSize):
    kernel = np.ones((kernelSize, kernelSize), np.float32)
    kernelOffset = kernelSize // 2
    directions = sorted([i * -1 for i in range(kernelSize // 2 + 1)] + [i for i in range(1,kernelSize//2 + 1)])
    redChannel = np.array(img[:,:,2])
    greenChannel = np.array(img[:,:,1])
    blueChannel = np.array(img[:,:,0])
    allChannels = (blueChannel, greenChannel, redChannel)
    temp = (np.zeros(allChannels[0].shape), np.zeros(allChannels[0].shape),np.zeros(allChannels[0].shape))
    for i, channel in enumerate(allChannels):
        for row in range(channel.shape[0]):
            for col in range(channel.shape[1]):
                result = []
                for drow in directions:
                    for dcol in directions:
                        newRow = row + drow
                        newCol = col + dcol
                        if ((0 <= newRow < channel.shape[0]) and
                            (0 <= newCol < channel.shape[1])):
                                result.append(channel[newRow][newCol])
                value = sorted(result)[len(result) // 2]
                temp[i][row][col] = round(value)
    fullImage = np.dstack(temp).astype(np.uint8)
    return fullImage
    
# somethings wrong with laplacian filter
def sharpen(img, selected, scale = 0.15):
    ogImg = img
    # img = medianFilter(img,3)
    laplacianFilter = np.array([[ 0, 0,-1, 0, 0],
                                [ 0,-1,-2,-1, 0],
                                [-1,-2,17,-2,-1],
                                [ 0,-1,-2,-1, 0],
                                [ 0, 0,-1, 0, 0]])
    basicFilter = np.array([[-1,-1,-1],
                            [-1,9,-1],
                            [-1,-1,-1]])
    if selected == "laplacian":
        kernel = laplacianFilter * -1
    elif selected == "basic":
        kernel = basicFilter
    kernelSize = kernel.shape[0]
    kernelOffset = kernelSize // 2
    directions = sorted([i * -1 for i in range( kernelSize // 2 + 1)] + [i for i in range(1, kernelSize // 2 + 1)])
    redChannel = np.array(img[:,:,2])
    greenChannel = np.array(img[:,:,1])
    blueChannel = np.array(img[:,:,0])
    allChannels = (blueChannel, greenChannel, redChannel)
    temp = (np.zeros(allChannels[0].shape), np.zeros(allChannels[0].shape),np.zeros(allChannels[0].shape))
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
                temp[i][row][col] = round(value)
    fullImage = np.dstack(temp)
    newFullImage = (fullImage * scale).astype(np.uint8)
    resultImg = np.add(ogImg, newFullImage)
    return fullImage

output1 = sharpen(img, "laplacian", 0.15)
# img = medianFilter(img, 3)
output2 = cv2.filter2D(img, -1, np.array([[ 0, 0,-1, 0, 0],
                                [ 0,-1,-2,-1, 0],
                                [-1,-2,16,-2,-1],
                                [ 0,-1,-2,-1, 0],
                                [ 0, 0,-1, 0, 0]]) )
# print(output1)
print('@@@@@@@@@@@@@@@@')
print(output2)
# print(output1 == output2)
output2 = np.add(img, (output2*0.15).astype(np.uint8))
cv2.imshow("og", img)
cv2.imshow("yay", output1)
cv2.imshow("ref", output2)
cv2.waitKey(0)

# name/text detection
from cmu_112_graphics import *
from PIL import ImageTk
from PIL import Image
import numpy as np
import imutils
from imutils.video import FileVideoStream
from imutils.video import FPS
import cv2
import mss
import time
import pytesseract

# demo
'''
opencv
pytesseract
mss
pillow
pandas
numpy
imutils
cmu112 graphics
'''

# constants 
blue = (255,0,0) # BGR not RGB
green = (0, 255, 0)
red = (0,0,255)

scale = 3
upperLimit = int(210/scale)
lowerLimit = int(60/scale)


# tess data is stored at "/usr/local/share/tessdata"

pytesseract.pytesseract.tesseract_cmd = r"/Users/tony/tesseract/build/tesseract"
img = cv2.imread("resources/testImg7.png")
hsvImg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
rgbImg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

def placeholder(x):
    pass
cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars", 400, 800)
cv2.createTrackbar("MIN HUE", "Trackbars", 0, 179, placeholder) # 30
cv2.createTrackbar("MAX HUE", "Trackbars", 95, 179, placeholder) # 63
cv2.createTrackbar("MIN SAT", "Trackbars", 0, 255, placeholder) # 82
cv2.createTrackbar("MAX SAT", "Trackbars", 0, 255, placeholder) # 160
cv2.createTrackbar("MIN VAL", "Trackbars", 133, 255, placeholder) # 176
cv2.createTrackbar("MAX VAL", "Trackbars", 255, 255, placeholder) # 255

while True:

    ### get color of words
    minH = cv2.getTrackbarPos("MIN HUE","Trackbars") 
    maxH = cv2.getTrackbarPos("MAX HUE","Trackbars") 
    minS = cv2.getTrackbarPos("MIN SAT","Trackbars") 
    maxS = cv2.getTrackbarPos("MAX SAT","Trackbars") 
    minV = cv2.getTrackbarPos("MIN VAL","Trackbars") 
    maxV = cv2.getTrackbarPos("MAX VAL","Trackbars") 
    # minH = 0
    # maxH = 95
    # minS = 0
    # maxS = 0
    # minV = 133
    # maxV = 255
    lower = np.array([minH,minS,minV])
    upper = np.array([maxH,maxS,maxV])
    mask = cv2.inRange(hsvImg, lower, upper)
    # mask = cv2.bitwise_not(mask)
    blurMaskImg = cv2.GaussianBlur(mask,(7,7),0.5)
    cannyMaskImg = cv2.Canny(blurMaskImg, 50, 50)
    cv2.imshow("mask", cannyMaskImg)
    
    data  = pytesseract.image_to_data(cannyMaskImg)
    for index, row in enumerate(data.splitlines()):
        if index == 0:
            continue
        wordData = row.split()
        if len(wordData) == 12:
            x, y, w, h = int(wordData[6]),int(wordData[7]),int(wordData[8]),int(wordData[9])
            cv2.rectangle(img,(x,y),(x+w,y+h), (0,0,255), 3)

    cv2.imshow("result",img)
    time.sleep(1)
    cv2.waitKey(1)

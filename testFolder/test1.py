import cv2
import numpy as np
from PIL import ImageGrab
import mss
import time

# constants 
blue = (255,0,0) # BGR not RGB
green = (0, 255, 0)
red = (0,0,255)

scale = 3
upperLimit = int(210/scale)
lowerLimit = int(60/scale)


#images
source1 = "testImg.jpeg"
source2 = "testImg2.png"
source3 = "testImg3.png"
source4 = "testImg4.png"
source5 = "testImg5.png"
source6 = "testImg6.png"

# image preprocessing
img = cv2.imread(source4)
dimensions = img.shape
img = cv2.resize(img, (int(dimensions[1]/scale),int(dimensions[0]/scale)))
greyImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
hsvImg = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)


# trackbar
'''
def placeholder(x):
    pass
cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars", 400, 800)
cv2.createTrackbar("MIN HUE", "Trackbars", 30, 179, placeholder) # 30
cv2.createTrackbar("MAX HUE", "Trackbars", 63, 179, placeholder) # 63
cv2.createTrackbar("MIN SAT", "Trackbars", 82, 255, placeholder) # 82
cv2.createTrackbar("MAX SAT", "Trackbars", 160, 255, placeholder) # 160
cv2.createTrackbar("MIN VAL", "Trackbars", 176, 255, placeholder) # 176
cv2.createTrackbar("MAX VAL", "Trackbars", 255, 255, placeholder) # 255
'''

### get speaker rectangle
# minH = cv2.getTrackbarPos("MIN HUE","Trackbars") 
# maxH = cv2.getTrackbarPos("MAX HUE","Trackbars") 
# minS = cv2.getTrackbarPos("MIN SAT","Trackbars") 
# maxS = cv2.getTrackbarPos("MAX SAT","Trackbars") 
# minV = cv2.getTrackbarPos("MIN VAL","Trackbars") 
# maxV = cv2.getTrackbarPos("MAX VAL","Trackbars") 
minH = 30
maxH = 63
minS = 82
maxS = 160
minV = 176
maxV = 255

# create mask
lower = np.array([minH,minS,minV])
upper = np.array([maxH,maxS,maxV])
mask = cv2.inRange(hsvImg, lower, upper)
speakerImg = cv2.bitwise_and(img, img, mask = mask)

# get contours
def getContours(img):
    areaThresh = 10000
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > areaThresh:
            cv2.drawContours(resultImg, cnt, -1, red, 2)
            perimeter = cv2.arcLength(cnt, True)
            points = cv2.approxPolyDP(cnt, 0.02 * perimeter, True)
            (x1, y1) = points[0][0]
            (x2, y2) = points[2][0]
            print(x1, y1, x2, y2)
            cv2.circle(resultImg, (x1,y1), 4, blue, -1) # (x,y), radius, color, thickness (-1 means fill)
            cv2.circle(resultImg, (x2,y2), 4, blue, -1)

greySpeakerImg = cv2.cvtColor(speakerImg,cv2.COLOR_BGR2GRAY)
blurSpeakerImg = cv2.GaussianBlur(greySpeakerImg,(7,7),0.5)
cannySpeakerImg = cv2.Canny(blurSpeakerImg, 50, 50)

resultImg = img.copy()
getContours(cannySpeakerImg)

# get faces
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
faces = faceCascade.detectMultiScale(greyImg, scaleFactor=1.1, minNeighbors=2)
for rec in faces:
    x, y, width, height = rec
    if lowerLimit < width < upperLimit:
        cv2.putText(resultImg, f"size, {width}", (x,y-10), fontFace = cv2.FONT_HERSHEY_PLAIN, fontScale = 1, color = green)
        cv2.rectangle(resultImg, (x,y), (x+width,y+height), color = green, thickness = 1)

#show images
cv2.imshow("view", resultImg)
# cv2.imshow("hsv", hsvImg)
# cv2.imshow("mask", mask)
# cv2.imshow("speaker", speakerImage)
# cv2.imshow("canny", cannySpeakerImg)


# if cv2.waitKey(1) and 0xFF == ord("q"):
#     break


# cv2.imshow("view", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
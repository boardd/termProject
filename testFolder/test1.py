import cv2
import numpy as np

# BGR not RGB
blue = (255,0,0)
green = (0, 255, 0)
red = (0,0,255)

#images
source1 = "testImg.jpeg"
source2 = "testImg2.png"
source3 = "testImg3.png"
source4 = "testImg4.png"

# image preprocessing
img = cv2.imread(source1)
dimensions = img.shape
img = cv2.resize(img, (int(dimensions[1]/3),int(dimensions[0]/3)))
greyImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# face detection code
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
faces = faceCascade.detectMultiScale(greyImg, scaleFactor=1.2, minNeighbors=3)
for rec in faces:
    x, y, w, h = rec
    cv2.putText(img, "Face", (x,y-10), fontFace = cv2.FONT_HERSHEY_PLAIN, fontScale = 1, color = green)
    cv2.rectangle(img, (x,y), (x+w,y+h), color = green, thickness = 1)

cv2.imshow("view", img)
cv2.waitKey(0)
import cv2
import numpy as np

# BGR not RGB
blue = (255,0,0)
green = (0, 255, 0)
red = (0,0,255)


# image preprocessing
frameWidth = 720
frameHeight = 480
cap = cv2.VideoCapture(0)
# width
cap.set(3,frameWidth)
# height
cap.set(4,frameHeight)
# brightness
cap.set(10,100)

# face detection code
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:
    success, frame = cap.read()
    greyFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(greyFrame, scaleFactor=1.1, minNeighbors=2)
    for rec in faces:
        x, y, w, h = rec
        cv2.putText((frame), "Face", (x,y-10), fontFace = cv2.FONT_HERSHEY_PLAIN, fontScale = 1, color = green)
        cv2.rectangle(frame, (x,y), (x+w,y+h), color = red, thickness = 1)
    
    cv2.imshow("webcam", frame)

    if cv2.waitKey(1) and 0xFF == ord("q"):
        break

video_capture.release()
cv2.destroyAllWindows()
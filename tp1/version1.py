from cmu_112_graphics import *
from PIL import ImageTk
from PIL import Image
import numpy as np
import cv2
import mss
import time
import pandas
import pytesseract
import string

def initConstants(app):
    pytesseract.pytesseract.tesseract_cmd = r"C:\Users\tonyt\AppData\Local\Tesseract-OCR\tesseract.exe" 
    app.faceCascade = cv2.CascadeClassifier("C:/Users/tonyt/Desktop/termProject/tp1/resources/haarcascade_frontalface_default.xml")
    app.cols = 4
    app.rows = 3
    app.blue = (255, 0, 0)
    app.green = (0, 255, 0)
    app.red = (0, 0, 255)
    app.scale = 0.8
    # face size limits
    # app.faceUpperLim = 
    # app.faceLowerLim = 
    # rectangle mask
    app.recLevels = {"minH":26, "maxH":79,
                        "minS":84,"maxS":231,
                        "minV":134,"maxV":255 }
    app.recLower = np.array([app.recLevels["minH"], app.recLevels["minS"], app.recLevels["minV"]])
    app.recUpper = np.array([app.recLevels["maxH"], app.recLevels["maxS"], app.recLevels["maxV"]])
    # word mask
    app.wordMaskLevels = {"minH":118, "maxH":179,
                        "minS":0,"maxS":31,
                        "minV":108,"maxV":255 }
    app.wordLower = np.array([app.wordMaskLevels["minH"], app.wordMaskLevels["minS"], app.wordMaskLevels["minV"]])
    app.wordUpper = np.array([app.wordMaskLevels["maxH"], app.wordMaskLevels["maxS"], app.wordMaskLevels["maxV"]])
    # people list
    app.people = {"sara", "liang", "tony", "tao", "karen", "li", "michael", "crotty", "kobe", "zhang",
                    "meng", "oi", "james", "chen", "jordan", "stephen", "dai", "kruthi", "thangali", "srinualnad", 
                    "ravi", "patel"}
    app.detected = set()
    # trackbars
    def placeholder(x):
        pass
    # cv2.namedWindow("Trackbars")
    # cv2.resizeWindow("Trackbars", 400, 800)
    # cv2.createTrackbar("MIN HUE", "Trackbars", 0, 179, placeholder) # 30
    # cv2.createTrackbar("MAX HUE", "Trackbars", 179,179, placeholder) # 63
    # cv2.createTrackbar("MIN SAT", "Trackbars", 0, 255, placeholder) # 82
    # cv2.createTrackbar("MAX SAT", "Trackbars", 61, 255, placeholder) # 160
    # cv2.createTrackbar("MIN VAL", "Trackbars", 185, 255, placeholder) # 176
    # cv2.createTrackbar("MAX VAL", "Trackbars", 255, 255, placeholder) # 255
    # 0, 179, 0, 61, 185, 255
    # cv2.createTrackbar("thresh1", "Trackbars", 0, 300, placeholder) # 176
    # cv2.createTrackbar("thresh2", "Trackbars", 0, 300, placeholder) # 255


def preProcess(app, frame):
    app.img = frame
    # app.dimensions = app.img.shape
    app.img = cv2.resize(app.img, (int(1920*app.scale), int(1080*app.scale)))
    # app.scaledImg = cv2.resize(app.img, (int(1920*2), int(1080*2)))
    # app.scaledHsv = cv2.cvtColor(app.scaledImg, cv2.COLOR_BGR2HSV)
    app.hsvImg = cv2.cvtColor(app.img, cv2.COLOR_BGR2HSV)
    app.greyImg = cv2.cvtColor(app.img, cv2.COLOR_BGR2GRAY)
    app.rgbImg = cv2.cvtColor(app.img, cv2.COLOR_BGR2RGB)
    app.resultImg = app.img.copy()
    # detection stuff
    # masks
    app.recMask = cv2.inRange(app.hsvImg, app.recLower, app.recUpper)
    # detect the rectangle
    speakerImg = cv2.bitwise_and(app.img, app.img, mask = app.recMask)
    greySpeakerImg = cv2.cvtColor(speakerImg, cv2.COLOR_BGR2GRAY)
    blurSpeakerImg = cv2.GaussianBlur(greySpeakerImg,(7,7),0.5)
    app.cannySpeakerImg = cv2.Canny(blurSpeakerImg, 50, 50)
    # detect the words
    # app.blurWordMask = cv2.GaussianBlur(app.wordMask, (5,5),0.1)
    # app.blurMask = cv2.GaussianBlur(app.img, (5,5), 0.1)
    

def appStarted(app):
    initConstants(app)
    app.running = False
    app.count = 0
    cv2.setUseOptimized(True)
    print(cv2.useOptimized())
    # app.timerDelay = 100

def keyPressed(app,event):
    if event.key == "r":
        app.running = not app.running

def getRectangle(app):
    areaThresh =  ((2200**0.5)*app.scale)**2 # threshold for the speaker rectangle
    contours, hierarchy = cv2.findContours(app.cannySpeakerImg, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > areaThresh:
            cv2.drawContours(app.resultImg, cnt, -1, app.red, 2)
            perimeter = cv2.arcLength(cnt, True)
            points = cv2.approxPolyDP(cnt, 0.02 * perimeter, True)
            (x1, y1) = points[0][0]
            (x2, y2) = points[2][0]
            cv2.circle(app.resultImg, (x1,y1), 4, app.blue, -1) # (x,y), radius, color, thickness (-1 means fill)
            cv2.circle(app.resultImg, (x2,y2), 4, app.blue, -1)

def getFaces(app):
    faces = app.faceCascade.detectMultiScale(app.greyImg, scaleFactor=1.1, minNeighbors=3)
    for rec in faces:
        x, y, width, height = rec
        if 40*app.scale < width < 100*app.scale:
            cv2.putText(app.resultImg, f"size, {width}", (x,y-10), fontFace = cv2.FONT_HERSHEY_PLAIN, fontScale = 3, color = app.green, thickness=2)
            cv2.rectangle(app.resultImg, (x,y), (x+width,y+height), color = app.green, thickness = 2)

def getWords(app):
    for r in range(app.rows):
        for c in range(app.cols):
            x1 = 107 + 330*c
            x2 = x1 + 114 # width of name label
            y1 = 285 + 189*r
            y2 = y1 + 17
            app.cropped = app.img[y1:y2,x1:x2]
            app.cropped = cv2.cvtColor(app.cropped, cv2.COLOR_BGR2GRAY)
            laplacianFilter = np.array([[0,0,-1,0,0],
                                [0,-1,-2,-1,0],
                                [-1,-2,16,-2,-1],
                                [0,-1,-2,-1,0],
                                [0,0,-1,0,0]])
            sharpenFilter = np.array([[-1,-1,-1],
                                    [-1,9,-1],
                                    [-1,-1,-1] ])
            app.cropped = cv2.resize(app.cropped, (0,0), fx = 3, fy = 3)
            app.cropped = cv2.GaussianBlur(app.cropped, (7,7), 1.5)
            app.cropped = cv2.filter2D(app.cropped, -1, laplacianFilter)
            app.newCropped = cv2.addWeighted(app.cropped, 5, np.zeros(app.cropped.shape, app.cropped.dtype), 0, 2) # alpha, gamma, beta
            # app.cannyCropped = cv2.Canny(app.cropped, app.thresh1, app.thresh2)
            dataTable = pytesseract.image_to_data(app.cropped)
            for index, row in enumerate(dataTable.splitlines()):
                if index == 0:
                    continue
                wordData = row.split()
                if wordData[-1].isalpha() and len(wordData) == 12:
                    x, y, w, h, word = int(wordData[6]),int(wordData[7]),int(wordData[8]),int(wordData[9]), wordData[11]
                    # print(word)
                    if word.strip().lower() in app.people:
                        app.detected.add(word)
                        cv2.putText(app.resultImg, f"{word}", (x1, y1 - 20),fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale = 2, color=app.red, thickness=3)
                        cv2.rectangle(app.resultImg,(x1,y1),(x1+w,y1+h), app.red, 3)

def runProgram(app):
    with mss.mss() as sct:
        # app.count += 1
        # print(f"running...{app.count}")
        frame = np.array(sct.grab(sct.monitors[2]))
        preProcess(app, frame)
        e1 = cv2.getTickCount()
        getRectangle(app)
        # getFaces(app)
        # minH = cv2.getTrackbarPos("MIN HUE","Trackbars")
        # maxH = cv2.getTrackbarPos("MAX HUE","Trackbars")
        # minS = cv2.getTrackbarPos("MIN SAT","Trackbars")
        # maxS = cv2.getTrackbarPos("MAX SAT","Trackbars")
        # minV = cv2.getTrackbarPos("MIN VAL","Trackbars")
        # maxV = cv2.getTrackbarPos("MAX VAL","Trackbars")
        # app.wordLower = np.array([minH,minS,minV])
        # app.wordUpper = np.array([maxH,maxS,maxV])
      
        # cv2.imshow("app", app.cannySpeakerImg)
        getWords(app)
        cv2.imshow("app", app.resultImg)
        # cv2.imshow("app2", app.newCropped)
        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            app.running = False
        e2 = cv2.getTickCount()
        time = (e2 - e1)/ cv2.getTickFrequency()
        print(time)
    
def timerFired(app):
    if app.running:
        runProgram(app)


def redrawAll(app, canvas):
    canvas.create_text(app.width/2, 220, text = "Press R to run app")


runApp(width = 400, height = 400) 

from cmu_112_graphics import *
from PIL import ImageTk
from PIL import Image
import numpy as np
import imutils
from imutils.video import FileVideoStream
import cv2
import mss
import time
import pytesseract

def initConstants(app):
    app.blue = (255, 0, 0)
    app.green = (0, 255, 0)
    app.red = (0, 0, 255)
    app.scale = 3
    app.faceUpperLim = int(210/app.scale)
    app.faceLowerLim = int(60/app.scale)
    app.faceMaskLevels = {"minH":30, "maxH":63,
                        "minS":82,"maxS":160,
                        "minV":176,"maxV":255 }
    app.wordMaskLevels = {"minH":0, "maxH":95,
                        "minS":0,"maxS":0,
                        "minV":133,"maxV":255 }


def processFiles(app):
    app.img = cv2.imread("resources/testImg7.png")
    vidDir = "resources/video3.mov"
    app.fvs = FileVideoStream(vidDir)
    time.sleep(1.0)
    # detection stuff
    pytesseract.pytesseract.tesseract_cmd = r"/Users/tony/tesseract/build/tesseract" 
    app.faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    app.faceLower = np.array([app.faceMaskLevels["minH"], app.faceMaskLevels["minS"], app.faceMaskLevels["minV"]])
    app.faceUpper = np.array([app.faceMaskLevels["maxH"], app.faceMaskLevels["maxS"], app.faceMaskLevels["maxV"]])
    app.wordLower = np.array([app.wordMaskLevels["minH"], app.wordMaskLevels["minS"], app.wordMaskLevels["minV"]])
    app.wordUpper = np.array([app.wordMaskLevels["maxH"], app.wordMaskLevels["maxS"], app.wordMaskLevels["maxV"]])

def appStarted(app):
    initConstants(app)
    processFiles(app)
    app.show = False

def keyPressed(app,event):
    if event.key == "s":
        app.show = not app.show

def getRectangle(app):
    pass

def getFaces(app):
    faces = app.faceCascade.detectMultiScale(app.greyImg, scaleFactor=1.1, minNeighbors=2)
    for rec in faces:
        x, y, width, height = rec
        if app.faceLowerLim < width < app.faceUpperLim:
            cv2.putText(app.resultImg, f"size, {width}", (x,y-10), fontFace = cv2.FONT_HERSHEY_PLAIN, fontScale = 1, color = app.green)
            cv2.rectangle(app.resultImg, (x,y), (x+width,y+height), color = app.green, thickness = 1)

def timerFired(app):
    if app.show:
        while app.fvs.more():
            app.img = app.fvs.read()
            app.dimensions = app.img.shape
            app.img = cv2.resize(app.img, (int(dimensions[1]/app.scale), int(dimensions[0]/app.scale)))
            app.hsvImg = cv2.cvtColor(app.img, cv2.COLOR_BGR2HSV)
            app.rgbImg = cv2.cvtColor(app.img, cv2.COLOR_BGR2RGB)
            app.greyImg = cv2.cvtColor(app.img, cv2.COLOR_BGR2GRAY)
            app.resultImg = app.img.copy()
            ###
            app.faceMask = cv2.inRange(app.hsvImg, app.faceLower, app.faceUpper)
            app.wordMask = cv2.inRange(app.hsvImg, app.wordLower, app.wordUpper)
            speakerImg = cv2.bitwise_and(app.img, app.img, mask = app.wordMask)
            cv2.imshow('video', app.resultImg)
            cv2.waitKey(1)


def redrawAll(app, canvas):
    canvas.create_text(app.width/2, 10, text ="Press S to show")


runApp(width = 720, height = 480) 

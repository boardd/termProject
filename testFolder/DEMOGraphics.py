from cmu_112_graphics import *
from PIL import ImageTk
from PIL import Image
import numpy as np
import imutils
from imutils.video import FileVideoStream
import cv2
import mss
import time


def loadVideo(app):
    vidDir = "resources/video3.mov"
    app.fvs  = FileVideoStream(vidDir).start()
    # app.timerDelay = 1

def appStarted(app):
    app.play = False
    app.counter = 0
    loadVideo(app)
    app.imageList = []
    while app.fvs.more():
        frame = app.fvs.read()
        frame = imutils.resize(frame, width=app.width)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(frame)
        image = ImageTk.PhotoImage(image)
        app.imageList.append(image)
    timerFired(app)


def keyPressed(app,event):
    app.play = True

def timerFired(app):
    app.image = app.imageList[app.counter % len(app.imageList)]
    app.counter += 1
    print(f"running {app.counter}")


def redrawAll(app, canvas):

    canvas.create_image(app.width/2, app.height/2, image=app.image)
    canvas.create_text(100,100, text=f"Queue Size: {app.fvs.Q.qsize()}", fill = "white")

runApp(width = 1080, height = 720)
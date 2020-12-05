from cmu_112_graphics import *
from blurs import *
from noise import *
from sharpen import *
from interface import *
from button import *
from adjustments import *
from menu import *
import os
import cv2
import math
import numpy as nps

def appStarted(app):
    app.started = False
    initUI(app)
    app.timerDelay = 100
    app.actions = []

def mousePressed(app, event):
    mX, mY = event.x, event.y
    if app.uploadB.click(mX, mY):
        openFileDialog(app)
    if app.started:
        if app.saveB.click(mX, mY):
            saveFileDialog(app)
        if app.loaded:
            for b in app.buttons:
                if app.actions == []:
                    app.actions = b.menuClick(mX, mY)
                    print(app.actions)
                # if b.click(mX, mY) and app.loaded:
                #     app.imgArray = b.function(app.imgArray)
                #     scaleImg(app)

def mouseMoved(app, event):
    mX, mY = event.x, event.y
    app.uploadB.hover(mX,mY)
    if app.started:
        app.saveB.hover(mX, mY)
        for b in app.buttons:
            b.hover(mX, mY)

def doAction(app):
    if app.actions != []:
        print("did the thing")
        action = app.actions[0]
        typ = app.actions[1].lower()
        try:
            kernel = float(app.actions[2])
            sigma = int(app.actions [3])
            speed = app.actions[4].lower()
        except:
            pass
        if action == "BLUR":
            kernel = int(kernel)
            if typ == "gaussian":
                if speed == "fast":
                    app.imgArray = cv2.GaussianBlur(app.imgArray, (kernel, kernel), sigma)
                elif speed == "slow":
                    app.imgArray = blur(app.imgArray, kernel, True, sigma)
            elif typ == "median":
                if speed == "fast":
                    app.imgArray = cv2.medianBlur(app.imgArray, (kernel, kernel))
                elif speed == "slow":
                    app.imgArray = medianBlur(app.imgArray, kernel)
            elif typ  == "average":
                if speed == "fast":
                    app.imgArray = cv2.blur(app.imgArray, (kernel, kernel))
                elif speed == "slow":
                    app.imgArray = blur(app.imgArray, kernel, False)
        elif action == "SHARPEN": 
            if typ == "laplacian":
                app.imgArray = fastSharpen(app.imgArray, "laplacian", kernel) #kernel represents scale here
            elif typ == "basic1":
                app.imgArray = fastSharpen(app.imgArray, "basic1", kernel)
            elif typ == "unsharpen":
                app.imgArray = unSharpen(app.imgArray)
            elif typ == "basic2":
                app.imgArray = fastSharpen(app.imgArray, "basic2", kernel)
            elif typ == "double prime":
                app.imgArray = fastSharpen(app.imgArray, "doublePrime", kernel)
        elif action == "DENOISE":
            kernel = int(kernel)
            if typ == "bilateral":
                if speed == "fast":
                    app.imgArray = cv2.bilateralFilter(app.imgArray, kernel, sigma, sigma)
                elif speed == "slow":
                    app.imgArray = bilateral(app.imgArray, kernel, sigma, sigma)
        elif action == "COLOR":
            if typ == "+":
                app.imgArray = increaseSat(app.imgArray)
            elif typ == "-":
                app.imgArray = decreaseSat(app.imgArray)
        elif action == "BRIGHTNESS":
            if typ == "+":
                app.imgArray = increaseBrightness(app.imgArray)
            elif typ == "-":
                app.imgArray = decreaseBrightness(app.imgArray)
        elif action == "CONTRAST":
            if typ == "+":
                app.imgArray = increaseContrast(app.imgArray)
            elif typ == "-":
                app.imgArray = decreaseContrast(app.imgArray)
        scaleImg(app)
        app.actions = []

def timerFired(app):
    if app.started:
        updateImg(app)
        doAction(app)


def keyPressed(app, event):
    key = event.key
    # skips the beginning screen
    if  key == "s":
        app.loadedImg = Image.open("resources/alanhsu.jpg")
        app.imgArray = np.array(app.loadedImg)
        app.scale = None
        scaleImg(app)
        app.started = True
        app.loaded = True
        app.uploadB.x = 20
        app.uploadB.y = 20
        app.uploadB.h = 40
    if app.loaded:
        for b in app.buttons:
            b.menuInput(key)

def redrawAll(app, canvas):
    drawUIBase(app,canvas)
    drawImage(app, canvas)
    drawUI(app, canvas)

runApp(width = 1380, height = 720)

# references
# https://www.youtube.com/watch?v=1THuCOKNn6U
# https://web.stanford.edu/class/cs448f/lectures/2.1/Denoising.pdf
# https://web.stanford.edu/class/cs448f/lectures/2.1/Sharpening.pdf
# https://web.stanford.edu/class/cs448f/lectures/2.2/Fast%20Filtering.pdf
# https://eeweb.engineering.nyu.edu/~yao/EE3414/image_filtering.pdf
# https://docs.opencv.org/master/d4/d13/tutorial_py_filtering.html
# https://computersciencesource.wordpress.com/2010/09/03/computer-vision-the-integral-image/
# https://users.itk.ppke.hu/kep/Lectures/IPA_02_Convolution.pdf
# https://www.youtube.com/watch?v=rFWnRT2iqKg
# http://people.csail.mit.edu/sparis/siggraph07_course/course_notes.pdf

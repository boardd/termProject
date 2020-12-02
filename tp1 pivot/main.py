from cmu_112_graphics import *
from blurs import *
from noise import *
from sharpen import *
from interface import *
from button import *
from menu import *
import os
import cv2
import math
import numpy as np

def appStarted(app):
    app.started = False
    initUI(app)
    app.timerDelay = 100
    

def mousePressed(app, event):
    mX, mY = event.x, event.y
    if app.uploadB.click(mX, mY):
        openFileDialog(app)
    if app.started:
        if app.saveB.click(mX, mY):
            print("saved")
        if app.loaded:
            for b in app.buttons:
                b.menuClick(mX, mY)
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

def timerFired(app):
    if app.started:
        updateImg(app)

def keyPressed(app, event):
    # skips the beginning screen
    if event.key == "s":
        app.started = True
        app.loaded = True
        app.uploadB.x = 20
        app.uploadB.y = 20
        app.uploadB.h = 40

def redrawAll(app, canvas):
    drawUIBase(app,canvas)
    drawImage(app, canvas)
    drawUI(app, canvas)

runApp(width = 1380, height = 720)

# references
# https://www.youtube.com/watch?v=1THuCOKNn6U
# https://web.stanford.edu/class/cs448f/lectures/2.1/Denoising.pdf
# https://web.stanford.edu/class/cs448f/lectures/2.1/Sharpening.pdf
# https://eeweb.engineering.nyu.edu/~yao/EE3414/image_filtering.pdf
# https://docs.opencv.org/master/d4/d13/tutorial_py_filtering.html
# https://computersciencesource.wordpress.com/2010/09/03/computer-vision-the-integral-image/
# https://users.itk.ppke.hu/kep/Lectures/IPA_02_Convolution.pdf
# https://www.youtube.com/watch?v=rFWnRT2iqKg
# http://people.csail.mit.edu/sparis/siggraph07_course/course_notes.pdf

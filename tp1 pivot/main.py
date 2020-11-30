'''
core functions:

more complex
Gaussian Blur
sharpening algorithms
De-noising algorithms

less complex
Contrast Slider/adjuster
Brightness Slider/adjuster
Color channel/adjusters
image cropping of selected area

any additional functions:
healing brush
blur out faces
blur out text
blur out selected regions
'''
from cmu_112_graphics import *
from blurs import *
from noise import *
from sharpen import *
from interface import *
import os
import cv2
import numpy as np

def appStarted(app):
    initUI(app)

def mousePressed(app, event):
    mX, mY = event.x, event.y
    if app.uploadB.click(mX, mY):
        openFileDialog(app)

def mouseMoved(app, event):
    mX, mY = event.x, event.y
    app.uploadB.hover(mX,mY)

def timerFired(app):
    updateImg(app)

def keyPressed(app, event):
    pass

def redrawAll(app, canvas):
    drawUI(app,canvas)
    drawImage(app, canvas)

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

from cmu_112_graphics import *
from blurs import *
from noise import *
from sharpen import *
from interface import *
from button import *
import os
import cv2
import math
import numpy as np


def initUI(app):
    app.uploadB = button(20,20,160,60,"Browse Images")
    app.loaded = False
    app.scale = None
    app.uploadColor = "#CDCDCD"
    app.buttons = []
    createButtons(app)

def createButtons(app):
    text = ["BLUR", "SHARPEN", "DENOISE", "CROP", "FILTER", "COLOR", "CONTRAST", "BRIGHTNESS"]
    x, y, w, h, gap = 20,100, 80, 30, 50
    for i in range(8):
        app.buttons.append(button(x, y + (gap * i), w, h, text[i], i))

def openFileDialog(app):
    dialog = filedialog.askopenfilename(initialdir = os.getcwd(), title="Choose Image", 
                                    filetypes = (("JPG", "*.jpg"), ("PNG", "*.png"), ("All Files", "*.*")))
    try:
        app.loadedImg = Image.open(dialog)
        # app.loadedImg = Image.open("resources/img2.jpg")
        app.imgArray = np.array(app.loadedImg)
        app.scale = None
        scaleImg(app)
        app.loaded = True
    except:
        pass

def scaleImg(app):
    app.imgOldW, app.imgOldH = app.imgArray.shape[1], app.imgArray.shape[0]
    if app.scale == None:
        for scale in np.arange(0,10,0.01):
            app.imgNewW, app.imgNewH = int(app.imgOldW * scale), int(app.imgOldH * scale)
            if (app.imgNewW >= (app.width - 240) or
                app.imgNewH >= (app.height - 40)):
                app.scale = scale
                break
    app.imgDisplay = cv2.resize(app.imgArray, (app.imgNewW, app.imgNewH))
    app.imgShow = Image.fromarray(app.imgDisplay)

def updateImg(app):
    if app.loaded:
        app.imgShow = Image.fromarray(app.imgDisplay)

def drawImage(app, canvas):
    if app.loaded:
        r = 5
        canvas.create_image((app.width/2 )+ 100,app.height/2 , image = ImageTk.PhotoImage(app.imgShow))
        # canvas.create_oval((app.width/2 + 100) - r, (app.height/2) - r,
        #                     (app.width/2 + 100) + r, (app.height/2) + r, fill = "red")

def drawUI(app, canvas):
    # draw background
    canvas.create_rectangle(0,0, app.width, app.height, fill = "#CDCDCD", outline = "#CDCDCD")
    canvas.create_rectangle(0,0, 200, app.height, fill = "#696969", outline = "#696969")
    # draw buttons
    app.uploadB.draw(canvas, "Arial 16 bold")
    for b in app.buttons:
        b.draw(canvas, "Arial 12 bold")
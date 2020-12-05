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


def initUI(app):
    app.uploadB = button(app.width/2 - 80,app.height - 200,160,60,"Browse Images")
    app.saveB = button(20, 80, 160, 40, "Save Image")
    app.loaded = False
    app.scale = None
    app.darkGrey = "#212529"
    app.medGrey = "#495057"
    app.litGrey = "#ADB5BD"
    app.veryLitGrey = "#CED4DA"
    app.torq = "#40E0D0"
    app.buttons = []
    app.cropping = False
    createButtons(app)

def createButtons(app):
    print("ran")
    text = ["BLUR", "SHARPEN", "DENOISE", "CROP", "FILTER", "COLOR", "CONTRAST", "BRIGHTNESS"]
    sampleList = ["Type", "Kernel", "Sigma", "Speed"]
    blurList = ["Type", "Kernel", "Sigma", "Speed"]
    sharpenList = ["Type", "Scale"]
    fields = [blurList] + [sharpenList] +  [sampleList]* 6
    x, y, w, h, gap = 20, 140, 80, 30, 50
    for i in range(len(text)):
        app.buttons.append(button(x, y + (gap * i), w, h, text[i], i, fields[i]))

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
        app.started = True
        app.uploadB.x = 20
        app.uploadB.y = 20
        app.uploadB.h = 40
    except:
        pass

def saveFileDialog(app):
    filename = filedialog.asksaveasfile(mode='w', defaultextension=".jpg")
    if not filename:
        return
    app.imgShow.save(filename)

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

def drawUIBase(app, canvas):
    if app.started:
        # draw background
        canvas.create_rectangle(0,0, app.width, app.height, fill = app.darkGrey, outline = app.darkGrey)
        canvas.create_rectangle(0,0, 200, app.height, fill = app.medGrey, outline = app.medGrey)

def drawUI(app, canvas):
    if app.started:
        # draw buttons
        app.uploadB.draw(canvas, "Arial 16 bold")
        app.saveB.draw(canvas, "Arial 16 bold")

        for b in app.buttons:
            b.draw(canvas, "Arial 12 bold")
    else:
        canvas.create_rectangle(0,0, app.width, app.height, fill = app.darkGrey, outline = app.darkGrey)
        canvas.create_text(app.width/2, 0 + 300,text = "Darkroom", font = "Arial 180 bold", fill = app.veryLitGrey )
        app.uploadB.draw(canvas, "Arial 16 bold")
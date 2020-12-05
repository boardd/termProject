from cmu_112_graphics import *
from blurs import *
from noise import *
from sharpen import *
from interface import *
import os
import cv2
import math
import numpy as np

class menu:
    def __init__(self, x, y, fields = list()):
        self.x = x
        self.y = y
        self.w = 200
        self.h = (len(fields) + 1) * 30 
        self.light = "#CED4DA"
        self.dark = "#495057"
        self.color = self.light
        self.show = False
        self.f = fields
        self.done = False
        self.inputs = []
        self.createMenuInputs()
        self.createDoneButton()
    
    def createDoneButton(self):
        self.doneButton = doneButton(self.x + (self.w * 3/4), (self.y + self.h) - 30, 40, 20, text = "Done" )
    
    def createMenuInputs(self):
        count = 0
        for key in self.f:
            self.inputs.append(inputField(self.x + 100, self.y + (20 * count) + 10, 90, 20))
            count += 1
    
    def draw(self, canvas):
        if self.show:
            canvas.create_rectangle(self.x, self.y, self.x + self.w, self.y + self.h, fill = self.color, outline = self.color)
            self.drawText(canvas)
            for b in self.inputs:
                b.draw(canvas)
            self.doneButton.draw(canvas)

    def drawText(self, canvas):
        count = 0
        for key in self.f:
            count += 1
            canvas.create_text(self.x + 40, self.y + (20 * count), text = f"{key}", font = "Arial 12 bold", fill = self.dark)
            
    def hover(self, x, y):
        if ((self.x < x < self.x + self.w) and
            (self.y < y < self.y + self.h)):
            return True
        return False


class inputField():
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.text = "Click Here"
        self.clicked = False
        self.dark = "#495057"
        self.light = "#CED4DA"
        self.color = self.dark
        self.textColor = self.light

    def changeColor(self, color):
        self.color = color
        if color == self.light:
            self.textColor = self.dark
        else:
            self.textColor = self.light
    
    def draw(self, canvas, font=None):
        canvas.create_rectangle(self.x, self.y, self.x+self.w, self.y+self.h, fill = self.color, outline = self.dark)
        canvas.create_text((self.w/2 + self.x), (self.h/2 + self.y), text = self.text, font = font, fill = self.textColor)
    
    def hover(self, x, y):
        if ((self.x < x < self.x + self.w) and
            (self.y < y < self.y + self.h)):
            self.changeColor(self.light)
        else:
            self.changeColor(self.dark)
   
    def detectClick(self, x, y):
        if ((self.x < x < self.x + self.w) and
            (self.y < y < self.y + self.h)):
            self.clicked = True
            if self.text != "":
                self.text = ""
    
    def takeInput(self, key):
        if self.clicked == True:
            if key == "Enter":
                self.clicked = False
                return
            if key == "Delete":
                self.text = self.text[:-1]
            else:
                self.text += key
            print(self.text)

    def returnText(self):
        return self.text

class doneButton():
    def __init__(self, x, y, w, h, text = ""):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.text = text
        self.dark = "#495057"
        self.light = "#CED4DA"
        self.color = self.dark
        self.textColor = self.light
    
    def changeColor(self, color):
        self.color = color
        if color == self.light:
            self.textColor = self.dark
        else:
            self.textColor = self.light
    
    def draw(self, canvas, font=None):
        canvas.create_rectangle(self.x, self.y,self.x+self.w,self.y+self.h, fill = self.color, outline = self.color)
        if self.text != "":
            canvas.create_text((self.w/2 + self.x), (self.h/2 + self.y), text = self.text, font = font, fill = self.textColor)
    
    def hover(self, x, y):
        if ((self.x < x < self.x + self.w) and
            (self.y < y < self.y + self.h)):
            self.changeColor(self.light)
        else:
            self.changeColor(self.dark)

    def click(self, x, y):
        if ((self.x < x < self.x + self.w) and
            (self.y < y < self.y + self.h)):
            print("done")
            return True
        return False

from cmu_112_graphics import *
from blurs import *
from noise import *
from sharpen import *
from interface import *
import os
import cv2
import math
import numpy as np

class adjMenu:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 200
        self.h = 100
        self.light = "#CED4DA"
        self.dark = "#495057"
        self.color = self.light
        self.show = False
        self.done = False
        self.createAdjustmentButtons()
    
    def createAdjustmentButtons(self):
        self.minusButton = adjButton(self.x + 10, self.y + 30, text = "-" )
        self.plusButton= adjButton(self.x + 105, self.y + 30, text = "+" )
    
    def draw(self, canvas):
        if self.show:
            canvas.create_rectangle(self.x, self.y, self.x + self.w, self.y + self.h, fill = self.color, outline = self.color)
            self.minusButton.draw(canvas)
            self.plusButton.draw(canvas)

            
    def hover(self, x, y):
        if ((self.x < x < self.x + self.w) and
            (self.y < y < self.y + self.h)):
            return True
        return False

class adjButton():
    def __init__(self, x, y, text = ""):
        self.x = x
        self.y = y
        self.w = 85
        self.h = 40
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
    
    def draw(self, canvas, font="Arial 48 bold"):
        canvas.create_rectangle(self.x, self.y,self.x+self.w,self.y+self.h, fill = self.color, outline = self.color)
        if self.text != "":
            if self.text == "-":
                canvas.create_text((self.w/2 + self.x), (15 + self.y), text = self.text, font = font, fill = self.textColor)
            else:
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
            print("adjusted")
            return True
        return False

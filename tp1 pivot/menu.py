from cmu_112_graphics import *
from blurs import *
from noise import *
from sharpen import *
from interface import *
from dropdown import *
import os
import cv2
import math
import numpy as np

class menu:
    def __init__(self, x, y, fields = dict()):
        self.x = x
        self.y = y
        self.w = 200
        self.h = (len(fields) + 1) * 30 
        self.light = "#CED4DA"
        self.dark = "#495057"
        self.color = self.light
        self.show = False
        self.f = fields
        self.buttons = []
        self.createMenuButtons()
    
    def createMenuButtons(self):
        count = 0
        for key in self.f:
            self.buttons.append(menuButton(self.x + 100, self.y + (20 * count) + 10, 90, 20, key, count, self.f))
            count += 1
    
    def draw(self, canvas):
        if self.show:
            canvas.create_rectangle(self.x, self.y, self.x + self.w, self.y + self.h, fill = self.color, outline = self.color)
            self.drawText(canvas)
            for b in self.buttons:
                b.draw(canvas)

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
    

class menuButton():
    def __init__(self, x, y, w, h, key, number = None, fields = None):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.key = key
        self.text = "Select"
        self.num = number
        if self.num == 0:
            self.field = "Type"
        elif self.num == 1:
            self.field = "Kernel"
        elif self.num == 2:
            self.field = "Sigma"
        elif self.num == 3:
            self.field = "Speed"
        self.dark = "#495057"
        self.light = "#CED4DA"
        self.color = self.dark
        self.textColor = self.light
        self.fields = fields
        self.dropMenu = drop(self.x, self.y, self.w, self.fields[self.field])

    def changeColor(self, color):
        self.color = color
        if color == self.light:
            self.textColor = self.dark
        else:
            self.textColor = self.light
    
    def draw(self, canvas, font=None):
        self.dropMenu.draw(canvas)
        canvas.create_rectangle(self.x, self.y, self.x+self.w, self.y+self.h, fill = self.color, outline = self.color)
        if self.text != "":
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
            self.dropMenu.expanded = not self.dropMenu.expanded
            print(self.text)
    
    def function(self, img):
        if app.loaded:
            print(self.text)
            if self.num == 0:
                pass
            elif self.num == 1:
                pass
            elif self.num == 2:
                pass
            elif self.num == 3:
                pass
            elif self.num == 4:
                pass
            elif self.num == 5:
                pass
            elif self.num == 6:
                pass
            elif self.num == 7:
                pass
            else:
                pass
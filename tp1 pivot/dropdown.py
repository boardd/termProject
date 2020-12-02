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

class drop():
    def __init__(self, x, y, w, field):
        self.x = x
        self.y = y
        self.w = w
        self.h = len(field)* 20
        self.midx = (self.x + self.w) / 2
        self.midy = (self.y + 20) / 2
        self.f = field
        self.buttons = []
        self.dark = "#212529"
        self.light = "#CED4DA"
        self.color = self.light
        self.expanded = False
        self.selected = ""
        self.show = False
        for i in range(len(self.f)):
            self.buttons.append(dropButton(self.x, self.y + (20*(i+1)), 90, 20, self.f[i], i))
    
    def draw(self, canvas):
        if self.expanded:
            canvas.create_rectangle(self.x, self.y, self.x+self.w, self.y + self.h, fill = self.color, outline = self.color)
            for b in self.buttons:
                b.draw(canvas)
        elif self.selected != "":
            canvas.create_rectangle(self.x, self.y, self.x+self.w, self.y + 20, fill = self.color, outline = self.color)
            canvas.create_text(self.midx, self.midy, text = f"{self.selected}", fill = self.dark)

    def click(self, x, y):
        if self.show:
            if ((self.x < x < self.x + self.w) and
                (self.y < y < self.y + self.h)):
                return True
            return False

class dropButton():
    def __init__(self, x, y, w, h, text = "", number = None):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.text = text
        self.num = number
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
        canvas.create_rectangle(self.x, self.y, self.x+self.w, self.y+self.h, fill = self.color, outline = self.color)
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
            return True
        return False
    
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
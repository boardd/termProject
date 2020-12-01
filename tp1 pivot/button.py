from cmu_112_graphics import *
from blurs import *
from noise import *
from sharpen import *
from interface import *
import os
import cv2
import math
import numpy as np

class button:
    def __init__(self, x, y, w, h, text = "", number = None):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.text = text
        self.num = number
        self.color = "#CDCDCD"
    
    def changeColor(self, color):
        self.color = color
    
    def draw(self, canvas, font=None):
        canvas.create_rectangle(self.x, self.y,self.x+self.w,self.y+self.h, fill = self.color, outline = "black")
        if self.text != "":
            canvas.create_text((self.w/2 + self.x), (self.h/2 + self.y), text = self.text, font = font)
    
    def hover(self, x, y):
        if ((self.x < x < self.x + self.w) and
            (self.y < y < self.y + self.h)):
            self.changeColor("#FFFFFF")
        else:
            self.changeColor("#CDCDCD")
    
    def click(self, x, y):
        if ((self.x < x < self.x + self.w) and
            (self.y < y < self.y + self.h)):
            return True
        return False
    
    def function(self, img):
        print(self.text)
        if self.num == 0:
            return blur(img, 3, True, 1)
        elif self.num == 1:
            return edgeDetection(img, "laplacian")
        elif self.num == 2:
            return bilateral(img, 3, 20, 100)
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
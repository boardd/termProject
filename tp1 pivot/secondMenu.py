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

class secondMenu():
    def __init__(self, x, y, fields = []):
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
            self.buttons.append(secondMenuButton(self.x + 10, self.y + (20 * count), 90, 20, key, count))
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

class secondMenuButton():
    def __init__(self, x, y, w, h, key, number = None):
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
   
    
    def detectClick(self, x, y):
        if ((self.x < x < self.x + self.w) and
            (self.y < y < self.y + self.h)):
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

# class drop():
#     def __init__(self, x, y, w, field):
#         self.x = x
#         self.y = y
#         self.w = w
#         self.h = len(field)* 20
#         self.midx = (self.x + self.w) / 2
#         self.midy = (self.y + 20) / 2
#         self.f = field
#         self.buttons = []
#         self.dark = "#212529"
#         self.light = "#CED4DA"
#         self.color = self.light
#         self.expanded = False
#         self.selected = ""
#         self.show = False
#         for i in range(len(self.f)):
#             self.buttons.append(dropButton(self.x, self.y + (20*(i+1)), 90, 20, self.f[i], i))
    
#     def draw(self, canvas):
#         if self.expanded:
#             canvas.create_rectangle(self.x, self.y, self.x+self.w, self.y + self.h, fill = self.color, outline = self.color)
#             for b in self.buttons:
#                 b.draw(canvas)
#         elif self.selected != "":
#             canvas.create_rectangle(self.x, self.y, self.x+self.w, self.y + 20, fill = self.color, outline = self.color)
#             canvas.create_text(self.midx, self.midy, text = f"{self.selected}", fill = self.dark)

#     def click(self, x, y):
#         if self.show:
#             if ((self.x < x < self.x + self.w) and
#                 (self.y < y < self.y + self.h)):
#                 return True
#             return False

# class dropButton():
#     def __init__(self, x, y, w, h, text = "", number = None):
#         self.x = x
#         self.y = y
#         self.w = w
#         self.h = h
#         self.text = text
#         self.num = number
#         self.dark = "#495057"
#         self.light = "#CED4DA"
#         self.color = self.dark
#         self.textColor = self.light

#     def changeColor(self, color):
#         self.color = color
#         if color == self.light:
#             self.textColor = self.dark
#         else:
#             self.textColor = self.light
    
#     def draw(self, canvas, font=None):
#         canvas.create_rectangle(self.x, self.y, self.x+self.w, self.y+self.h, fill = self.color, outline = self.color)
#         if self.text != "":
#             canvas.create_text((self.w/2 + self.x), (self.h/2 + self.y), text = self.text, font = font, fill = self.textColor)
    
#     def hover(self, x, y):
#         if ((self.x < x < self.x + self.w) and
#             (self.y < y < self.y + self.h)):
#             self.changeColor(self.light)
#         else:
#             self.changeColor(self.dark)
   
    
#     def click(self, x, y):
#         if ((self.x < x < self.x + self.w) and
#             (self.y < y < self.y + self.h)):
#             return True
#         return False
    
#     def function(self, img):
#         if app.loaded:
#             print(self.text)
#             if self.num == 0:
#                 pass
#             elif self.num == 1:
#                 pass
#             elif self.num == 2:
#                 pass
#             elif self.num == 3:
#                 pass
#             elif self.num == 4:
#                 pass
#             elif self.num == 5:
#                 pass
#             elif self.num == 6:
#                 pass
#             elif self.num == 7:
#                 pass
#             else:
#                 pass
from cmu_112_graphics import *
from blurs import *
from noise import *
from sharpen import *
from interface import *
from menu import *
import os
import cv2
import math
import numpy as np

class button():
    def __init__(self, x, y, w, h, text = "", number = None, fields = None):
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
        self.fields = fields
        self.actions = []
        if self.fields != None:
            self.bMenu = menu(self.x + self.w, self.y, self.fields)
    
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
        if self.fields != None:
            self.bMenu.draw(canvas)
    
    def hover(self, x, y):
        if ((self.x < x < self.x + self.w) and
            (self.y < y < self.y + self.h)):
            self.changeColor(self.light)
            if self.fields != None:
                self.bMenu.show = True
        else:
            if self.fields != None:
                if self.bMenu.hover(x,y) and self.bMenu.show:
                    self.bMenu.show = True
                    for b in self.bMenu.inputs:
                        b.hover(x,y)
                    self.bMenu.doneButton.hover(x,y)
                else:
                    for b in self.bMenu.inputs:
                        b.changeColor(b.dark)
                    self.bMenu.show = False
                    self.changeColor(self.dark)
            else:
                self.changeColor(self.dark)
        
    def click(self, x, y):
        if ((self.x < x < self.x + self.w) and
            (self.y < y < self.y + self.h)):
            return True
        return False

    def menuClick(self, x, y):
        if self.bMenu.show:
            for b in self.bMenu.inputs:
                b.detectClick(x,y)
            if self.bMenu.doneButton.click(x,y):
                self.actions.append(self.text)
                for field in self.bMenu.inputs:
                    self.actions.append(field.text)
                    field.text = "Click Here"
                self.bMenu.show = False
                
                return self.actions
        return []
    
    def menuInput(self, key):
        if self.bMenu.show:
            for b in self.bMenu.inputs:
                b.takeInput(key)


from cmu_112_graphics import *
from blurs import *
from noise import *
from sharpen import *
from interface import *
from adjustmentMenu import *
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
        self.special = {"CROP", "FILTER"}
        self.regularMenus = {"BLUR", "SHARPEN", "DENOISE"}
        self.adjMenus = {"COLOR", "CONTRAST", "BRIGHTNESS"}
        self.type = None
        self.dark = "#495057"
        self.light = "#CED4DA"
        self.color = self.dark
        self.textColor = self.light
        self.fields = fields
        print(self.fields)
        self.actions = []
        if self.text in self.special:
            self.type = 1
            self.bMenu = menu(self.x + self.w, self.y, self.fields)
        if self.text in self.regularMenus:
            self.type = 2
            self.bMenu = menu(self.x + self.w, self.y, self.fields)
        elif self.text in self.adjMenus:
            self.type = 3
            self.bMenu = adjMenu(self.x + self.w, self.y)

            
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
                    if self.type == 2:
                        for b in self.bMenu.inputs:
                            b.hover(x,y)
                        self.bMenu.doneButton.hover(x,y)
                    if self.type == 3:
                        self.bMenu.minusButton.hover(x,y)
                        self.bMenu.plusButton.hover(x,y)
                else:
                    if self.type == 2:
                        for b in self.bMenu.inputs:
                            b.changeColor(b.dark)
                    if self.type == 3:
                        self.bMenu.minusButton.changeColor(self.bMenu.minusButton.dark)
                        self.bMenu.plusButton.changeColor(self.bMenu.plusButton.dark)
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
        self.actions = []
        if self.bMenu.show:
            if self.type == 2:
                for b in self.bMenu.inputs:
                    b.detectClick(x,y)
                if self.bMenu.doneButton.click(x,y):
                    self.actions.append(self.text)
                    for field in self.bMenu.inputs:
                        self.actions.append(field.text)
                        field.text = "Click Here"
                    self.bMenu.show = False
                    return self.actions
            if self.type == 3:
                if self.bMenu.plusButton.click(x,y):
                    self.actions.append(self.text)
                    self.actions.append(self.bMenu.plusButton.text)
                    return self.actions
                elif self.bMenu.minusButton.click(x,y):
                    self.actions.append(self.text)
                    self.actions.append(self.bMenu.minusButton.text)
                    return self.actions
        return []
    
    def menuInput(self, key):
        if self.type == 2:
            if self.bMenu.show:
                for b in self.bMenu.inputs:
                    b.takeInput(key)


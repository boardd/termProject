import cv2
import numpy as np

class kernelMenu():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 200
        self.h = 250
        self.light = "#CED4DA"
        self.dark = "#495057"
        self.color = self.light
        self.show = False
        self.done = False
        self.inputs = []
        self.createMenuInputs()
        self.createDoneButton()
    
    def createDoneButton(self):
        self.doneButton = kernelDoneButton(self.x + (self.w * 3/4), (self.y + self.h) - 30, 40, 20, text = "Done" )
    
    def createMenuInputs(self):
        for row in range(5):
            temp = []
            for col in range(5):
                temp.append(kernelInputField(self.x + 40*col, self.y + 40*row, 40, 40))
            self.inputs.append(temp)

    def draw(self, canvas):
        if self.show:
            canvas.create_rectangle(self.x, self.y, self.x + self.w, self.y + self.h, fill = self.color, outline = self.color)
            for row in self.inputs:
                for b in row:
                    b.draw(canvas)
            self.doneButton.draw(canvas)
            
    def hover(self, x, y):
        if ((self.x < x < self.x + self.w) and
            (self.y < y < self.y + self.h)):
            return True
        return False


class kernelInputField():
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.text = "[-]"
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
            if self.text != "[]":
                self.text = "[]"
    
    def takeInput(self, key):
        if self.clicked == True:
            if key == "Enter":
                self.clicked = False
                return
            if key == "Delete":
                self.text = self.text[:-2] + "]"
            else:
                self.text = self.text[:-1] + key + "]"
            print(self.text)

    def returnText(self):
        return self.text

class kernelDoneButton():
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

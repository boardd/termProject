class button:
    def __init__(self, x, y, w, h, text = ""):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.text = text
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
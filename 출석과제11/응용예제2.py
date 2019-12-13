from tkinter import *
import math
import random
class Shape:            
    color, width = '', 0
    shX1, shY1, shX2, shY2 = [0] * 4   
    def drawShape(self):                
        raise NotImplementedError()
class Rectangle(Shape):                  
    objects = None                       
    def __init__(self, x1, y1, x2, y2, c, w):
        self.shX1 = x1
        self.shY1 = y1
        self.shX2 = x2
        self.shY2 = y2
        self.color = c
        self.width = w
        self.drawShape()
    def __del__(self) : 
        for obj  in self.objects :
            canvas.delete(obj)
    def drawShape(self) :
        sx1 = self.shX1; sy1 = self.shY1; sx2 = self.shX2; sy2 =self.shY2
        squreList = []        
        squreList.append(canvas.create_line(sx1, sy1, sx1, sy2, fill = self.color, width = self.width))
        squreList.append(canvas.create_line(sx1, sy2, sx2, sy2, fill = self.color, width = self.width))
        squreList.append(canvas.create_line(sx2, sy2, sx2, sy1, fill = self.color, width = self.width))
        squreList.append(canvas.create_line(sx2, sy1, sx1, sy1, fill = self.color, width = self.width))
        self.objects=squreList         
class Circle(Shape) :          
    objects = None
    def __init__(self,  x1, y1, x2, y2, c, w):
        self.shX1 = x1
        self.shY1 = y1
        self.shX2 = x2
        self.shY2 = y2
        self.color = c
        self.width = w
        self.drawShape()
    def __del__(self) :            
        canvas.delete(self.objects)
    def drawShape(self) : 
        sx1= self.shX1;   sy1= self.shY1;  sx2 = self.shX2;   sy2 = self.shY2
        self.objects = canvas.create_oval(sx1, sy1, sx2, sy2, outline = self.color, width = self.width)
def  getColor() :   
    r = random.randrange(16, 256)
    g = random.randrange(16, 256)
    b = random.randrange(16, 256)
    return "#" + hex(r)[2:] + hex(g)[2:] + hex(b)[2:] 
def getWidth() :
    return random.randrange(1, 9)
def  startDrawRect(event):
    global x1, y1, x2, y2, shapes
    x1 = event.x
    y1 = event.y
def endDrawRect(event):
    global x1, y1, x2, y2, shapes
    x2 = event.x
    y2 = event.y
    rect = Rectangle(x1, y1, x2, y2, getColor(), getWidth())
    shapes.append(rect) 
def  startDrawCircle(event):
    global x1, y1, x2, y2, shapes
    x1=event.x
    y1=event.y
def endDrawCircle(event):
    global x1, y1, x2, y2, shapes
    x2=event.x
    y2=event.y
    cir = Circle(x1, y1, x2, y2, getColor(), getWidth())
    shapes.append(cir)  
def  deleteShape(event):
    global shapes
    if len(shapes) != 0 :
        shp = shapes.pop()
        del(shp)
shapes = []
window = None
canvas = None
x1, y1, x2, y2 = None, None, None, None 
if __name__ == "__main__" :
    window=Tk()
    window.title("객체지향 그림판")
    canvas = Canvas(window, height = 300, width = 300)
    canvas.bind("<Button-1>", startDrawRect)
    canvas.bind("<ButtonRelease-1>", endDrawRect)
    canvas.bind("<Button-2>", deleteShape)
    canvas.bind("<Button-3>", startDrawCircle)
    canvas.bind("<ButtonRelease-3>", endDrawCircle)
    canvas.pack()
    window.mainloop()

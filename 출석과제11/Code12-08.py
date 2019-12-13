import turtle
import random
class Shape:
    myTurtle = None
    cx, cy = 0, 0
    def __init__(self):
        self.myTurtle = turtle.Turtle('turtle') 
    def setPen(self) :
        r = random.random()
        g = random.random()
        b = random.random()
        self.myTurtle.pencolor((r, g, b))
        pSize = random.randrange(1,10)
        self.myTurtle.pensize(pSize)                
    def drawShape(self):
        pass
class Rectangle(Shape):
    width, height = [0] * 2
    def __init__(self, x, y):
        Shape.__init__(self)  
        self.cx = x
        self.cy = y
        self.width = random.randrange(20, 100)
        self.height = random.randrange(20, 100)
    def drawShape(self) :
        sx1, sy1, sx2, sy2 = [0] * 4
        sx1 = self.cx - self.width/2
        sy1 = self.cy - self.height /2
        sx2 = self.cx + self.width/2
        sy2 = self.cy + self.height /2
        self.setPen()
        self.myTurtle.penup()
        self.myTurtle.goto(sx1, sy1)
        self.myTurtle.pendown()
        self.myTurtle.goto(sx1, sy2)
        self.myTurtle.goto(sx2, sy2)
        self.myTurtle.goto(sx2, sy1)
        self.myTurtle.goto(sx1, sy1)
def  screenLeftClick(x,y):
    rect = Rectangle(x, y)
    rect.drawShape()
turtle.title('거북이로 객체지향 사각형  그리기')
turtle.onscreenclick(screenLeftClick,1)
turtle.done()

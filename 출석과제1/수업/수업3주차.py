"""
num=input("16진수값 입력:")
if num>='G' and num<='Z':
    print("16진수가 아닙니다")
else:
    num10=int(num,16)
    print("10진수==>",num10)

"""
"""
import turtle
import random
turtle.shape('turtle')
def box(x,y,s,w):
    global r,g,b
    r=random.random()
    g=random.random()
    b=random.random()
    turtle.pendown()
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.pencolor((r,g,b))
    for i in range(0,4):
        turtle.forward(s)
        turtle.right(90)
        if i==0:
            turtle.penup()
            turtle.goto(x+s-10,y-15)
            turtle.write(w)
            turtle.goto(x+s,y)
            turtle.pendown()
box(150,200,50,7)
r,g,b=1.0,1.0,1.0
turtle.title('거북이로 그림그리기')

turtle.done()
"""

"""
print("\t\t\t\t\t%2d"%1)
print("\t\t\t\t%2d\t%2d\t%2d\n"%(1,2,1))
print("\t\t\t%2d\t%2d\t%2d\t%2d\t%2d\n"%(1,2,4,2,1))
print("\t\t%2d\t%2d\t%2d\t%2d\t%2d\t%2d\t%2d\n"%(1,2,4,8,4,2,1))
print("\t%2d\t%2d\t%2d\t%2d\t%2d\t%2d\t%2d\t%2d\t%2d"%(1,2,4,8,16,8,4,2,1))
"""


a=int(input("10진수를 입력하시오:"))
while True:
    num=a%2
    a=a//2
    print(num)
    if a<=0:
        break
    


__author__ = 'mandla'
import turtle


class Point:
    """class representing a geometric point"""
    def __init__(self,x=0,y=0):
        """method to initialize coordinates"""
        self.x=x
        self.y=y

class Rectangle:
    """class representing a rectangle shape"""
    def __init__(self,p1,p2):
        """method to initialize rectangle"""
        self.ul = p1
        self.br = p2

    def includesPoint(self,p):
        """detects whether a point p is part of this rectangle"""
        return self.ul.x <= p.x <= self.br.x and self.br.y <=p.y <=self.ul.y

wn = turtle.Screen()
wn.setup(500,500)
tess = turtle.Turtle()
tess.shape('turtle')
tess.penup()
screen=Rectangle(Point(-250,250),Point(250,-250))
#print(Rectangle.__init__.__doc__)
step=10

def check():
    if not screen.includesPoint(Point(tess.xcor(),tess.ycor())):
        wn.title('({:.2f},{:.2f}) tess is off the screen'.format(tess.xcor(),tess.ycor()))

def right():
    if tess.heading() == 270:
        tess.left(90)
        tess.forward(step)
        check()
    else:
        diff=0-tess.heading()
        tess.left(diff)
        tess.forward(step)
        check()

def left():
    diff=180-tess.heading()
    tess.left(diff)
    tess.forward(step)
    check()

def up():
    diff=90-tess.heading()
    tess.left(diff)
    tess.forward(step)
    check()

def down():
    if tess.heading() == 0:
        tess.right(90)
        tess.forward(step)
        check()
    else:
        diff=270-tess.heading()
        tess.left(diff)
        tess.forward(step)
        check()

wn.onkey(right,'Right')
wn.onkey(left,'Left')
wn.onkey(up,'Up')
wn.onkey(down,'Down')

wn.listen()
wn.mainloop()